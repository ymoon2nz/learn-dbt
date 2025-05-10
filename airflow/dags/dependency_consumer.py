from airflow.decorators import dag, task
from airflow import Dataset
from datetime import datetime

# arn:aws:s3:::ymoon-au-fx-raw

data_a = Dataset("s3://bucket_a/data_a")
data_b = Dataset("s3://bucket_b/data_b")

@dag(start_date=datetime(2024, 11, 13), schedule=[data_a, data_b], catchup=False)
def dependency_consumer():

    @task
    def run():
        print('consumer run')

    run()


dependency_consumer()