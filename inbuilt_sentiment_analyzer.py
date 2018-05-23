import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

from tweepy import Stream 
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
ckey='MRblXfNQmvHssuz5zLydkUjuP'
csecret='RE2htDqLQfXMu44abXXCC5chWYBfHpkGmnvSsCfKxDdpJeAdX0'
atoken='904991952982089728-r5SKV7WnHmjtNamHkb1ATTBoW7uRq3A'
asecret='A4ZI6AHJzZzACtg6WZvrkMQdL9YtR9vQdbUOHW3xap7jh'

#sid=SentimentIntensityAnalyzer()
class listener(StreamListener):
    def on_data(self,data):
        all_data=json.load(data)
        tweet=all_data["text"]
        print(tweet)
 #       ss=sid.polarity_score(tweet)
 #       for k in ss:
  #          print('{0}:{1},'.format(k,ss[k]),end='')
  #      print(" ")
        return True
    
    def on_error(self,status):
        print(status)

auth=OAuthHandler(ckey,csecret)
auth.set_access_token(atoken,asecret)
twitterStream=Stream(auth,listener())
twitterStream.filter(track=["car"])
