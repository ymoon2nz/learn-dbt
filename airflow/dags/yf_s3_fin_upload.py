from airflow.decorators import dag, task
from datetime import datetime, timezone
from airflow.providers.amazon.aws.hooks.s3 import S3Hook
from airflow.providers.amazon.aws.sensors.s3 import S3KeySensor
import os, json
import yfinance, pandas

AWS_S3_CONN_ID = "S3_conn"
S3_BUCKNAME = 'ymoon-au-fx-raw'
STOCK_SYMBOL = 'AIR.NZ'
FILENAME = "stock_details-%s-%s.json" % (datetime.now(timezone.utc).strftime("%Y%m%d"), STOCK_SYMBOL)
S3_PATH = 'hist'

@dag(start_date=datetime(2024, 11, 11), schedule='@daily', catchup=False)
def yf_s3_fin_upload():

    @task
    def start_aws_s3_data_upload():
        print ('Starting yf_s3_fin_upload')
        print ('FILENAME= %s', FILENAME)
    
    @task
    def download_yf_fin():

        ticker = yfinance.Ticker(STOCK_SYMBOL)
        pnl = ticker.financials
        bs = ticker.balancesheet
        cf = ticker.cashflow

        # ticker details into one dataframe
        fs = pandas.concat([pnl, bs, cf])
        fs_json = fs.to_json()
        with open( "/tmp/%s" % FILENAME, 'w') as f:
            f.write('{ "%s": %s }' % (STOCK_SYMBOL, fs_json))
        print("Created - /tmp/%s" % FILENAME)

    @task
    def upload_yf_to_s3():
        hook = S3Hook(AWS_S3_CONN_ID)
        filename = "/tmp/%s" % FILENAME
        print ("filename: %s" % FILENAME)
        hook.load_file(
            filename="/tmp/%s" % FILENAME,
            key="%s/%s" % (S3_PATH, FILENAME),
            bucket_name=S3_BUCKNAME,
            replace=True
        )
    
    start_aws_s3_data_upload() >> download_yf_fin() >> upload_yf_to_s3()

yf_s3_fin_upload()