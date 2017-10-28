# Trump Tweet Reception Predictor

### Peer reviewers, check nortti.win/introds for some static output

### Prerequisites
Python3, pip3
### Setup

Register a Twitter app at apps.twitter.com. Check the Keys and Access Tokens page, and set the following environment variables.
```sh
export client_key="key"        # Twitter Consumer Key
export client_secret="secret"  # Twitter Consumer Secret
```
Now run
```sh
git clone git@github.com:nortti/trump-tweet-reception-predictor.git
cd trump-tweet-reception-predictor
pip3 install virtualenv
virtualenv -p python3 venv
. venv/bin/activate
pip3 install -r requirements.txt
```

### Example usage (from virtual environment)
```sh
./generate.py realDonaldTrump
```
