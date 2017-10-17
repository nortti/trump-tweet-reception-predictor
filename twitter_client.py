#!/usr/bin/env python
import os
import sys
import json
import urllib
from requests_oauthlib import OAuth1Session

def download_tweets_json(screen_name):
    client_key = os.environ['client_key']
    client_secret = os.environ['client_secret']

    twitter = OAuth1Session(client_key, client_secret)

    base_url = 'https://api.twitter.com/1.1/statuses/user_timeline.json?'
    params = {'screen_name': screen_name,
              'count': 200,              # TODO: get 3400 tweets by traversing timeline
              'exclude_replies': True,   # Don't need replies
              'include_rts': False}      # Don't want retweets

    url = base_url + urllib.parse.urlencode(params)
    json_data = json.dumps(twitter.get(url).json())

    json_file = open('json_data/' + screen_name + '.json', 'w')
    json_file.write(json_data)
    json_file.close()

if len(sys.argv) is 1:
    print('Missing argument')
else:
    download_tweets_json(sys.argv[1])
