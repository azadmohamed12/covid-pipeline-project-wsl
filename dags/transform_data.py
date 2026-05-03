from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id="transform_data",
    start_date=datetime(2024, 1, 1),
    schedule="@daily",
    catchup=False,
) as dag:

    transform = BashOperator(
        task_id="run_transform",
        bash_command="python3 /opt/airflow/scripts/transform.py"
    )