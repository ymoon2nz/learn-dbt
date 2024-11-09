with nzd_hist as (
    select date as fx_date, krw, nzd from {{ source('fx_hist', 'aud1980') }} UNION ALL
    select date as fx_date, krw, nzd from {{ source('fx_hist', 'aud1990') }} UNION ALL
    select date as fx_date, krw, nzd from {{ source('fx_hist', 'aud2000') }} UNION ALL
    select date as fx_date, krw, nzd from {{ source('fx_hist', 'aud2010') }} UNION ALL
    select date as fx_date, krw, nzd from {{ source('fx_hist', 'aud2020') }} 
)
select 
    {{ 
        dbt_utils.generate_surrogate_key([
            'fx_date'
        ])
    }} as fx_date_key,
    fx_date, 1*krw/nzd as krw
from nzd_hist