# Import the necessary package to process data in JSON format
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

for status in tweepy.Cursor(api.home_timeline).items(1):
    print(status._json)

# from geopy import geocoders
from geopy.geocoders import Nominatim
from geopy.exc import GeopyError

# geolocator = Nominatim(user_agent='myapplication')
geolocator = Nominatim()
location = geolocator.geocode('California')
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
    frameList = []
    for l in hashtags:
        if l.startswith('#'):
            frameList.append(l)
        else:
            frameList.append('\"' + l + '\"')
    print('\nFrameList :',frameList)

    searchQuery1 = ' OR '.join(str(li) for li in frameList)
    print('\nSearchQuery1 :', searchQuery1)

    placeID = api.reverse_geocode(latitude,longitude);
    print('\nID:', placeID)

    places = api.geo_search(query="California", granularity="city")
    place_id = places[0].id
    print('\nplace:', place_id)

    # searchQuery = '\''+ 'place:' + place_id +  ' ' +  searchQuery1 + '\''
    # print('\nSearchQuery:', searchQuery)

    searchQuery = 'place:fbd6d2f5a4e4a15e #SuperBowl OR #fresno OR #california OR #LakeShow OR "fresno state" OR "Dutch" OR "Lakers" OR "AirPods" OR #AllStars4 OR "Malik Beasley" OR "Manila" OR "Russian Doll" OR "Naomi Smalls" OR "The Nuggets" OR "Torrey Craig" OR "All Stars" OR "Huntington Park" OR "Governor Northam" OR "Latrice" OR "Free Blueface" OR "Woj and Shams" OR "The Boyz" OR "Maher" OR "horror noire" OR "Natasha Lyonne" OR #Home4thWin OR #LoveAfterLockup OR #ThankYouJin OR #MyPersonalActionFigure OR #teammystic OR #teaminstinct'
    # searchQuery = 'place:fbd6d2f5a4e4a15e #Northam OR #pursuit OR #RalphNortham OR #BasicMoviesOrShows OR #FineWomenWhoWatchWrestling OR #ImWillingToBet OR #DragRace OR #RhymingEulogy OR #ACEeddies OR #SiempreBruja OR #BlueBloods OR #RPDR OR #YouCanGetItIf OR #FridayNight OR #ResignRalph OR #rupaulsdragraceallstars4 OR #ExtremeLove OR #SaturdayThoughts OR #Dateline OR #SaturdayMotivation OR #teammystic OR #teaminstinct'
    searchQuery2 = 'place:96683cc9126741d1 #teammystic OR #teaminstinct OR #teamvalor OR #teamblue OR #teamyellow OR #teamred OR #mystic OR #valor OR #instinct OR "team mystic" OR "team valor" OR "team instinct" OR  OR "Russian Doll" OR "Naomi Smalls" OR "The Nuggets" OR "Torrey Craig" OR "All Stars" OR "Huntington Park" OR "Governor Northam" OR "Latrice" OR "Free Blueface" OR "Woj and Shams" OR "The Boyz" OR "Maher" OR "horror noire" OR "Natasha Lyonne" OR #Home4thWin OR #LoveAfterLockup OR #ThankYouJin OR "HI" OR #Yes'
    print("\nsrchqry2",searchQuery2)  
    import jsonpickle
    maxTweets = 2
    tweetsPerQry = 100 #The twitter Search API allows up to 100 tweets per query
    tweetCount = 0
  
    with open('output.json', 'w') as f:
        for tweet in tweepy.Cursor(api.search,q=searchQuery, count=50, result_type='popular').items(maxTweets):  
            # print("tweet",tweet.encode("utf-8"))
            if tweet.place is not None: 
                f.write(jsonpickle.encode(tweet._json, unpicklable=False) + '\n')
                tweetCount += 1
            
    print('\nDownloaded {0} tweets'.format(tweetCount))
else:
    latitude = None
    longitude = None