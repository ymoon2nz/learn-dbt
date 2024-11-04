from sqlalchemy import create_engine
import pandas as pd

# Initialize connection.
uri = f"postgresql+psycopg2://dev:dbtdev@localhost:5432/fx"
alchemyEngine = create_engine(uri)
conn = alchemyEngine.connect()
#conn = st.connection("postgresql", type="sql")
print(conn)
# Perform query.
#df = conn.query('SELECT * FROM fx.analysis_aud limit 10;', ttl="10m")

SQL_Query = pd.read_sql_query('SELECT fx_date, usd, last_30_max, last_30_min FROM fx.analysis_aud', conn)

## Print results.
#for row in df.itertuples():
#    st.write(f"{row.fx_date} has a :{row.usd}:")
df = pd.DataFrame(SQL_Query, columns=['fx_date','usd','last_30_max','last_30_min'])
df = df.set_index('fx_date')
