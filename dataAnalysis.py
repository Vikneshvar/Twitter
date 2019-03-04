import pandas as pd
import numpy as np
import json 
import re
from nltk.util import ngrams
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from collections import Counter

def textClen(tweets_list):
    # print("In cleaning")
    ngramList = []
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
        each_tweet = each_tweet.lower()
        processedSentenceList = each_tweet.split('.')

        # Count number of words
        tokenizer = RegexpTokenizer(r'\w+')
        tokens = tokenizer.tokenize(each_tweet)
        dict_output={}
        dict_output['string']=each_tweet
        dict_output['count']=len(tokens)
        print("dict_output",dict_output)

        for sentence in processedSentenceList:
            ng_list = []
            sentence_list = sentence.strip().split(' ')
            ng_list = word_grams(sentence_list)

        for item in ng_list:
            item = item.strip()
            if len(item)>1:
                ngramList.append(item)

    return ngramList


# Create ngrams of one words only - coz we are removing only one words from the text
def word_grams(words, min=1, max=2):
	s = []
	for n in range(min, max):
		for ngram in ngrams(words, n):
			p =' '.join(str(i) for i in ngram)
			s.append(p)
	return s

#open the json file and take the "text"
tweets_list = []
with open("C:/Users/vikneshvar.chandraha/Dev/Twitter_dataset/output_noRe.json") as f:
    json_object = json.load(f)
    tweets_object = json_object["tweets"]
    print(json_object["tweets"][0]["tweetInfo"][0]["text"])
    for each_hashtag in tweets_object[0:1]:
        print("hashtag: ", each_hashtag["hashtag"])
        for each_tweet in each_hashtag["tweetInfo"]:
            print("\n",each_tweet["text"])
            tweets_list.append(each_tweet["text"])

    print("no of tweets:", len(tweets_list))
    # print(tweets_list)

ngramList = textClen(tweets_list)
print("ngramList------>>>>>>",ngramList)

counts = {}
counts = Counter(ngramList).most_common(10)

print("counts------>>>>>>",counts)






