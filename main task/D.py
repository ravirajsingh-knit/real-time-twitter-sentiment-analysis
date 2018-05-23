from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import sqlite3
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from unidecode import unidecode
import time
import re
import pandas as pd

analyzer = SentimentIntensityAnalyzer()

#consumer key, consumer secret, access token, access secret.
ckey="IXiuKwDcHceu0V6rJZs5eTCqb"
csecret="bQ7iPFlfJpXQYAmd1h3uega7LGRkKYAzyuoeRq7bEzzzzPwcZa"
atoken="904991952982089728-caW2ZirsvpWyjWBbnJeFE1DEO4bmIEf"
asecret="Xxpd9ko6LZ7OxhT5RIopUfI5bvzgATpykkeJ7hlao5VNh"

conn = sqlite3.connect('twitter.db')
c = conn.cursor()
df=pd.read_sql("SELECT name FROM prime_data",conn)
tracker=list(df.name)[0:]
print(tracker)

f=open('test.txt','w')
class listener(StreamListener):
    def on_data(self, data):
        try:
            data = json.loads(data)
            tweet = unidecode(data['text'])
            time_ms = data['timestamp_ms']
            vs = analyzer.polarity_scores(tweet)
            sentiment = vs['compound']
            print(tweet)
            print(sentiment)
            b=False
            for x in tracker:
                name=x
                x=x.lower()
                if x.split(" ")[-1] in tweet.lower().split(" "):
                    f.write(name)
                    f.write("\n")
                    f.write(tweet)
                    f.write("\n\n")
                    if sentiment>=0.5:
                        df = pd.read_sql("SELECT pos FROM sentiment_data WHERE name='"+name+"'", conn)
                        c.execute("UPDATE sentiment_data SET pos="+str(list(df.pos)[0]+1)+" WHERE  name='"+name+"'")
                    elif sentiment<0.5 and sentiment>-0.5:
                        df = pd.read_sql("SELECT neu FROM sentiment_data WHERE name='"+name+"'", conn)
                        c.execute("UPDATE sentiment_data SET neu="+str(list(df.neu)[0]+1)+" WHERE  name='"+name+"'")
                    else:
                        df = pd.read_sql("SELECT neg FROM sentiment_data WHERE name='"+name+"'", conn)
                        c.execute("UPDATE sentiment_data SET neg="+str(list(df.neg)[0]+1)+" WHERE  name='"+name+"'")
                    temp=name.lower()
                    name=""
                    for i in temp:
                        if i=="(" or i==")" or i=="." or i=="'" :
                            continue
                        elif i!=" ":
                            name+=i
                        else:
                            name+="_"
                    #print(time_ms, tweet, sentiment)
                    c.execute("INSERT INTO "+name+" (unix, sentiment) VALUES (?,?)",
                          (time_ms, sentiment))
                    conn.commit()
        except KeyError as e:
            print(str(e))
        return(True)

    def on_error(self, status):
        print(status)


while True:
    try:
        auth = OAuthHandler(ckey, csecret)
        auth.set_access_token(atoken, asecret)
        twitterStream = Stream(auth, listener())
        twitterStream.filter(track=tracker,languages=['en'])
    except Exception as e:
        print(str(e))
        time.sleep(5)
