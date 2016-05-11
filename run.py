#!/usr/bin/env python

import json
import argparse
from search import TwitterSearch

parser = argparse.ArgumentParser()


def setup_argparse():
    parser.add_argument('-k', '--keyword', help='search text keyword', required=True)
    parser.add_argument('-l', '--limit', help='number of tweets to retrieve')


def parse_argparse():
    args = parser.parse_args()
    return args.keyword, args.limit


def main(keyword):
    twitter_search = TwitterSearch()
    tweets = twitter_search.search("nadal")
    print json.dumps(tweets, indent=4)


if __name__ == '__main__':
    setup_argparse()
    keyword, limit = parse_argparse()
    main(keyword)
