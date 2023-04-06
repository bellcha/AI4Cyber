from __future__ import annotations

from typing import Any, List, Optional

from pydantic import BaseModel, Field


class Author(BaseModel):
    username: str
    id: str
    avatar_url: str
    is_subscribed: bool
    is_following: bool


class Pulse(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    author_name: Optional[str] = None
    modified: Optional[str] = None
    created: Optional[str] = None
    tags: Optional[List[str]] = None
    references: Optional[List] = None
    public: Optional[int] = None
    adversary: Optional[Any] = None
    targeted_countries: Optional[List] = None
    malware_families: Optional[List] = None
    attack_ids: Optional[List] = None
    industries: Optional[List] = None
    tlp: Optional[str] = Field(None, alias='TLP')
    indicators: Optional[List] = None
    revision: Optional[int] = None
    groups: Optional[List] = None
    in_group: Optional[bool] = None
    author: Optional[Author] = None
    is_subscribing: Optional[Any] = None