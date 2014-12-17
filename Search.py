#! /usr/bin/python

__author__ = "bunkdeath"
__date__ = "$Mar 10, 2012 8:05:18 AM$"

import tweepy
import config as setting
from Parser import TweetParser

parser = TweetParser()
auth = tweepy.OAuthHandler(setting.CONSUMER_KEY, setting.CONSUMER_SECRET)

auth.secure = True
auth.set_access_token(setting.ACCESS_TOKEN, setting.ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

query = 'tech'
count = 3

# search for 'count' number of tweets containing 'query' value in it
tweets = api.search(query, count=count)

# returns JSON object
response = parser.parse_class(tweets)
# print response

# displaying minimal tweet
for tweet in response:
    print tweet['author']
    print tweet['author_screen_name']
    print tweet['text']
    print
