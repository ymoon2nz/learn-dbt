select 
    fx_date, 1 as nzd, krw,
    MIN(krw) OVER (
    	ORDER BY fx_date 
    	ROWS BETWEEN 30 PRECEDING AND current ROW) 
        as last_30_min,
    MAX(krw) OVER (
    	ORDER BY fx_date 
    	ROWS BETWEEN 30 PRECEDING AND current ROW) 
        as last_30_max,
    MIN(krw) OVER (
    	ORDER BY fx_date 
    	ROWS BETWEEN 60 PRECEDING AND current ROW) 
        as last_60_min,
    MAX(krw) OVER (
    	ORDER BY fx_date 
    	ROWS BETWEEN 60 PRECEDING AND current ROW) 
        as last_60_max,
    MIN(krw) OVER (
    	ORDER BY fx_date 
    	ROWS BETWEEN 90 PRECEDING AND current ROW) 
        as last_90_min,
    MAX(krw) OVER (
    	ORDER BY fx_date 
    	ROWS BETWEEN 90 PRECEDING AND current ROW) 
        as last_90_max,
    AVG(krw) OVER (
    	ORDER BY fx_date 
    	ROWS BETWEEN 30 PRECEDING AND current ROW) 
        as last_30_avg,
    AVG(krw) OVER (
    	ORDER BY fx_date 
    	ROWS BETWEEN 60 PRECEDING AND current ROW) 
        as last_60_avg,
    AVG(krw) OVER (
    	ORDER BY fx_date 
    	ROWS BETWEEN 180 PRECEDING AND current ROW) 
        as last_180_avg,
    AVG(krw) OVER (
    	ORDER BY fx_date 
    	ROWS BETWEEN 360 PRECEDING AND current ROW) 
        as last_360_avg
from {{ ref('stg_history_nzd2krw') }}