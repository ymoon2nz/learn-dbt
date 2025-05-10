import os
from airflow.decorators import dag, task
from datetime import datetime, timezone
from airflow.providers.amazon.aws.hooks.s3 import S3Hook
from airflow.providers.amazon.aws.sensors.s3 import S3KeySensor


AWS_S3_CONN_ID = "S3_conn"
S3_BUCKNAME = 'ymoon-au-fx-raw'
FILENAME = "nzd2usd-%s.json" % (datetime.now(timezone.utc).strftime("%Y%m%d"))
S3_LOCATE = 'hist/%s' % FILENAME

@dag(start_date=datetime(2024, 11, 11), schedule='@daily', catchup=False)
def aws_s3_data_upload():

    @task
    def start_aws_s3_data_upload():
        print ('Starting aws_s3_data_upload')
        print ('FILENAME= %s', FILENAME)
    
    @task
    def create_file():
        with open( ("/tmp/%s" % FILENAME), 'w') as f:
            f.write('{ "json": "TEST" }')
        print("Created - /tmp/%s" % FILENAME)

    @task
    def upload_to_s3():
        hook = S3Hook(AWS_S3_CONN_ID)
        hook.load_file(
            filename=("/tmp/%s" % FILENAME),
            key=S3_LOCATE,
            bucket_name=S3_BUCKNAME,
            replace=False
        )
    
    start_aws_s3_data_upload() >> create_file() >> upload_to_s3()

aws_s3_data_upload()