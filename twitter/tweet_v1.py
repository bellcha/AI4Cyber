import tweepy
import configparser
from pathlib import Path
import csv

config = configparser.ConfigParser()
config.read(Path(Path(__file__).parent).joinpath("twitter.ini"))

# Your app's API/consumer key and secret can be found under the Consumer Keys
# section of the Keys and Tokens tab of your app, under the
# Twitter Developer Portal Projects & Apps page at
# https://developer.twitter.com/en/portal/projects-and-apps
consumer_key = config["TWITTER"]["CONSUMER_KEY"]
consumer_secret = config["TWITTER"]["CONSUMER_KEY_SECRET"]

# Your account's (the app owner's account's) access token and secret for your
# app can be found under the Authentication Tokens section of the
# Keys and Tokens tab of your app, under the
# Twitter Developer Portal Projects & Apps page at
# https://developer.twitter.com/en/portal/projects-and-apps
access_token = config["TWITTER"]["ACCESS_TOKEN"]
access_token_secret = config["TWITTER"]["ACCESS_TOKEN_SECRET"]

auth = tweepy.OAuth1UserHandler(
    consumer_key, consumer_secret, access_token, access_token_secret
)

# If the authentication was successful, this should print the
# screen name / username of the account

api = tweepy.API(auth, wait_on_rate_limit=True)

# print(json.dumps(api.get_status("1643078290645581824")._json, indent=4))

# This will search for Tweets with the query "Twitter", returning up to the
# maximum of 100 Tweets per request to the Twitter API

# Once the rate limit is reached, it will automatically wait / sleep before
# continuing
with open("zero_day_042623_2.csv", "w", encoding="utf-8") as w:
    csv_writer = csv.writer(w,delimiter=',')
    header = ['tweet_id','tweet']
    csv_writer.writerow(header)
    for tweet in tweepy.Cursor(api.search_tweets, "zeroday").items():
        t_text = str(tweet.text).replace("\n", " ")
        row = [tweet.id,t_text]
        csv_writer.writerow(row)
