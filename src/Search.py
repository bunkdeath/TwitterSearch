#! /usr/bin/python

# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__ = "bunkdeath"
__date__ = "$Mar 10, 2012 8:05:18 AM$"

import httplib
import json
import logging
import socket
import urllib

PATH = "/search.json"
c = httplib.HTTPConnection("search.twitter.com")
params = {'q': 'bunkdeath'}
path = "%s?%s" % (PATH, urllib.urlencode(params))

def parseTweet(tweet):
    try:
        jsonData = json.loads(tweet)
        if 'results' not in jsonData:
            print "no result"
        else:
            for results in jsonData:
                if results == 'results':
                    totalTweetString = json.dumps(jsonData[results])
                    totalTweetJson = json.loads(totalTweetString)

                    for singleTweet in totalTweetJson:
                        signleTweetString = json.dumps(singleTweet)
                        signleTweetJson = json.loads(signleTweetString)
                        for index in signleTweetJson:
                            if index == 'text':
                                print signleTweetJson[index]
                            if index == 'created_at':
                                print signleTweetJson[index]
                            if index == 'geo':
                                print signleTweetJson[index]
                            if index == 'in_reply_to_status_id':
                                print signleTweetJson[index]
                        print "\n"
    except ValueError:
        print "Error in json"
        return

try:
    c.request('GET', path)
    r = c.getresponse()
    data = r.read()
    c.close()
    parseTweet(data)
except (httplib.HTTPException, socket.error, socket.timeout), e:
    logging.error("search() error: %s" % (e))