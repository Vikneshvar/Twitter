import pandas as pd
import numpy as np
import json 
import re



def textClen(tweets_list):
    print("In cleaning")

    tweets_clean = []
    # Remove all non-alpha characters except period, @, #, blank space
    regex1 = re.compile('[^a-zA-Z.@# ]')
    # Remove string staring with "@" 
    regex2 = re.compile(r'\@.*? ')
    # Remove string staring with https and ending at the end of the string
    regex3 = re.compile(r'http.*?$')
    # Remove "RT" at the beginning of the string
    regex4 = re.compile(r'^RT')
    for each_tweet in tweets_list:      
        each_tweet = regex1.sub('',each_tweet)
        each_tweet = regex2.sub('',each_tweet)
        each_tweet = regex3.sub('',each_tweet)
        each_tweet = regex4.sub('',each_tweet)
        tweets_clean.append(each_tweet)
    
    for a in tweets_clean:
        print("\n-->",a)

#open the json file and take the "text"
tweets_list = []
with open("C:/Users/vikneshvar.chandraha/Dev/Twitter_dataset/output.json") as f:
    json_object = json.load(f)
    tweets_object = json_object["tweets"]
    print(json_object["tweets"][0]["tweetInfo"][0]["text"])
    for each_hashtag in tweets_object[0:1]:
        print("hashtag: ", each_hashtag["hashtag"])
        for each_tweet in each_hashtag["tweetInfo"]:
            print("\n",each_tweet["text"])
            tweets_list.append(each_tweet["text"])

    print(len(tweets_list))
    # print(tweets_list)

textClen(tweets_list)
    # for each in json_object:
    #     tweet_list = each["text"]
    #     print(tweet_list)



