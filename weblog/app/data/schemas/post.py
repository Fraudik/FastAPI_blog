from typing import Sequence, Optional
from pydantic import BaseModel
from datetime import datetime


class PostBase(BaseModel):
    title: str
    text: str


class PostCreate(PostBase):
    pass


class PostUpdate(PostBase):
    title: str
    text: str


class PostUpdateRestricted(BaseModel):
    title: str
    text: str


class PostInDatabase(PostBase):
    id: int
    author_id: int
    creation_time: datetime

    class Config:
        orm_mode = True


class Post(PostInDatabase):
    pass


class PostSearchResults(BaseModel):
    results: Sequence[Post]
