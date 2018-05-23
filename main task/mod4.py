from tweepy import Stream
from time import monotonic as timer 
from tweepy import OAuthHandler
import tweepy
import time
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from tweepy.streaming import StreamListener
import json
import sqlite3
import pandas as pd
from unidecode import unidecode
analyzer = SentimentIntensityAnalyzer()
conn = sqlite3.connect('twitter4.db')
c = conn.cursor()
ckey='IXiuKwDcHceu0V6rJZs5eTCqb'
csecret='bQ7iPFlfJpXQYAmd1h3uega7LGRkKYAzyuoeRq7bEzzzzPwcZa'
atoken='904991952982089728-caW2ZirsvpWyjWBbnJeFE1DEO4bmIEf'
asecret='Xxpd9ko6LZ7OxhT5RIopUfI5bvzgATpykkeJ7hlao5VNh'

#from twitterapistuff import  *
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
try:
    c.execute("DROP TABLE IF EXISTS world_trend_data")
    c.execute("CREATE TABLE IF NOT EXISTS world_trend_data(id INT,name TEXT,country TEXT,woeid INT)")
    #f=open('data.txt','w')
    api = tweepy.API(auth)
    #locationid = 23424848 
    datas=api.trends_available()
    print("hello")
    i=1
    for data in datas:
        c.execute("INSERT INTO world_trend_data(id, name, country, woeid) VALUES (?, ?, ?, ?)",
                            (i,data['name'],data['country'],data['woeid']))
        i=i+1

    conn.commit()
    print("visulizing data for db")
    df = pd.read_sql("SELECT * FROM  world_trend_data", conn)
    out = df.to_json(orient='records')[1:-1].replace('},{', '} {')
    print(out)
    i=1
    for data in datas:
        #print(data)
        #name.append(data['name'])
        #country.append(data['country'])
        #woeid.append(data['woeid'])
        print(data['name'])
        print("checkpoint 1")
        #c.execute("INSERT INTO world_trend_data (id, name, country, woeid) VALUES (?, ?, ?, ?)",
        #                    (i,data['name'],data['country'],data['woeid']))
        if i>20:
            i=1
            api = tweepy.API(auth)

        print("checkpoint 2")
        name=data['name'].lower()
        temp=""
        for x in name:
            if x=="(" or x==")" or x=="." or x=="'" or x=="#":
                continue
            elif x==" " or x=="-" :
                temp+="_"
            else:
                temp+=x
        name=temp
        print(name)
        c.execute("CREATE TABLE IF NOT EXISTS "+name+"_"+str(data['woeid'])+"(name TEXT,query TEXT,url TEXT,tweet_volume INT)")
        print("checkpoint 3")
        trends=api.trends_place(data['woeid'])[0]
        print(i)

        trends=trends["trends"]
        for trend in trends:
            print(trend['name'],trend['query'],trend['tweet_volume'])
            c.execute("INSERT INTO "+name+"_"+str(data['woeid'])+"( name, query,url,tweet_volume) VALUES (?, ?, ?)",
                            (trend['name'],trend['query'],trend['url'],trend['tweet_volume']))
        conn.commit()
        time.sleep(20)
        i=i+1
    c.close()
except Exception as e:
    print(str(e))
    c.close()
    #time.sleep(50)
