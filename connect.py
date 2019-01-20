# Import the necessary package to process data in JSON format
try:
    import json
except ImportError:
    import simplejson as json

# Import the tweepy library
import tweepy

consumer_key = "J5PXQdndY5uYURoH6HKjQVquO"
consumer_secret = "XDprvdQhMIQu9VuhvTU0NEjCJMU9TouQ52vlStsY2gCkSdV5Yy"

access_token = "1028861674516705281-N5Smpi61z57bExUy0ymDdUJVHURAAo"
access_token_seceret = "mcDZYyeoHub83TxlVjFGS1FDRtLjypQ0TS08g1zsj9qhc"


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_seceret)

# Create the api to connect to twitter with your creadentials
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True);

for status in tweepy.Cursor(api.home_timeline).items(200):
	print(status._json)

