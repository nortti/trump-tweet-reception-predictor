#!/usr/bin/env python
import os
import sys
import json
import urllib
from requests_oauthlib import OAuth1Session


def get_tweets_json(screen_name):
    client_key = os.environ['client_key']
    client_secret = os.environ['client_secret']

    twitter = OAuth1Session(client_key, client_secret)

    base_url = 'https://api.twitter.com/1.1/statuses/user_timeline.json?'
    params = {'screen_name': screen_name,
              'count': 200,                # Maximum for each request
              'exclude_replies': True,     # Don't need replies
              'include_rts': False}        # Don't want retweets

    url = base_url + urllib.parse.urlencode(params)

    json_data = twitter.get(url).json()

    if not json_data:
        sys.exit('User has no tweets')

    if 'errors' in json_data:
        error = json_data.get('errors')[0]
        if error.get('code') is 34:
            sys.exit('User does not exist')
        else:
            sys.exit(error)

    print('Getting tweets from %s...' % screen_name)

    # A single response includes up to 200 tweets. We can get as many as the
    # API lets us (up to 3200) by continually making requests with the max_id
    # parameter set to the id of the last tweet in the previous response - 1,
    # as described in
    # https://developer.twitter.com/en/docs/tweets/timelines/guides/working-with-timelines
    while True:
        max_id = json_data[-1]['id'] - 1
        next_url = url + '&max_id=' + str(max_id)
        tweet_batch = twitter.get(next_url).json()

        if not tweet_batch:
            break
        else:
            json_data += tweet_batch

    return json.dumps(json_data)
