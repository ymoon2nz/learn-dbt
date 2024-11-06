select 
    fx_date, 1 as nzd, usd,
    MIN(usd) OVER (
    	ORDER BY fx_date 
    	ROWS BETWEEN 30 PRECEDING AND current ROW) 
        as last_30_min,
    MAX(usd) OVER (
    	ORDER BY fx_date 
    	ROWS BETWEEN 30 PRECEDING AND current ROW) 
        as last_30_max,
    MIN(usd) OVER (
    	ORDER BY fx_date 
    	ROWS BETWEEN 60 PRECEDING AND current ROW) 
        as last_60_min,
    MAX(usd) OVER (
    	ORDER BY fx_date 
    	ROWS BETWEEN 60 PRECEDING AND current ROW) 
        as last_60_max,
    MIN(usd) OVER (
    	ORDER BY fx_date 
    	ROWS BETWEEN 90 PRECEDING AND current ROW) 
        as last_90_min,
    MAX(usd) OVER (
    	ORDER BY fx_date 
    	ROWS BETWEEN 90 PRECEDING AND current ROW) 
        as last_90_max,
    MIN(usd) OVER (
    	ORDER BY fx_date 
    	ROWS BETWEEN 180 PRECEDING AND current ROW) 
        as last_180_min,
    MAX(usd) OVER (
    	ORDER BY fx_date 
    	ROWS BETWEEN 360 PRECEDING AND current ROW) 
        as last_180_max,
    MIN(usd) OVER (
    	ORDER BY fx_date 
    	ROWS BETWEEN 360 PRECEDING AND current ROW) 
        as last_360_min,
    MAX(usd) OVER (
    	ORDER BY fx_date 
    	ROWS BETWEEN 360 PRECEDING AND current ROW) 
        as last_360_max,
    AVG(usd) OVER (
    	ORDER BY fx_date 
    	ROWS BETWEEN 30 PRECEDING AND current ROW) 
        as last_30_avg,
    AVG(usd) OVER (
    	ORDER BY fx_date 
    	ROWS BETWEEN 60 PRECEDING AND current ROW) 
        as last_60_avg,
    AVG(usd) OVER (
    	ORDER BY fx_date 
    	ROWS BETWEEN 180 PRECEDING AND current ROW) 
        as last_180_avg,
    AVG(usd) OVER (
    	ORDER BY fx_date 
    	ROWS BETWEEN 360 PRECEDING AND current ROW) 
        as last_360_avg
from {{ source('fx', 'hist_nzd2usd') }}