from airflow.decorators import dag, task
from airflow import Dataset
from datetime import datetime

# arn:aws:s3:::ymoon-au-dbt-fx-raw

data_a = Dataset("s3://bucket_a/data_a")
data_b = Dataset("s3://bucket_b/data_b")

@dag(start_date=datetime(2024, 11, 13), schedule='@daily', catchup=False)
def dependency_producer():

    @task(outlets=[data_a])
    def update_a():
        print("update a")
    
    @task(outlets=[data_b])
    def update_b():
        print("update b")

    update_a() >> update_b()


dependency_producer()