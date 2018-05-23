import sqlite3
import pandas as pd
import csv
conn = sqlite3.connect('twitter.db')
c = conn.cursor()

def create_table():
	try:
		c.execute("DROP TABLE IF EXISTS sentiment_data")
		c.execute("CREATE TABLE IF NOT EXISTS sentiment_data(id INT,name TEXT,pos INT,neu INT,neg INT)")
		i=1
		df = pd.read_sql("SELECT name FROM prime_data", conn)
		#print(df.name[3])
		for x in list(df.name):
		#	print(x)
			if i!=0:
				c.execute("INSERT INTO sentiment_data (id, name, pos, neu, neg) VALUES (?, ?, ?, ?, ?)",
                	 (i,x, 0,0,0))
			i=i+1
		df = pd.read_sql("SELECT * FROM sentiment_data", conn)
		print(df[0:])	
		conn.commit()
	except Exception as e:
		print(str(e))
create_table()
