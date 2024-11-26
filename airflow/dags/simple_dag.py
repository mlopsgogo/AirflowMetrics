from datetime import datetime
from airflow import DAG
from airflow.operators.dummy import DummyOperator

# Определите аргументы по умолчанию для DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 10, 1),
    'retries': 1,
}

# Создайте DAG
dag = DAG(
    'simple_dag',
    default_args=default_args,
    description='A simple DAG',
    schedule_interval='@daily',
)

# Определите задачи
start = DummyOperator(
    task_id='start',
    dag=dag,
)

end = DummyOperator(
    task_id='end',
    dag=dag,
)

# Установите зависимости между задачами
start >> end