from __future__ import annotations
from typing import Any, List, Optional
from pydantic import BaseModel
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.types import String
import configparser
from pathlib import Path

config = configparser.ConfigParser()
config.read(Path(Path(__file__).parent).joinpath("twitter.ini"))

table_name = config["MYSQL"]["TABLE"]


class Base(DeclarativeBase):
    pass


class TweetSqlModel(Base):
    __tablename__ = table_name

    tweet_id: Mapped[int] = mapped_column(String(250), primary_key=True)
    tweet_text: Mapped[str] = mapped_column(String(250))
    date_created: Mapped[int] = mapped_column(String(250))
    user_id: Mapped[str] = mapped_column(String(250))
    screen_name: Mapped[int] = mapped_column(String(250))
    user_name: Mapped[str] = mapped_column(String(250))


class UserMention(BaseModel):
    screen_name: str
    name: str
    id: int
    id_str: str
    indices: List[int]


class Entities(BaseModel):
    hashtags: List
    symbols: List
    user_mentions: List[UserMention]
    urls: List


class Description(BaseModel):
    urls: List


class Entities1(BaseModel):
    description: Description


class User(BaseModel):
    id: int
    id_str: str
    name: str
    screen_name: str
    location: str
    description: str
    url: Any
    entities: Entities1
    protected: bool
    followers_count: int
    friends_count: int
    listed_count: int
    created_at: str
    favourites_count: int
    utc_offset: Any
    time_zone: Any
    geo_enabled: bool
    verified: bool
    statuses_count: int
    lang: Any
    contributors_enabled: bool
    is_translator: bool
    is_translation_enabled: bool
    profile_background_color: str
    profile_background_image_url: Optional[Any] = None
    profile_background_image_url_https: Optional[Any] = None
    profile_background_tile: bool
    profile_image_url: Optional[str] = None
    profile_image_url_https: Optional[str] = None
    profile_banner_url: Optional[str] = None
    profile_link_color: Optional[str] = None
    profile_sidebar_border_color: str
    profile_sidebar_fill_color: str
    profile_text_color: str
    profile_use_background_image: bool
    has_extended_profile: bool
    default_profile: bool
    default_profile_image: bool
    following: bool
    follow_request_sent: bool
    notifications: bool
    translator_type: str
    withheld_in_countries: List


class UserMention1(BaseModel):
    screen_name: str
    name: str
    id: int
    id_str: str
    indices: List[int]


class Url(BaseModel):
    url: str
    expanded_url: str
    display_url: str
    indices: List[int]


class Entities2(BaseModel):
    hashtags: List
    symbols: List
    user_mentions: List[UserMention1]
    urls: List[Url]


class Description1(BaseModel):
    urls: List


class Entities3(BaseModel):
    description: Description1


class User1(BaseModel):
    id: int
    id_str: str
    name: str
    screen_name: str
    location: str
    description: str
    url: Any
    entities: Entities3
    protected: bool
    followers_count: int
    friends_count: int
    listed_count: int
    created_at: str
    favourites_count: int
    utc_offset: Any
    time_zone: Any
    geo_enabled: bool
    verified: bool
    statuses_count: int
    lang: Any
    contributors_enabled: bool
    is_translator: bool
    is_translation_enabled: bool
    profile_background_color: Optional[str] = None
    profile_background_image_url: Optional[str] = None
    profile_background_image_url_https: Optional[str] = None
    profile_background_tile: bool
    profile_image_url: Optional[str] = None
    profile_image_url_https: Optional[str] = None
    profile_banner_url: Optional[str] = None
    profile_link_color: str
    profile_sidebar_border_color: str
    profile_sidebar_fill_color: str
    profile_text_color: str
    profile_use_background_image: bool
    has_extended_profile: bool
    default_profile: bool
    default_profile_image: bool
    following: bool
    follow_request_sent: bool
    notifications: bool
    translator_type: str
    withheld_in_countries: List


class RetweetedStatus(BaseModel):
    created_at: str
    id: int
    id_str: str
    text: str
    truncated: bool
    entities: Entities2
    source: str
    in_reply_to_status_id: Optional[int] = None
    in_reply_to_status_id_str: Optional[str] = None
    in_reply_to_user_id: Optional[int] = None
    in_reply_to_user_id_str: Optional[str] = None
    in_reply_to_screen_name: Optional[str] = None
    user: User1
    geo: Any
    coordinates: Any
    place: Any
    contributors: Any
    is_quote_status: bool
    retweet_count: int
    favorite_count: int
    favorited: bool
    retweeted: bool
    possibly_sensitive: Optional[bool] = None
    possibly_sensitive_appealable: Optional[bool] = None
    lang: str


class Tweet(BaseModel):
    created_at: Optional[str] = None
    id: Optional[int] = None
    id_str: Optional[str] = None
    text: Optional[str] = None
    truncated: Optional[bool] = None
    entities: Optional[Entities] = None
    source: Optional[str] = None
    in_reply_to_status_id: Optional[Any] = None
    in_reply_to_status_id_str: Optional[Any] = None
    in_reply_to_user_id: Optional[Any] = None
    in_reply_to_user_id_str: Optional[Any] = None
    in_reply_to_screen_name: Optional[Any] = None
    user: Optional[User] = None
    geo: Optional[Any] = None
    coordinates: Optional[Any] = None
    place: Optional[Any] = None
    contributors: Optional[Any] = None
    retweeted_status: Optional[RetweetedStatus] = None
    is_quote_status: Optional[bool] = None
    retweet_count: Optional[int] = None
    favorite_count: Optional[int] = None
    favorited: Optional[bool] = None
    retweeted: Optional[bool] = None
    lang: Optional[str] = None
