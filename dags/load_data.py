import logging
import os
from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook
from airflow.providers.postgres.operators.postgres import PostgresOperator

# -----------------------------
# LOAD FUNCTION
# -----------------------------
def load_csv_to_postgres():
    file_path = "/opt/airflow/data/covid_mini.csv"

    logging.info(f"Checking file at: {file_path}")

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"{file_path} not found")

    hook = PostgresHook(postgres_conn_id="postgres_default")
    conn = hook.get_conn()
    cur = conn.cursor()

    try:
        logging.info("Creating table if not exists...")

        cur.execute("""
            CREATE TABLE IF NOT EXISTS covid_table (
                location TEXT,
                date DATE,
                total_cases DOUBLE PRECISION,
                total_deaths DOUBLE PRECISION,
                population BIGINT
            );
        """)

        logging.info("Truncating table...")
        cur.execute("TRUNCATE TABLE covid_table;")

        logging.info("Loading CSV into Postgres...")

        with open(file_path, "r") as f:
            cur.copy_expert(
                """
                COPY covid_table(location, date, total_cases, total_deaths, population)
                FROM STDIN WITH CSV HEADER
                """,
                f
            )

        conn.commit()
        logging.info("✅ Data loaded successfully!")

    except Exception as e:
        conn.rollback()
        logging.error(f"❌ Error loading data: {e}")
        raise

    finally:
        cur.close()
        conn.close()


# -----------------------------
# DAG DEFINITION
# -----------------------------
with DAG(
    dag_id="load_data_clean",
    start_date=datetime(2024, 1, 1),
    schedule_interval=None,   # manual trigger (better for debugging)
    catchup=False,
    tags=["etl", "covid"],
) as dag:

    # LOAD TASK
    load_task = PythonOperator(
        task_id="load_to_postgres",
        python_callable=load_csv_to_postgres
    )

    # TRANSFORM TASK
    transform_task = PostgresOperator(
        task_id="transform_in_postgres",
        postgres_conn_id="postgres_default",
        sql="""
            DROP TABLE IF EXISTS covid_summary;

            CREATE TABLE covid_summary AS
            SELECT 
                location,
                date,
                total_cases,
                total_deaths,
                population,
                (total_deaths / NULLIF(population, 0)) * 100 AS death_rate
            FROM covid_table;
        """
    )

    # TASK ORDER
    load_task >> transform_task
