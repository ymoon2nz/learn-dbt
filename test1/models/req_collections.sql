{{ config(materialized='table') }}
with req_collections as (
    select req_type, frequency, code, codes::json from dbt.s1_req_collections
)
select * from req_collections