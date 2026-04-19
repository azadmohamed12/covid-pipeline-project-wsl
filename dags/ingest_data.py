from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id="ingest_data",
    start_date=datetime(2024, 1, 1),
    schedule_interval="@daily",
    catchup=False,
) as dag:
    ingest = BashOperator(
        task_id="download_raw_data",
        bash_command="bash /opt/airflow/scripts/run_pipeline.sh ingest"
    )
