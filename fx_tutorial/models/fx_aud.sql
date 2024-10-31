with fx_aud (
    select "date" as fx_date, usd from s1_aud1980 UNION ALL
    select "date" as fx_date, usd from s1_aud1990 UNION ALL
    select "date" as fx_date, usd from s1_aud2000 UNION ALL
    select "date" as fx_date, usd from s1_aud2010 UNION ALL
    select "date" as fx_date, usd from s1_aud2020 
)
select * from fx_aud