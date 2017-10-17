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
              'count': 200,                # Maximum for each request
              'exclude_replies': True,     # Don't need replies
              'include_rts': False}        # Don't want retweets

    url = base_url + urllib.parse.urlencode(params)

    json_data = twitter.get(url).json()

    if 'errors' in json_data:  # Invalid screen name, probably
        sys.exit(json_data['errors'])

    # A single response includes up to 200 tweets. We can get as many as the
    # API lets us (up to 3200) by continually making requests with the max_id
    # parameter set to the id of the last tweet in the previous response - 1,
    # as described in
    # https://developer.twitter.com/en/docs/tweets/timelines/guides/working-with-timelines
    while True:
        max_id = json_data[-1]['id'] - 1
        next_url = url + "&max_id=" + str(max_id)
        tweet_batch = twitter.get(next_url).json()

        if not tweet_batch:
            break
        else:
            json_data += tweet_batch

    filename = 'json_data/' + screen_name + '.json'
    print('Writing %d tweets to %s' % (len(json_data), filename))

    json_str = json.dumps(json_data)
    json_file = open(filename, 'w')
    json_file.write(json_str)
    json_file.close()

if len(sys.argv) is 1:
    print('Missing argument')
else:
    download_tweets_json(sys.argv[1])
