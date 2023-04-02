import tweepy
import configparser
from pathlib import Path
import json

config = configparser.ConfigParser()
config.read(Path(Path(__file__).parent).joinpath("twitter.ini"))


bearer_token = config["TWITTER"]["BEARER_TOKEN"]

client = tweepy.Client(bearer_token)

response = client.search_recent_tweets("ransomware", max_results = 100)

tweets = response.data

for t in tweets:
    print(t.id)
    print(t.text)


#response = client.get_users_tweets(279390084)

#for i in response.data:
    #print(i.id)
    #print(i.text)
