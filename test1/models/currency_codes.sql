{{ config(materialized='table') }}
with currency_codes as (
    select distinct currency, code from dbt.s1_currency_codes where code is not null and code <> ''
)
select * from currency_codes