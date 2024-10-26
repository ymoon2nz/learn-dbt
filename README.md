# learn-dbt
Learn dbt

## Install
```
#pip install dbt-postgres

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
* Create dbt env
```
dbt init test1
```
* Check dbt
```
dbt debug
```

