from sqlalchemy.orm import Session

from datetime import datetime

from data.database.base_class import Base # noqa
from data.database.session import engine, SessionLocal
from data.schemas.post import PostCreate
from data.crud import crud_post


TEST_POSTS = [
    {
        "id": 1,
        "title": "How i met race condition",
        "text": "'Race conditions' refers to bugs that occur due to the timing or order-of-execution "
                "of multiple operations. Here's how to deal with them."
    },
    {
        "id": 2,
        "title": "What's the difference between an ocean and a sea?",
        "text": "In terms of geography, seas are smaller than oceans and are usually located where "
                "the land and ocean meet. Typically, seas are partially enclosed by land."
    },
    {
        "id": 3,
        "title": "Why Is the Sky Blue?",
        "text": " Blue light is scattered in all directions by the tiny molecules of air in Earth's atmosphere. "
                "Blue is scattered more than other colors because it travels as shorter, smaller waves. "
                "This is why we see a blue sky most of the time. Lambda."
    },
]


# TODO add/create ADMIN
def init_db(db: Session) -> None:
    # for creating without migrations
    # Base.metadata.create_all(bind=engine)

    for post in TEST_POSTS:
        post_in = PostCreate(
            title=post["title"],
            text=post["text"],
            creation_time=datetime.now())
        crud_post.post.create(db, obj_in=post_in)


init_db(SessionLocal())
