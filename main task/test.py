import sqlite3
import pandas as pd
conn = sqlite3.connect('twitter4.db')
c = conn.cursor()
df = pd.read_sql("SELECT * FROM  world_trend_data", conn)
out = df.to_json(orient='records')[1:-1].replace('},{', '} {')
print(out)