import wikipedia
import sqlite3
import json
import pandas as pd
conn = sqlite3.connect('twitter.db')
c = conn.cursor()
#import matplotlib.image as mpimg
#import numpy as np
#ny=wikipedia.page('Rahul Gandhi')
#print(ny.content.split("\n\n")[0])
#img=mpimg.imread(ny.images[0])
#plt.imshow(img)
def wiki(id):
	df = pd.read_sql("SELECT wikipedia_search,image_file FROM prime_data where id="+str(id), conn)
	#print(list(df.tweeet_search))
	ny=wikipedia.page(list(df.tweeet_search)[0])
	print(ny.content.split("\n\n")[0])
	l=[]
	l.append(ny.content.split("\n\n")[0])
	l.append(list(df.image_file)[0])
	return json.dumps(l)

print(wiki(2))

