#! /usr/bin/python

__author__ = "bunkdeath"
__date__ = "$Mar 10, 2012 8:05:18 AM$"


class TweetParser:
    def __init__(self):
        '''This is custom parser to parse object returned from tweetpy lib
        '''

    def parse_class(self, searched_object):
        '''searched_object is response object got from api.search() method of tweetpy
           this method parse this object to required JSON format'''

        tweets = []
        for tweet in searched_object:
            json = {}
            json['author'] = tweet.author.name
            json['author_screen_name'] = tweet.author.screen_name
            json['favorited'] = tweet.favorited
            json['in_reply_to_user_id'] = tweet.in_reply_to_user_id
            json['contributors'] = tweet.contributors
            json['truncated'] = tweet.truncated
            json['source'] = tweet.source
            json['text'] = tweet.text
            json['created_at'] = tweet.created_at.strftime('%B %d, %Y')
            json['retweeted'] = tweet.retweeted
            json['in_reply_to_status_id'] = tweet.in_reply_to_status_id
            json['coordinates'] = tweet.coordinates
            json['id'] = tweet.id
            json['entities'] = tweet.entities
            json['in_reply_to_status_id_str'] = tweet.in_reply_to_status_id_str
            json['place'] = tweet.place
            json['id_str'] = tweet.id_str
            json['in_reply_to_screen_name'] = tweet.in_reply_to_screen_name
            json['retweet_count'] = tweet.retweet_count
            json['geo'] = tweet.geo
            json['in_reply_to_user_id_str'] = tweet.in_reply_to_user_id_str
            json['metadata'] = tweet.metadata

            tweets.append(json)

        return tweets
