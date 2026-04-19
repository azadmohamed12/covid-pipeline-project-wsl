from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.sensors.external_task import ExternalTaskSensor
from datetime import datetime

with DAG(
    dag_id="transform_data",
    start_date=datetime(2024, 1, 1),
    schedule="@daily",
    catchup=False,
) as dag:

    wait_for_ingest = ExternalTaskSensor(
        task_id="wait_for_ingest",
        external_dag_id="ingest_data",
        external_task_id="download_raw_data",
        poke_interval=30,
        timeout=900,
        mode="reschedule",
    )

    transform = BashOperator(
        task_id="run_transform",
        bash_command="python /opt/airflow/scripts/transform.py"
    )

    wait_for_ingest >> transform