from sqlalchemy import create_engine
import streamlit as st
import pandas as pd

# Initialize connection.
conn = st.connection("postgresql", type="sql")
print(conn)
# Perform query.
#df = conn.query("SELECT TO_CHAR(fx_date, 'dd/mm/yyyy') as fx_date, usd FROM fx.analysis_aud order by fx_date", ttl="10m")
#df = conn.query("SELECT fx_date, usd FROM fx.analysis_aud order by fx_date", ttl="10m")
df = conn.query("SELECT fx_date, usd, last_60_max, last_60_min, last_180_avg FROM \
    fx.last_trend_aud where 10 > DATE_PART('year', NOW()) - DATE_PART('year', fx_date) order by fx_date;", ttl="10m")
#SQL_Query = pd.read_sql_query('SELECT fx_date, usd, last_30_max, last_30_min FROM fx.analysis_aud', conn)

## Print results.
#for row in df.itertuples():
#    st.write(f"{row.fx_date} has a :{row.usd}:")
st.write("FX - AUD Chart")

df = df.set_index('fx_date')
st.line_chart(df)