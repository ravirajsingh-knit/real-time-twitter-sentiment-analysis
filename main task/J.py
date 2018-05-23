import sqlite3
import pandas as pd
conn = sqlite3.connect('twitter1.db')
c = conn.cursor()
df = pd.read_sql("SELECT * FROM trend_data", conn)
print(df[0:])