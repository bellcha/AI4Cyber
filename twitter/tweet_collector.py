import tweepy
import configparser
from pathlib import Path
import sq

config = configparser.ConfigParser()
config.read(Path(Path(__file__).parent).joinpath("twitter.ini"))


bearer_token = config["TWITTER"]["BEARER_TOKEN"]

client = tweepy.Client(bearer_token)

response = client.search_recent_tweets("alphv", max_results = 100)

tweets = response.data

print(tweets)