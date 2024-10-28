{{ config(materialized='table') }}
with hist_aapl as (
    select date, goog as price from dbt.stock_us
)
select * from hist_aapl