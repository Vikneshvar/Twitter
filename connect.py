# Import the tweepy library and json
import tweepy
import simplejson as json

with open("/Users/vik_work/Desktop/Workspace/Twitter/keys.json") as f:
    data=json.load(f)

consumer_key = data["consumer_key"]
consumer_secret = data["consumer_secret"]

access_token = data["access_token"]
access_token_seceret = data["access_token_seceret"]


print(consumer_key)
print(consumer_secret)
print(access_token)
print(access_token_seceret)

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_seceret)

# Create the api to connect to twitter with your creadentials
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True);

for status in tweepy.Cursor(api.home_timeline).items(200):
	print(status._json)

