#!/usr/bin/env python
import os
from requests_oauthlib import OAuth1Session

client_key = os.environ['client_key']
client_secret = os.environ['client_secret']

twitter = OAuth1Session(client_key, client_secret)

url = "https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=realDonaldTrump"

r = twitter.get(url).json()

print(r)
