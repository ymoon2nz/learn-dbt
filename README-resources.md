* Ref: https://medium.com/orchestras-data-release-pipeline-blog/installing-and-configuring-apache-airflow-a-step-by-step-guide-5ff602c47a36

* Create Airflow Admin
```
airflow users  create --role Admin --username admin --email admin --firstname admin --lastname admin --password admin
```

* Bulk Stock Data: http://finance.jasonstrimpel.com/bulk-stock-download/

* [stock-us]
``` sql
-- Date,AAPL,FB,GOOG,JPM,NVDA,^GSPC
CREATE TABLE stock_us (
    id SERIAL,
    Date DATE,
    AAPL NUMERIC(12,2) ,
    FB NUMERIC(12,2) ,
    GOOG NUMERIC(12,2) ,
    JPM NUMERIC(12,2) ,
    NVDA NUMERIC(12,2) ,
    "^GSPC" NUMERIC(12,2),
    UPDATED timestamp DEFAULT CURRENT_TIMESTAMP
);
```