# Trump Tweet Reception Predictor
### Prerequisites
Python3, pip3
### Getting tweets as json
As a starting point, json\_data/realDonaldTrump.json contains 200 tweets by trump. There should be no need to fetch more for now, but here's how anyway:

Register a Twitter app at apps.twitter.com. Check the Keys and Access Tokens page, and set the following environment variables.
```sh
export client_key="key"        # Twitter Consumer Key
export client_secret="secret"  # Twitter Consumer Secret
```
Now run
```sh
$ ./install.sh
. venv/bin/activate
./twitter_client.py realDonaldTrump
```
