import json
import tweepy
import simplejson as json

with open("C:/Users/welcome/Documents/pythonProject/keys.json") as f:
    data=json.load(f)

consumer_key = data["consumer_key"]
consumer_secret = data["consumer_secret"]
access_token = data["access_token"]
access_token_seceret = data["access_token_seceret"]

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_seceret)

print('Connected to Twitter')

# Create the api to connect to twitter with your creadentials
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True);

if (not api):
    print ('Problem connecting to API')

# from geopy import geocoders
from geopy.geocoders import Nominatim
from geopy.exc import GeopyError

myFile = open("C:/Users/welcome/Documents/pythonProject/input.txt", "r")
lines = [line.strip("\n\r") for line in myFile.readlines()]
print(lines)

myDict = {}
for lin in lines:
    geolocator = Nominatim()
    location = geolocator.geocode(lin)
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
        myList = [latitude,longitude,woeid1]
        myDict[lin] = myList
print(myDict)

import csv
with open("C:/Users/welcome/Documents/pythonProject/cityOuput.csv","w") as csvFile:
    csv_File = csv.writer(csvFile)
    csv_File.writerow(['City','Latitude','Longitude','WOEID'])
    for key in sorted(myDict.keys()):
        csv_File.writerow([key] + myDict[key])
   
    
  

        
