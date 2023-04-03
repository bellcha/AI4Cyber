import tweepy
import configparser
from pathlib import Path
import json

config = configparser.ConfigParser()
config.read(Path(Path(__file__).parent).joinpath("twitter.ini"))


bearer_token = config["TWITTER"]["BEARER_TOKEN"]

client = tweepy.Client(bearer_token)

response = client.search_recent_tweets("alphv", max_results = 100)

tweets = response.data

with open('alphv_tweets.csv', 'w', encoding='utf-8') as w:
    w.write('tweet_id,tweet\n')
    for t in tweets:
        t_text = str(t.text).replace('\n',' ')
        w.write(f'{t.id},{t_text}\n')


#response = client.get_users_tweets(279390084)

#for i in tweets:
    #print(i.id)
    #print(str(i.text).replace('\n', ' '))
