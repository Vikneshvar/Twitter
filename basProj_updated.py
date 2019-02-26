import json
import tweepy
import simplejson as json
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
from geopy.exc import GeopyError
import jsonpickle
import re

with open("C:/Users/vikneshvar.chandraha/Dev/Twitter/keys.json") as f:
    data=json.load(f)

consumer_key = data["consumer_key"]
consumer_secret = data["consumer_secret"]
access_token = data["access_token"]
access_token_seceret = data["access_token_seceret"]

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_seceret)
print('\nConnected to Twitter')

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True);

if (not api):
    print ('\nERROR: Problem connecting to API')

geolocator = Nominatim(user_agent="my-application")

def do_geocode(address):
    try:
        return geolocator.geocode(address)
    except GeocoderTimedOut:
        return do_geocode(address)
    except GeopyError:
        return None


#city_state_country = ""+ each["city"]+", "+each["state"]+", "+each["country"]
city_state_country = "Fullerton, California, USA"
location = do_geocode(city_state_country)

if location:
    latitude = location.latitude
    longitude = location.longitude
    # print('\nLatitude =', latitude)
    # print('\nLongitude =', longitude)
    gcode = ""+str(latitude)+","+str(longitude)+",10mi"
    # print("gcode: ",gcode)

    TrendingClosest = api.trends_closest(latitude,longitude)
    # print('\nTrendingClosest = ', TrendingClosest)
    woeid = [dic['woeid'] for dic in TrendingClosest]
    woeid1 = ''.join(map(str,woeid))
    # print ('\nWOEID =', woeid1)

    trending = api.trends_place(woeid1)
    if len(trending) != 0:
        hashtags = [x['name'] for x in trending[0]['trends']]
        # hashtags = [x['name'] for x in trending[0]['trends'] if x['name'].startswith('#')]
        if len(hashtags) != 0:
            # placeID = api.reverse_geocode(latitude,longitude)
            # print('\nID:', placeID)

            placeResponce = api.reverse_geocode(latitude,longitude);
            placeResponce = str(placeResponce)
            print('\nplaceResponce:', placeResponce)
            matchObj = re.findall(r"id='(\w+)'",placeResponce)
            place_id = matchObj[0]
            print('place_id', place_id)


            frameList = []
            for l in hashtags:
                if l.startswith('#'):
                    frameList.append('\"'+l+'\"')
                else:
                    frameList.append('\"' + l + '\"')
            print('\nFrameList :',frameList)
            listSize = len(frameList)
            print('\n', listSize)
            tweetCount = 0
            hashtagCount = 0
            with open('output.json', 'w') as f:
                json_str = '{"tweets":['
                f.write(json_str)
                for li in frameList:
                    hashtag = str(li)
                    print('\n hashtag:', hashtag)
                    hashtag_str = '{"hashtag":'+hashtag+',"tweetInfo":['
                    f.write(hashtag_str)
                    for tweet in tweepy.Cursor(api.search,q = hashtag, geocode = gcode, count=100, result_type="recent",
                                                lang = "en").items(2):  
                        f.write(jsonpickle.encode(tweet._json, unpicklable=False) + ',')
                        tweetCount += 1
                    hashtagCount+=1
                    if hashtagCount == len(frameList):
                        f.write("]}\n")
                    else:
                        f.write("]},\n")
                f.write(']}')

            with open('output.json', 'r') as f:
                data = f.read().replace("e}},]}","e}}]}")
                print("\ndata ", data)

            with open('output.json', 'w') as f:
                f.write(data)
    
            print('\nDownloaded {0} tweets'.format(tweetCount))
        else:
            print('\nNo Trending Hashtags!')
    else:
        print('\nNo Trending places!')

else:
    latitude = None
    longitude = None

"""
# Driver code 
if __name__ == '__main__': 
  
    # Here goes the twitter handle for the user 
    # whose tweets are to be extracted. 
    get_tweets("twitter-handle")

"""