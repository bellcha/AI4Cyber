import tweepy
import configparser
from pathlib import Path
from tweet_model import Tweet, TweetSqlModel
import demoji
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
import re


config = configparser.ConfigParser()
config.read(Path(Path(__file__).parent).joinpath("twitter.ini"))

consumer_key = config["TWITTER"]["CONSUMER_KEY"]
consumer_secret = config["TWITTER"]["CONSUMER_KEY_SECRET"]

access_token = config["TWITTER"]["ACCESS_TOKEN"]
access_token_secret = config["TWITTER"]["ACCESS_TOKEN_SECRET"]

host = config["MYSQL"]["HOST"]
user = config["MYSQL"]["USER"]
passwd = config["MYSQL"]["PASSWORD"]
database = config["MYSQL"]["DATABASE"]


def emoji_converter(tweet_text: str):

    stripped_tweet = replace_new_line_with_space(tweet_text)

    return re.sub(r"[^A-Za-z0-9 ]+", "", demoji.replace_with_desc(stripped_tweet))


def replace_new_line_with_space(raw_tweet_text: str):

    return raw_tweet_text.replace("\n", " ")


def get_tweet_data(api: tweepy.API, tweet_id: str):

    try:

        response = api.get_status(tweet_id)._json

        return Tweet(**response)

    except tweepy.NotFound as err:
        print(err)

    except tweepy.Forbidden as err:
        print(err)


def main():

    file = "ai4cyber_alphv2_tweets.csv"

    engine = create_engine(f"mysql+pymysql://{user}:{passwd}@{host}/{database}")

    auth = tweepy.OAuth1UserHandler(
        consumer_key, consumer_secret, access_token, access_token_secret
    )

    api = tweepy.API(auth, wait_on_rate_limit=True)

    with open(file, "r") as f:

        lines = f.read().splitlines()

        tweet_ids = [l.split(",")[0] for l in lines]

    print(tweet_ids)

    # tweet_data = []
    # tweet_data = [

    # with open('converted_data.txt', 'a') as d:

    # for tweet_id in tweet_ids:
    # d = get_tweet_data(api, tweet_id)
    # tweet_data.append(d)
    # print(d.dict())

    with Session(engine) as session:

        for tweet_id in tweet_ids:

            tweet = get_tweet_data(api, tweet_id)

            try:
                post = TweetSqlModel(
                    tweet_id=tweet.id_str,
                    tweet_text=emoji_converter(tweet.text),
                    date_created=tweet.created_at,
                    user_id=tweet.user.id_str,
                    screen_name=tweet.user.screen_name,
                    user_name=emoji_converter(tweet.user.name)[:249],
                )
                session.add(post)
                session.commit()
                print(f"Record id {post.tweet_id} Inserted")
            except Exception as err:
                print(err)
                session.rollback()


if __name__ == "__main__":
    main()
