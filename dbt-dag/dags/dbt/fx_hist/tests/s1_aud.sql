with aud_hist as (
    select coalesce(date, '1970-01-01') as fx_date from {{ ref('s1_aud1980') }} UNION ALL
    select coalesce(date, '1970-01-01') as fx_date from {{ ref('s1_aud1990') }} UNION ALL
    select coalesce(date, '1970-01-01') as fx_date from {{ ref('s1_aud2000') }} UNION ALL
    select coalesce(date, '1970-01-01') as fx_date from {{ ref('s1_aud2010') }} UNION ALL
    select coalesce(date, '1970-01-01') as fx_date from {{ ref('s1_aud2020') }} 
)
select fx_date from aud_hist group by fx_date having count(fx_date) > 1