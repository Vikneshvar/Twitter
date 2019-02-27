import pandas as pd
import numpy as np
import json 

#open the json file and take the "text"
with open("C:/Users/vikneshvar.chandraha/Dev/Twitter/output.json") as f:
    data = json.load(f)
    
    for each in data:
        tweet_list = each["text"]
        print(tweet_list)