Airflow Astronomer
-------

* Install
```
brew install astro
```

## Create ``dbt-dag``
* Init ``dbt-dag``
```
mkdir dbt-dag
cd dbt-dag
astro dev init
```
* Add ``Dockerfile``
```
RUN python -m venv dbt_venv && source dbt_venv/bin/activate && \
    pip install --no-cache-dir dbt-postgres && deactivate
```
* Add ``requirements.txt``
```
astronomer-cosmos
apache-airflow-providers-postgres
```
### Start Airflow
```
astro dev start
```