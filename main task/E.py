import sqlite3
import pandas as pd
import csv
conn = sqlite3.connect('twitter.db')
c = conn.cursor()

def create_table():
	try:
		c.execute("DROP TABLE IF EXISTS prime_data")
		c.execute("CREATE TABLE IF NOT EXISTS prime_data(id INT,name TEXT,category TEXT,twitter_search TEXT,wikipedia_search TEXT,image_file TEXT)")
		i=0
		with open('A.csv','r',encoding='') as f:
			r=csv.reader(f)
			print(list(r))
			#p=list(r)
			for p in list(r):
				if i!=0:
					c.execute("INSERT INTO prime_data (id, name, category, twitter_search, wikipedia_search, image_file) VALUES (?, ?, ?, ?, ?, ?)",
                  (i, p[0], p[1],p[2],p[3],p[4]))
				i=i+1
		
		df = pd.read_sql("SELECT * FROM prime_data", conn)
		print(df[0:])
		conn.commit()
	except Exception as e:
		print(str(e))
create_table()
