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
conn = sqlite3.connect('twitter1.db')
c = conn.cursor()
ckey='IXiuKwDcHceu0V6rJZs5eTCqb'
csecret='bQ7iPFlfJpXQYAmd1h3uega7LGRkKYAzyuoeRq7bEzzzzPwcZa'
atoken='904991952982089728-caW2ZirsvpWyjWBbnJeFE1DEO4bmIEf'
asecret='Xxpd9ko6LZ7OxhT5RIopUfI5bvzgATpykkeJ7hlao5VNh'

#from twitterapistuff import *
f=open('test1.txt','w')
class listener(StreamListener):
    def on_data(self, data):
        global deadline
        try:
            data = json.loads(data)
            tweet = unidecode(data['text'])
            time_ms = data['timestamp_ms']
            vs = analyzer.polarity_scores(tweet)
            sentiment = vs['compound']
            print(tweet)
            print(sentiment)
            
            for x in tracker:
                name=x
                x=x.lower()
                print("Search")
                print(x)
                if x in tweet.lower().split(" "):
                    print("OK")
                    f.write(name)
                    f.write("\n")
                    f.write(tweet)
                    f.write("\n\n")
                    if sentiment>=0.5:
                        df = pd.read_sql("SELECT pos FROM trend_data WHERE name='"+name+"'", conn)
                        c.execute("UPDATE trend_data SET pos="+str(list(df.pos)[0]+1)+" WHERE  name='"+name+"'")
                    elif sentiment<0.5 and sentiment>-0.5:
                        df = pd.read_sql("SELECT neu FROM trend_data WHERE name='"+name+"'", conn)
                        c.execute("UPDATE trend_data SET neu="+str(list(df.neu)[0]+1)+" WHERE  name='"+name+"'")
                    else:
                        df = pd.read_sql("SELECT neg FROM trend_data WHERE name='"+name+"'", conn)
                        c.execute("UPDATE trend_data SET neg="+str(list(df.neg)[0]+1)+" WHERE  name='"+name+"'")
                    temp=name.lower()
                    name=""
                    for x in temp:
                        if x=="(" or x==")" or x=="." or x=="'" or x=="#":
                            continue
                        elif x==" " or x=="-" :
                            name+="_"
                        else:
                            name+=x
                    if name[0] in "0123456789":
                        name="numeric_"+name
                    #print(time_ms, tweet, sentiment)
                    c.execute("INSERT INTO "+name+" (unix, sentiment) VALUES (?,?)",
                          (time_ms, sentiment))
                    conn.commit()
        except KeyError as e:
            print(str(e))
        if timer() >= deadline:
            return False
        return(True)

    def on_error(self, status):
        print(status)


deadline=""
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
while True:
    try:
        
        c.execute("DROP TABLE IF EXISTS trend_data")
        c.execute("CREATE TABLE IF NOT EXISTS trend_data(id INT,name TEXT,pos INT,neu INT,neg INT)")
        c.execute("DROP TABLE IF EXISTS primary_trend_data")
        c.execute("CREATE TABLE IF NOT EXISTS primary_trend_data(id INT,name TEXT,query TEXT,tweet_volume INT)")
        api = tweepy.API(auth)
        locationid = 23424848 
        datas=api.trends_place(locationid)[0]
        datas=datas["trends"]
        #print(datas)
        #datas=datas.split("'trends': [")[1]
        #datas=datas.split("]")[0]
        #print(datas)
        tracker=[]
        i=1
        for data in datas:
            name=data["name"]
            query=data["query"]
            tweet_volume=data["tweet_volume"]
            #print(tweet_volume)
            if name[0]=='#' or tweet_volume!="None":
                c.execute("INSERT INTO primary_trend_data (id, name, query, tweet_volume) VALUES (?, ?, ?, ?)",
                            (i,name,query,tweet_volume))            
                c.execute("INSERT INTO trend_data (id, name, pos, neu, neg) VALUES (?, ?, ?, ?, ?)",
                            (i,name, 0,0,0))
                i=i+1
                tracker.append(name)
                name=name.lower()
                temp=""
                #print(name)
                for x in name:
                    if x=="(" or x==")" or x=="." or x=="'" or x=="#":
                        continue
                    elif x==" " or x=="-" :
                        temp+="_"
                    else:
                        temp+=x
                name=temp
                if name[0] in "0123456789":
                    name="numeric_"+name
               # print(name)
                c.execute("DROP TABLE IF EXISTS "+name)
                c.execute("CREATE TABLE IF NOT EXISTS "+ name+"(unix REAL, sentiment REAL)")
        print(tracker)
        deadline = timer() + 60*60*12
        twitterStream = Stream(auth, listener())
        twitterStream.filter(track=tracker)
        for name in tracker:
            name=name.lower()
            temp=""
            for x in name:
                if x=="(" or x==")" or x=="." or x=="'" or x=="#":
                    continue
                elif x==" " or x=="-":
                    temp+="_"
                else:
                    temp+=x
            name=temp
            if name[0] in "0123456789":
                name="numeric_"+name
            c.execute("DROP TABLE IF EXISTS "+name)
        conn.commit()
    except Exception as e:
        print(str(e))
        time.sleep(5)
