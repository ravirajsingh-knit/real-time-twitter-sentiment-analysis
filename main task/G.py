import matplotlib.pyplot as plt
import pandas as pd  
import sqlite3
 # Data to plot
conn = sqlite3.connect('twitter.db')
c = conn.cursor()

labels = 'POSITIVE', 'NEGATIVE', 'NEUTRAL'
df = pd.read_sql("SELECT pos,neg,neu FROM sentiment_data WHERE name="+'"BJP"', conn)
sizes = [int(df.pos),int(df.neg),int(df.neu)]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
#explode = (0.1, 0, 0, 0)  # explode 1st slice
  
  # Plot
plt.pie(sizes, labels=labels, colors=colors,
                  autopct='%1.1f%%', shadow=True, startangle=140)
   
plt.axis('equal')
plt.show()
