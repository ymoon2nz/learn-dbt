-- Create dbt database for dev user
DROP DATABASE fx;
CREATE database fx;
CREATE USER dev WITH PASSWORD 'dbtdev' SUPERUSER;
GRANT ALL PRIVILEGES ON DATABASE fxhist TO postgres;
GRANT ALL PRIVILEGES ON DATABASE fxhist TO dev;