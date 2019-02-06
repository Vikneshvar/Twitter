import peewee
from models import Location
import simplejson as json
import time
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
from geopy.exc import GeopyError
import tweepy

geolocator = Nominatim(user_agent="my-application")

with open("C:/Users/vikneshvar.chandraha/Dev/Twitter/keys.json") as f:
    data=json.load(f)

consumer_key = data["consumer_key"]
consumer_secret = data["consumer_secret"]
access_token = data["access_token"]
access_token_seceret = data["access_token_seceret"]

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_seceret)

# Create the api to connect to twitter with your creadentials
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True)

def do_geocode(address):
    try:
        return geolocator.geocode(address)
    except GeocoderTimedOut:
        return do_geocode(address)
    except GeopyError:
        return None

with open("C:/Users/vikneshvar.chandraha/Dev/Twitter/usaCities.json") as cities:
    dataObj = json.load(cities)
#    print(dataObj)
    values=[]
    for each in dataObj:
#        print(each["city"])
#        print(each["city"][0].lower())
        if each["city"][0].lower() in ('z'):
            print(each["city"][0].lower())
            print(each["state"])
            print(each["country"])
            city_state_country = ""+ each["city"]+", "+each["state"]+", "+each["country"]
#            city_state_country = "Bangor Trident Base, Washington, USA"
            print(city_state_country)
            location = do_geocode(city_state_country)
            if location is not None:
                TrendingClosest = api.trends_closest(location.latitude,location.longitude)
                print('\nTrendingClosest = ', TrendingClosest)
                
                woeid = [dic['woeid'] for dic in TrendingClosest]
                woeid_value = ''.join(map(str,woeid))
                print ('\nWOEID =', woeid_value)
                
                trendClosest = [dic['name'] for dic in TrendingClosest]
                closest_city = ''.join(map(str,trendClosest))
                print ('\nclosest_city =', closest_city)
                
                latitude = str(location.latitude)
                longitude = str(location.longitude)

                tup = (each["city"],each["state"],each["country"],latitude,longitude,closest_city,woeid_value)
                print('\nLatitude =', latitude)
                print('\nLongitude =', longitude)
            
                values.append(tup)
                print("values ********",values)
                time.sleep(1)
#        break
print("values ********",values)   

Location.insert_many(values,fields=[Location.City, Location.State,Location.Country,Location.Latitude,Location.Longitude,Location.CCity,Location.CCity_WOEID]).execute()
    

    
