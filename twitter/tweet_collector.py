import tweepy
import configparser
from pathlib import Path
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session
from sqlalchemy.types import Integer, String
from sqlalchemy import create_engine
import time

config = configparser.ConfigParser()
config.read(Path(Path(__file__).parent).joinpath("twitter.ini"))

host = config["MYSQL"]["HOST"]
user = config["MYSQL"]["USER"]
passwd = config["MYSQL"]["PASSWORD"]
database = config["MYSQL"]["DATABASE"]

engine = create_engine(f'mysql+pymysql://{user}:{passwd}@{host}/{database}')

class Base(DeclarativeBase):
    pass

class Tweet(Base):
    __tablename__ = "twitter"

    id: Mapped[int] = mapped_column(Integer(),primary_key=True)
    tweet: Mapped[str] = mapped_column(String(250))

bearer_token = config["TWITTER"]["BEARER_TOKEN"]

client = tweepy.Client(bearer_token)


response = client.search_recent_tweets("#threatintel", max_results =100)

next_token = response.meta['next_token']

while next_token != None:

    response = client.search_recent_tweets("#threatintel", max_results =100, next_token=next_token)

    print(response.meta['next_token'])


    tweets = response.data

    with Session(engine) as session:
        for tweet in tweets:
            t_text = str(tweet.text).replace('\n',' ')


            try:
                post = Tweet(id=int(tweet.id), tweet = t_text.encode('utf-8'))
                session.add(post)
                session.commit()
            except Exception as err:
                pass
    
    time.sleep(10)
    
    next_token = response.meta['next_token']