from asyncio import Task
from airflow import DAG
from datetime import timedelta, datetime
from airflow.operators.python import PythonOperator
from airflow.operators.postgres_operator import PostgresOperator
from airflow.decorators import dag, task
import yfinance
import json

DAG_ID = "fx_nzd_dag"

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2024, 11, 11),
    "email": ["myemail@domain.com"],
    "email_on_failure": False,
    "email_on_retruy": False,
    "retries": 2,
    "retry_delay": timedelta(minutes=3),
    "provide_context": True
}

def get_yf_nzd_json():
    """Download NZD Exchange Rate"""
    start_date = datetime.today()- timedelta(7) 
    end_date = datetime.today()
    stock ="NZDUSD=X"
    yf_json=yfinance.download(stock, start_date, end_date).to_json()
    return yf_json

#@task(execution_timeout=timedelta(minutes=3))
def _yf_nzd_json(ti):
    """Download NZD Exchange Rate"""
    start_date = datetime.today()- timedelta(7) 
    end_date = datetime.today()
    stock ="NZDUSD=X"
    yf_json=yfinance.download(stock, start_date, end_date).to_json()
    ti.xcom_push(key="yf_json", value=yf_json)

def _get_yf_nzd_json(ti):
    """Retrieve Downloaded NZD Exchange Rate"""
    yf_json = ti.xcom_pull(task_ids=f'_yf_nzd_json', key='yf_json')
    print(yf_json)
    return yf_json

with DAG(
    default_args=default_args,
    dag_id=DAG_ID,
    start_date=datetime(2024, 11, 11),
    schedule="@daily",
    catchup=False
) as dag:
    create_fx_dump_table = PostgresOperator(
        task_id='create_fx_dump_table',
        postgres_conn_id='postgres_conn',
        sql="""
            CREATE TABLE IF NOT EXISTS fx.fx_dump (
            fx_dump_id SERIAL PRIMARY KEY,
            type TEXT,
            info TEXT,
            dump JSON,
            updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
            """
    )
    
    # yf_nzd_json = PythonOperator(
    #     task_id="yf_nzd_json",
    #     python_callable=_yf_nzd_json
    # )

    populate_fx_dump_table = PostgresOperator(
        task_id='insert_fx_dump',
        postgres_conn_id='postgres_conn',
        sql="""
            INSERT INTO fx.fx_dump (type, info, dump)
            VALUES ('yfinance.fx.daily','NZDUSD=X:NZDUSD=X', %(json)s)
            """,
        #parameters={ "json" : json.dumps({ "NZDUSD=X" : {} }) }
        parameters={ "json" : get_yf_nzd_json() }
    )

    [create_fx_dump_table] >> populate_fx_dump_table
