from pydantic import BaseModel

from datetime import datetime
from typing import Sequence


class PostBase(BaseModel):
    title: str
    text: str
    creation_time: datetime


class PostCreate(PostBase):
    title: str
    text: str
    # author_id: int


class PostUpdate(PostBase):
    id: int


class PostUpdateRestricted(BaseModel):
    id: int
    title: str


class PostInDatabase(PostBase):
    id: int
    # author_id: int

    class Config:
        orm_mode = True


class Post(PostInDatabase):
    pass


class PostSearchResults(BaseModel):
    results: Sequence[Post]
