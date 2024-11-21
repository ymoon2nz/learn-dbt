from airflow.decorators import dag, task
from datetime import datetime

@dag(start_date=datetime(2024, 11, 11), schedule='@daily', catchup=False)
def dependency_target():

    @task
    def message(dag_run=None):
        print(dag_run.conf.get("message"))
    
    message()

dependency_target()