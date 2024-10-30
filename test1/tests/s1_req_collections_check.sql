select frequency, codes, count(*) from (
    select req_type, frequency, code, codes, codes::json as codes_json from dbt.s1_req_collections where req_type = 'set'
) group by frequency, codes having count(*) > 1
UNION ALL
select frequency, code, count(*) from dbt.s1_req_collections where req_type = 'currency'
    group by frequency, code having count(*) > 1