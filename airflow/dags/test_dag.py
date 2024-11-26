from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

def fail_task():
    raise ValueError("This task is supposed to fail")

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 1, 1),
    'retries': 1,
}

dag = DAG(
    'test_dag',
    default_args=default_args,
    description='A DAG to test failure',
    schedule_interval='@daily',
)

start = PythonOperator(
    task_id='start',
    python_callable=fail_task,
    dag=dag,
)

start
