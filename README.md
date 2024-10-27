# learn-dbt
Learn dbt

## Install
### ref - https://docs.getdbt.com/docs/core/pip-install
* Get dbt Package by pip
```
pip install dbt-postgres
# OR
python -m pip install \
  dbt-core \
  dbt-postgres \
  dbt-redshift \
  dbt-snowflake \
  dbt-bigquery \
  dbt-trino
```
* Setup Python Environment
```
python -m venv dbt-env
source dbt-env/bin/activate
```
* dbt core & postgres adapter
```
#python -m pip install dbt-core dbt-ADAPTER_NAME
python -m pip install dbt-core dbt-postgres
```

## Tutorial 0

## Tutorial 1

## Tutorial 2

* Run PostgreSQL as docker
```
docker run -itd \
    -e POSTGRES_USER=postgres -e POSTGRES_DB=postgres -e POSTGRES_PASSWORD=postgres1 \
    -p 5432:5432 \
    -v ./containers/postgres1/data:/var/lib/postgresql/data \
    --name postgres1 \
    postgres
```
* Copy file to docker
```
docker cp {file} postgres1:/var/lib/postgresql/.
```
* Add Test Data
```
docker exec -it postgres1 bash
su - postgres
psql
  \c postgres
  CREATE SCHEMA dbt;
  SET search_path TO dbt;
  CREATE TABLE dbt.test1 (col1 int, col2 varchar);
  insert into dbt.test1 values (1, 'hello');
  insert into dbt.test1 values (2, 'postgres');
```
* [stock-us]
``` sql
-- Date,AAPL,FB,GOOG,JPM,NVDA,^GSPC
CREATE TABLE stock_us (
    ID SERIAL,
    DATE DATE,
    AAPL NUMERIC(12,2) ,
    FB NUMERIC(12,2) ,
    GOOG NUMERIC(12,2) ,
    JPM NUMERIC(12,2) ,
    NVDA NUMERIC(12,2) ,
    "^GSPC" NUMERIC(12,2),
    UPDATED timestamp DEFAULT CURRENT_TIMESTAMP
);
```
* Import from file (csv)
```
COPY stock_us(DATE, AAPL, FB, GOOG, JPM, NVDA, "^GSPC")
FROM '/var/lib/postgresql/stock-us.csv'
DELIMITER ','
CSV HEADER;
```
* Create dbt env
```
dbt init test1
```
* Check dbt
```
dbt debug
```

