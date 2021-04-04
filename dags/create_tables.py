from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.postgres_operator import PostgresOperator


default_args = {
    'owner': 'zongyliu',
    'depends_on_past': False,
    'retries': 3,
    'retry_delay': timedelta(minutes=5),
    'catchup': False,
    'email_on_retry': False
}


dag = DAG(
    'create_table_dag',
    start_date=datetime.now(),
    default_args=default_args,
    template_searchpath = ['/home/workspace/airflow/']
)

create_table = PostgresOperator(
        task_id="create_tables",
        dag=dag,
        postgres_conn_id="redshift",
        sql=['create_tables.sql']
    )

    
create_table