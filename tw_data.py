import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from tweepy import Stream 
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import datetime






ckey='MRblXfNQmvHssuz5zLydkUjuP'
csecret='RE2htDqLQfXMu44abXXCC5chWYBfHpkGmnvSsCfKxDdpJeAdX0'
atoken='904991952982089728-0KVycVAdw98H9kKyDi4gqVfSXwcBti3'
asecret='9fy4vZ22bugeDlNkSGG5dd056vG5tqRwiXdtK56306QeT'
pos=0
neg=0
neu=0
sid=SentimentIntensityAnalyzer()
class listener(StreamListener):
    def on_data(self,data):
        global pos
        global neg
        global neu
        #all_data=json.load(data)
        #tweet=all_data["text"]
        tweet=data.split(',"text":"')[1].split('","source')[0]
        #tweet=all_data["text"]
        print(tweet)
        #con=open("data.txt","r")
        #s=con.read()
        #con.close();
        #print(s)
        #s=s.split(" ")
        #pos=int(s[0])
        #neg=int(s[1])
        #neu=int(s[2])
        ss=sid.polarity_scores(tweet)
        if ss['compound']>0:
            pos+=1
        elif ss['compound']==0:
            neu+=1
        else:
            neg+=1
        con=open("samplefile.txt","a")
        now = datetime.datetime.now()
        con.write(str(now)+','+str(pos*.1+neu*0.01-neg*0.1)+"\n")
        con.close()
        con=open("data.txt","w")
        con.write(str(pos)+" "+str(neg)+" "+str(neu)+"\n")
        con.close()
        return True

    def on_error(self,status):
        print(status)
pointer=open("data.txt","w")
pointer.write("0 0 0\n")
pointer.close()
oauth=OAuthHandler(ckey,csecret)
oauth.set_access_token(atoken,asecret)
twitterStream=Stream(oauth,listener())
twitterStream.filter(track=["rahul gandhi"])
#twitter = Stream(auth=oauth)
#sfo_trends = twitter.trends.place(_id =23424848)
#print(sfo_trends)
