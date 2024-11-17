from airflow.decorators import dag, task
from datetime import datetime
from airflow.operators.trigger_dagrun import TriggerDagRunOperator

@dag(start_date=datetime(2024, 11, 11), schedule='@daily', catchup=False)
def dependency_controller():

    @task
    def start():
        print("dependency_controller start")

    trigger = TriggerDagRunOperator(
        task_id='trigger_dependency_target_dag',
        trigger_dag_id='dependency_target',
        conf={"message": "my_data"},
        wait_for_completion=True
    )

    @task
    def done():
        print("dependency_controller done")

    start() >> trigger >> done()

dependency_controller()