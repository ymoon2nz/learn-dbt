{{ config(materialized='table') }}
with tickers_nyse as (
    select "Ticker" as ticker,  "Name" as name from dbt.stock_info where "Exchange" = 'NYSE'
)
select * from tickers_nyse