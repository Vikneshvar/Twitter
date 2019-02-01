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

if (not api):
    print ('Problem connecting to API')

for status in tweepy.Cursor(api.home_timeline).items(1):
    print(status._json)

# from geopy import geocoders
from geopy.geocoders import Nominatim
from geopy.exc import GeopyError

# geolocator = Nominatim(user_agent='myapplication')
geolocator = Nominatim()
location = geolocator.geocode("California")
if location:
    latitude = location.latitude
    longitude = location.longitude
    print('\nLatitude =', latitude)
    print('\nLongitude =', longitude)
    TrendingClosest = api.trends_closest(latitude,longitude)
    print('\nTrendingClosest = ', TrendingClosest)
    woeid = [dic['woeid'] for dic in TrendingClosest]
    woeid1 = ''.join(map(str,woeid))
    print ('\nWOEID =', woeid1)

    trending = api.trends_place(woeid1)
    print('\nTRENDING in WOEID')
    print(trending)
    # for trending in api.trends_place(woeid1):
    #     for trend in trending['trends']:
    #         print('%s' % trend['name'])
    hashtags = [x['name'] for x in trending[0]['trends'] if x['name']]
    # hashtags = [x['name'] for x in trending[0]['trends'] if x['name'].startswith('#')]
    hashtags1 = '\n'.join(map(str,hashtags))
    print('\nHashTags:\n', hashtags1)

