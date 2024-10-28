select t.date, 
    t.price as aapl,
    t1.price as goog,
    t2.price as nvda
from
    {{ ref('hist_aapl') }} t,
    {{ ref('hist_goog') }} t1,
    {{ ref('hist_nvda') }} t2
where t.date = t1.date and t1.date = t2.date
