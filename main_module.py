import sentiment_module as s

from tweepy import Stream 
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
ckey='MRblXfNQmvHssuz5zLydkUjuP'
csecret='RE2htDqLQfXMu44abXXCC5chWYBfHpkGmnvSsCfKxDdpJeAdX0'
atoken='904991952982089728-r5SKV7WnHmjtNamHkb1ATTBoW7uRq3A'
asecret='A4ZI6AHJzZzACtg6WZvrkMQdL9YtR9vQdbUOHW3xap7jh'


#from twitterapistuff import *

class listener(StreamListener):
    def on_data(self, data):
        all_data = json.loads(data)
        tweet = all_data["text"]
        sentiment_value, confidence = s.sentiment(tweet)
        print(tweet, sentiment_value, confidence)
        if confidence*100 >= 80:
            output = open("twitter-out.txt","a")
            output.write(sentiment_value)
            output.write('\n')
            output.close()
        return True 
    def on_error(self, status):
        print(status)
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)              
twitterStream = Stream(auth, listener())
twitterStream.filter(track=["sachin tendulkar"])
