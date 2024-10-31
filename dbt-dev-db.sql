-- Create dbt database for dev user
DROP DATABASE dbt;
DROP USER dev;
CREATE database dbt;
CREATE USER dev WITH PASSWORD 'dbtdev' SUPERUSER;
GRANT ALL PRIVILEGES ON DATABASE dbt TO dev;