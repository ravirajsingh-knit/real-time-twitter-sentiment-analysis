import sqlite3
import pandas as pd
import csv
conn = sqlite3.connect('twitter.db')
c = conn.cursor()

def create_table():
	try:
		df=pd.read_sql("SELECT name FROM prime_data",conn)
		names=list(df.name)
		for name in names:
			temp=name.lower()
			name=""
			for i in temp:
				if i=="(" or i==")" or i=="." or i=="'" :
					continue
				elif i!=" ":
					name+=i
				else:
					name+="_"
			print(name)
			c.execute("DROP TABLE IF EXISTS "+name)
			c.execute("CREATE TABLE IF NOT EXISTS "+ name+"(unix REAL, sentiment REAL)")
			#c.execute("CREATE INDEX fast_unix ON "+name+"(unix)")
			#c.execute("CREATE INDEX fast_sentiment ON "+name+"(sentiment)")
		conn.commit()
	except Exception as e:
		print(str(e))
create_table()
