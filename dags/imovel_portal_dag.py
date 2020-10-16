from datetime import datetime
import logging

from airflow import DAG
from airflow.models import Variable
from airflow.contrib.operators.ecs_operator import ECSOperator

logger = logging.getLogger(__name__)

default_args = {
    'owner': 'judith',
    'start_date': datetime(2020, 10, 15),
    'depends_on_past': False,
    'provide_context': True
}

with DAG('imovel_portal_dag',
          description='Dag dos imóveis do portal',
          schedule_interval=None,
          catchup=False,
          default_args=default_args) as dag:


    t1 = ECSOperator(
        task_id="imovel_portal_extract",
        dag=dag,
        aws_conn_id="aws_default",
        cluster="airflow-production-ecs-cluster",
        task_definition="production-imovel-portal-extract-image",
        launch_type="FARGATE",
        overrides={
            "containerOverrides": [
                {
                    "name": "dev-imovel-portal-extract-image",
                    "command": ["python", "main.py"],
                },
            ],
        },
        network_configuration={
            "awsvpcConfiguration": {
                "securityGroups": [Variable.get("security-group")],
                "subnets": [Variable.get("subnet")],
                "assingPublicIp": "ENABLED"
            },
        },
    )

    t1
