#! /usr/bin/python

__author__ = "bunkdeath"
__date__ = "$Dec 16, 2014 8:52:18 PM$"

# fill this entry from your twitter app
# you can find keys to your application from https://apps.twitter.com/
# select application you like to use or create one

CONSUMER_KEY = ""
CONSUMER_SECRET = ""

ACCESS_TOKEN = ""
ACCESS_TOKEN_SECRET = ""

# ignore this, this is to import my personal setting (not to disclose publicly)

try:
    from config_local import *
except Exception:
    pass
