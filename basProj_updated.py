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
    gcode = ""+str(latitude)+","+str(longitude)+",50mi"
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
            # print('\nplaceResponce:', placeResponce)
            matchObj = re.findall(r"id='(\w+)'",placeResponce)
            place_id = matchObj[0]
            # print('place_id', place_id)


            frameList = []
            for l in hashtags[0:1]:
                if l.startswith('#'):
                    frameList.append('\"'+l+'\"')
                else:
                    frameList.append('\"' + l + '\"')
            # print('\nFrameList :',frameList)
            listSize = len(frameList)
            # print('\n', listSize)
            tweetCount_all = 0
            tweetCount_noRetweet = 0
            hashtagCount = 0

            # Creating a json file with all tweets for each hashtag
            # json string for all taking all tweets
            json_str_all = '{"tweets":['
            # json string that doesnt take retweeted tweets
            json_str_noRe = '{"tweets":['
            for li in frameList:
                hashtag = str(li)
                print('\n hashtag:', hashtag)
                hashtag_str = '{"hashtag":'+hashtag+',"tweetInfo":['
                json_str_all = json_str_all + hashtag_str
                json_str_noRe = json_str_noRe + hashtag_str

                for tweet in tweepy.Cursor(api.search,q = hashtag, geocode = gcode, count=100, result_type="recent",
                                            lang = "en").items(100):
                    json_encoded = jsonpickle.encode(tweet._json, unpicklable=False)
                    json_object = json.loads(json_encoded)

                    json_str_all = json_str_all + json_encoded + ','
                    tweetCount_all += 1

                    # If "retweeted_status" key is present in the json response, then its a retweet.
                    if "retweeted_status" not in json_object:
                        json_str_noRe = json_str_noRe + json_encoded + ','
                        tweetCount_noRetweet += 1
                    
                
                hashtagCount+=1
                if hashtagCount == len(frameList):
                    json_str_all = json_str_all + "]}\n"
                    json_str_noRe = json_str_noRe + "]}\n"
                else:
                    json_str_all = json_str_all + "]},\n"
                    json_str_noRe = json_str_noRe + "]},\n"
            json_str_all = json_str_all + "]}"
            json_str_noRe = json_str_noRe + "]}"
            
            # Make the json perfect by replacing some commas
            json_str_all = re.sub("e}},]}","e}}]}",json_str_all)
            json_str_noRe = re.sub("e}},]}","e}}]}",json_str_noRe)

            # Write the json string to a output file
            with open("C:/Users/vikneshvar.chandraha/Dev/Twitter_dataset/output_all.json", 'w') as f:
                f.write(json_str_all)

            with open("C:/Users/vikneshvar.chandraha/Dev/Twitter_dataset/output_noRe.json", 'w') as f:
                f.write(json_str_noRe)

            print('\ntweetCount_noRetweet',tweetCount_noRetweet)
            print('\n tweetCount', tweetCount_all)
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