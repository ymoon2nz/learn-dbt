from datetime import datetime
from airflow.decorators import dag, task
from airflow.providers.microsoft.azure.hooks.wasb import WasbHook

WASB_CONN_ID = "az_conn"
CONTAINER_NAME = "test"
BLOB_NAME = "nzd2usd.json"

@dag(start_date=datetime(2024, 11, 11), schedule='@daily', catchup=False)
def az_blob_data_process():

    @task
    def get_blob_list():
        wh = WasbHook(wasb_conn_id='az_conn')
        print (wh.get_blobs_list(CONTAINER_NAME))

    get_blob_list()

az_blob_data_process()