{{ config(materialized='table') }}
with hist_aapl as (
    select date, nvda as price from dbt.stock_us
)
select *, 
    {{ convert_currency('price', 1.51, 'AUD', 'USD') }} as price_aud
from hist_aapl