select * 
from 
    fx.s1_req_collections
where 
    (code is null or code = '')
    AND
    (codes is null or codes = '' or json_array_length(codes::json->'currency')=0 or (codes::json->'currency') is null)