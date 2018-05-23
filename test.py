import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from tweepy import Stream 
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import twitter
from datetime import *
ckey='MRblXfNQmvHssuz5zLydkUjuP'
csecret='RE2htDqLQfXMu44abXXCC5chWYBfHpkGmnvSsCfKxDdpJeAdX0'
atoken='904991952982089728-r5SKV7WnHmjtNamHkb1ATTBoW7uRq3A'
asecret='A4ZI6AHJzZzACtg6WZvrkMQdL9YtR9vQdbUOHW3xap7jh'

sid=SentimentIntensityAnalyzer()
pop=1000
time1=""
time2=""
class listener(StreamListener):
    def on_data(self,data):
        global pop
        global time1
        global time2
        time0=""
        #all_data=json.load(data)
        #tweet=all_data["text"]

        #tweet=data.split(',"text":"')[1].split('","source')[0]
        #tweet=all_data["text"]
        print(pop)
        time0=data.split('"created_at":"')[1].split('","id":')[0]
        time0=datetime.strptime(time0,'%a %b %d %H:%M:%S +0000 %Y')    
        if pop==1000:
            time2=time0
            time1=time0
        if time0>time2:
        	time2=time0
        if time0<time1:
        	time1=time0
        print("the timestamp")
        print(time1)
        pop-=1
        if pop==-1:
        	delta=time2-time1
        	time=24*delta.days+delta.seconds/(60*60)
        	print((1/time)*24)
        if pop>=0:	
        	return True
        else:
        	pop=1000
        	return False

    def on_error(self,status):
        return False  

oauth=OAuthHandler(ckey,csecret)
oauth.set_access_token(atoken,asecret)
twitterStream=Stream(oauth,listener())

api=twitter.Api(ckey,csecret,atoken,asecret)
details=api.GetTrendsWoeid(woeid=23424848)
#print(details)
for x in details:
    print(x)
    twitterStream.filter(track=[x.name])
