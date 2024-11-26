# ./plugins/metrics_plugin.py
from prometheus_client import start_http_server, Counter
from airflow.plugins_manager import AirflowPlugin
from airflow.utils.db import provide_session

METRIC_COUNTER = Counter('airflow_task_count', 'Number of tasks executed')

class MetricsPlugin(AirflowPlugin):
    name = "metrics_plugin"

    @provide_session
    def on_task_instance_success(self, context, session=None):
        METRIC_COUNTER.inc()

def start_exporter():
    start_http_server(8000)

start_exporter()