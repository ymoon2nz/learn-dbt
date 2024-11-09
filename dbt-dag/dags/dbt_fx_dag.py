import os 
from datetime import datetime 
from pathlib import Path 

from cosmos import DbtDag, ProjectConfig, ProfileConfig, ExecutionConfig
from cosmos.profiles import PostgresUserPasswordProfileMapping 


DEFAULT_DBT_ROOT_PATH = Path(__file__).parent / "dbt" 
DBT_ROOT_PATH = Path(os.getenv("DBT_ROOT_PATH", DEFAULT_DBT_ROOT_PATH)) 

profile_config = ProfileConfig( 
    profile_name="default", 
    target_name="dev", 
    profile_mapping=PostgresUserPasswordProfileMapping( 
        conn_id="postgres_conn", 
        profile_args={"schema": "fx"}, 
    )
)

dbt_postgres_dag = DbtDag(
    project_config = ProjectConfig("/usr/local/airflow/dags/dbt/fx_tutorial",),
    operator_args = {"install_deps": True},
    profile_config = profile_config,
    execution_config = ExecutionConfig(dbt_executable_path=f"{os.environ['AIRFLOW_HOME']}/dbt_venv/bin/dbt",),
    schedule_interval = "@daily",
    start_date = datetime(2024, 11, 8),
    catchup=False,
    dag_id="dbt_fx_dag",
)