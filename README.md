# Twitter

Step one: we enter a location(town or city or state) name: we use this method (geolocator = Nominatim()) to get the lat,long of that location. We use this lat,long to find the nearest big city for which hashtags are available. some small cities might not have hashtags/woeid.

Step Two: TrendingClosest = api.trends_closest(latitude,longitude) => this method gives the nearest location(for which trending hashtags are available) to the lat, long we supply.

Step three: We find the trending hashtags in that location(using that locations woeid) using this method: trending = api.trends_place(woeid1)

Step Four: We need to get tweets on these hashtags. We have different methods: ->tweepy.Cursor(api.search,q=searchQuery).items(10000): this methods works with search query. search query needs place id and hashtags. How to get place id? -> Two methods: api.reverse_geocode(latitude,longitude) and api.geo_search(query="California", granularity="city") -> api.reverse_geocode(latitude,longitude) is better because it goes with lat,long values and we have tweepy documentation for that. -> so using this method we get the place id. -> Use this place id and trending hashtags(we get from step 3) to get the tweets.

->API.search(q[, lang][, locale][, rpp][, page][, since_id][, geocode][, show_user])
	this method shows all tweets in a particular location. lat, long can directly be given. surrounding radius kilometer can be given
	to take tweets from location within that radius. 
	-> disadvantage is it gives all tweets, but we are looking for trending hashtags only.
