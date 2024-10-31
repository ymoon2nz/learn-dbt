# learn-dbt
Learn dbt

## Postgres ``docker``
* Run PostgreSQL as docker
```
cd ~
mkdir -p ./containers/postgres1/data
docker run -itd \
    -e POSTGRES_USER=postgres -e POSTGRES_DB=postgres -e POSTGRES_PASSWORD=postgres1 \
    -p 5432:5432 \
    -v ./containers/postgres1/data:/var/lib/postgresql/data \
    --name postgres1 \
    postgres
```
## Setup & Install ``dbt``
### ref - https://docs.getdbt.com/docs/core/pip-install
* (Mac) Brew Updates for psycopg2
```
brew install postgresql

pip install psycopg2-binary
# OR
pip install psycopg2
```
* Get dbt Package by pip
```
# dbt postgres adapter
pip install dbt-postgres
# OR
# dbt core & adapters (dbt-ADAPTER_NAME)
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
python -m venv py-env
source py-env/bin/activate
```

## Run ``dbt``
* Create dbt env
```
dbt init {project-name}
# Follow the prompts
```
* Run dbt
```
dbt run
```
* Run for a model (including sub)
```
dbt run --models +hist_all
```
* Check dbt
```
dbt debug
```
* Generate Docs
```
dbt docs generate
```
* Serve as web for docs
```
dbt docs serve
```

## Tutorial
### FX Project
* Create PostgreSQL user
```
docker cp dbt-dev-db.sql postgres1:/var/lib/postgresql/data/.
docker exec --user postgres \
  --workdir /var/lib/postgresql/data/ \
  -it postgres1 psql -f dbt-dev-db.sql
```
* Create ``fx_tutorial`` Project
```
dbt init fx_tutorial

# #######
# 01:23:35  Setting up your profile.
# Which database would you like to use?
# ...
# [5] postgres
# Enter a number: 5
# host (hostname for the instance): localhost
# port [5432]:
# user (dev username): dev
# pass (dev password):
# dbname (default database that dbt will build objects in): dbt
# schema (default schema that dbt will build objects in): fx_tutorial
# threads (1 or more) [1]: 1
# ########

# Connection Test...
cd fx_tutorial
dbt debug
```

* Seeding Currency Codes and History Data
```
dbt seed --select s1_currency_codes
dbt seed --select s1_req_collections

dbt seed --select s1_aud1980
dbt seed --select s1_aud1990
dbt seed --select s1_aud2000
dbt seed --select s1_aud2010
dbt seed --select s1_aud2020
```

* Models

* Macrosß

* Tests

* Snapshots

* Analyses

## Tips
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
* psql commands
```
# Connect to database
\c {database}
# List databases (+ for detail)
\l
\l+
# List schemas (+ for detail, S for all)
\dn
\dn+
\dnS
# List tables (+ for detail, S for all schemas)
\dt
\dt+
\dtS
```
* Import from file (csv)
```
COPY stock_us(DATE, AAPL, FB, GOOG, JPM, NVDA, "^GSPC")
FROM '/var/lib/postgresql/stock-us.csv'
DELIMITER ','
CSV HEADER;
```

