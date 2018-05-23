from tweepy import Stream
from time import monotonic as timer 
from tweepy import OAuthHandler
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from tweepy.streaming import StreamListener
import json
import time
import sqlite3
from unidecode import unidecode

analyzer = SentimentIntensityAnalyzer()

#consumer key, consumer secret, access token, access secret.
ckey='IXiuKwDcHceu0V6rJZs5eTCqb'
csecret='bQ7iPFlfJpXQYAmd1h3uega7LGRkKYAzyuoeRq7bEzzzzPwcZa'
atoken='904991952982089728-caW2ZirsvpWyjWBbnJeFE1DEO4bmIEf'
asecret='Xxpd9ko6LZ7OxhT5RIopUfI5bvzgATpykkeJ7hlao5VNh'

conn = sqlite3.connect('twitter_mod5.db')
c = conn.cursor()

class listener(StreamListener):
    def on_data(self, data):
        try:
            data = json.loads(data)
            tweet = unidecode(data['text'])
            vs = analyzer.polarity_scores(tweet)
            sentiment = vs['compound']
            time_ms = data['timestamp_ms']
            print(tweet,sentiment)
            c.execute("INSERT INTO tweets (unix, tweet, sentiment) VALUES (?, ?, ?)",
                  (time_ms, tweet, sentiment))
            conn.commit()
        except KeyError as e:
            print(str(e))
        return(True)

    def on_error(self, status):
        print(status)

c.execute("DROP TABLE IF EXISTS tweets")
c.execute("CREATE TABLE IF NOT EXISTS tweets(unix REAL, tweet TEXT, sentiment REAL)")
c.execute("CREATE INDEX fast_unix ON tweets(unix)")
c.execute("CREATE INDEX fast_tweet ON tweets(tweet)")
c.execute("CREATE INDEX fast_sentiment ON tweets(sentiment)")
conn.commit()
while True:
    try:
        auth = OAuthHandler(ckey, csecret)
        auth.set_access_token(atoken, asecret)
        twitterStream = Stream(auth, listener())
        twitterStream.filter(track=['.',',','#','?','_','"'],languages=['en'],locations=[68.116667 ,8.066667, 97.416667,37.100000,])
    except Exception as e:
        print(str(e))
        time.sleep(5)