# Import the tweepy library and json
import tweepy
import simplejson as json

with open("C:/Users/vikneshvar.chandraha/Dev/Twitter/keys.json") as f:
    data=json.load(f)

consumer_key = data["consumer_key"]
consumer_secret = data["consumer_secret"]

access_token = data["access_token"]
access_token_seceret = data["access_token_seceret"]

"""
print(consumer_key)
print(consumer_secret)
print(access_token)
print(access_token_seceret)
"""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_seceret)

# Create the api to connect to twitter with your creadentials
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True)

"""
for status in tweepy.Cursor(api.home_timeline).items(200):
	print(status._json)

trends1 = api.trends_place(id=2442047) # from the end of your code
# trends1 is a list with only one element in it, which is a 
# dict which we'll put in data.
data = trends1[0] 
# grab the trends
trends = data['trends']
# grab the name from each trend
names = [trend['name'] for trend in trends]
# put all the names together with a ' ' separating them
trendsName = ' '.join(names)
print(trendsName)


#trends2 = api.trends_available()
#print(trends2)

trends3 = api.trends_closest(42.65258, -73.75623)
print(trends3)

#Getting Geo ID for USA
places = api.geo_search(query="USA", granularity="country")

#Copy USA id
place_id = places[0].id
print('USA id is: ',place_id)

print(api.rate_limit_status()['resources']['search'])

"""

print('Connected to Twitter')

# Create the api to connect to twitter with your creadentials
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True)

if (not api):
    print ('Problem connecting to API')

for status in tweepy.Cursor(api.home_timeline).items(1):
    print(status._json)

# from geopy import geocoders
from geopy.geocoders import Nominatim
from geopy.exc import GeopyError

# geolocator = Nominatim(user_agent='myapplication')
geolocator = Nominatim()
location = geolocator.geocode('Austintown,Ohio')
latitude = location.latitude
longitude = location.longitude
print('\nLatitude =', latitude)
print('\nLongitude =', longitude)


"""

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

    hashtags2 = '" OR "'.join(map(str,hashtags))
    print('\n', hashtags2)

    placeID = api.reverse_geocode(latitude,longitude);
    print('\nID:', placeID)

    places = api.geo_search(query="California", granularity="city")
    place_id = places[0].id
    print('\nplace:', place_id)

    # searchQuery = '\''+ 'place:' + place_id +  ' ' + '\"' + hashtags2 + '\"' + '\''
    # print('\nSearchQuery:', searchQuery)

    searchQuery1 = 'place:fbd6d2f5a4e4a15e #LakeShow OR #fresno OR #California OR "fresno state" OR "Lakers" OR "Super Bowl" OR "Valentines Day" OR '  \
    '#WritingCommunity OR #HereTheyCome OR Lance OR Ben Simmons OR Sixers OR Happy Black History Month OR ' \
    'clippers OR Boban OR Avery Bradley OR Embiid OR Lou Williams OR 2 Chainz OR Hard White OR '  \
    'Inside the NBA OR Landry Shamet OR JJ Redick OR Oracle OR HardWhiteVIDEO OR HappyBirthdayHarryStyles OR #Budget2019 OR ' \
    '#HTGAWM OR #LALvsLAC OR #PHIvsGSW OR #ComplimentAMonster OR #ItsNotUpForDebate OR #HardWhiteMusicVideo OR #NBAonTNT OR '\
    '#7RingsRemix OR #hourlycomicday OR #DosAndDontsOfHaunting OR #TheRapGame OR #Brooklyn99 OR #Medicate OR #criticalrolespoilers OR ' \
    '#TheOrville OR #BudgetForNewIndia OR #HardWhiteOnVEVO OR #30for30 OR #InsideTheNBA OR #howicheermyfriends OR #ClipperNation OR #myhappyplaceiswhere OR #SBMusicFest'
    
    print('\nSearchQuery1:', searchQuery1)


    searchQuery2 = 'place:96683cc9126741d1 #teammystic OR #teaminstinct OR #teamvalor OR' \
              '#teamblue OR #teamyellow OR #teamred OR' \
              '#mystic OR #valor OR #instinct OR' \
              '"team mystic" OR "team valor" OR "team instinct"'

    print('\nSearchQuery2:', searchQuery2)

    # import jsonpickle
    maxTweets = 2
    # tweetsPerQry = 100 #The twitter Search API allows up to 100 tweets per query
    # tweetCount = 0

    # with open('output.json', 'w') as f:
    for tweet in tweepy.Cursor(api.search,q=searchQuery2).items(maxTweets) :     
        print("\ntweet json",tweet)
    #    if tweet.place is not None:
                
            #    f.write(jsonpickle.encode(tweet._json, unpicklable=False) + '\n')
            #    tweetCount += 1
               
     #   print('\nDownloaded {0} tweets'.format(tweetCount))

else:
    latitude = None
    longitude = None

"""