import tweepy
from tweepy import OAuthHandler
import json
import twitter
from datetime import *
ckey='IXiuKwDcHceu0V6rJZs5eTCqb'
csecret='bQ7iPFlfJpXQYAmd1h3uega7LGRkKYAzyuoeRq7bEzzzzPwcZa'
atoken='904991952982089728-caW2ZirsvpWyjWBbnJeFE1DEO4bmIEf'
asecret='Xxpd9ko6LZ7OxhT5RIopUfI5bvzgATpykkeJ7hlao5VNh'



auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

api = tweepy.API(auth)

locationid = 23424848 
data=api.trends_place(locationid)
print(data)

#print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
#trendqueries = [trend['query'] for trend in api.trends_place(locationid)[0]['trends']]

# for trendquery in trendqueries:
#     print(api.search(q=trendquery))
#     print("\n\n\n\n\n\n\n\n\n")




