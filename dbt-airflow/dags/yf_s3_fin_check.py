# ref: https://www.youtube.com/watch?v=mXaP2ag1CHo

from airflow.decorators import dag, task
from datetime import datetime
from airflow.providers.amazon.aws.hooks.s3 import S3Hook
from airflow.providers.amazon.aws.sensors.s3 import S3KeySensor

AWS_S3_CONN_ID = "S3_conn"
S3_BUCKNAME = 'ymoon-au-dbt-fx-raw'
S3_LOCATE = 'hist/nzd2usd.json'

@dag(start_date=datetime(2024, 11, 11), schedule='@daily', catchup=False)
def aws_s3_data_process():
    
    @task
    def start_sensor():
        print("S3 Sensor Start!")
        print(" AWS_S3_CONN_ID: ", AWS_S3_CONN_ID)
        print(" S3_BUCKNAME: ", S3_BUCKNAME)

    # @task
    # def s3_retrieve():
    #     source_s3_key = ""
    #     source_s3_bucket = ""
    #     source_s3 = S3Hook(AWS_S3_CONN_ID)
    s3_sensor = S3KeySensor(
        task_id='s3_file_check',
        aws_conn_id=AWS_S3_CONN_ID,
        bucket_name=S3_BUCKNAME,
        bucket_key=S3_LOCATE,
        poke_interval=60,
        timeout=180,
        soft_fail=False,
        retries=2,
    )

    @task
    def end_sensor():
        print("S3 Sensor Completed!")

    start_sensor() >> s3_sensor >> end_sensor()

aws_s3_data_process()