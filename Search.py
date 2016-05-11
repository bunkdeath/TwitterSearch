#!/usr/bin/env python

__author__ = "bunkdeath"
__date__ = "$Mar 10, 2012 8:05:18 AM$"

import tweepy
import config as setting
from Parser import TweetParser


class TwitterSearch(object):
    def __init__(self, keyword=None, count=10):
        self.keyword = keyword
        self.count = count

        self.auth = tweepy.OAuthHandler(setting.CONSUMER_KEY, setting.CONSUMER_SECRET)
        self.auth.secure = True
        self.auth.set_access_token(setting.ACCESS_TOKEN, setting.ACCESS_TOKEN_SECRET)
        self.api = tweepy.API(self.auth)

        self.parser = TweetParser()

    def search(self, keyword, count=10):
        if not self.keyword:
            self.keyword = keyword

        if count != 10:
            self.count = count

        tweets = self.api.search(self.keyword, count=self.count)
        return self.parser.parse_class(tweets)
