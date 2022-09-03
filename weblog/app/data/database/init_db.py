#  Copyright (c)  2022 Fraudik (Blinov Ilya)

from sqlalchemy.orm import Session

from datetime import datetime

from data.database.base_class import Base # noqa
from data.database.session import engine, SessionLocal

from data.schemas.post import PostCreate
from data.schemas.user import UserCreate

from data.crud import crud_post, crud_user
from data.configuration import settings


TEST_POSTS = [
    {
        "title": "How i met race condition",
        "text": "'Race conditions' refers to bugs that occur due to the timing or order-of-execution "
                "of multiple operations. Here's how to deal with them."
    },
    {
        "title": "What's the difference between an ocean and a sea?",
        "text": "In terms of geography, seas are smaller than oceans and are usually located where "
                "the land and ocean meet. Typically, seas are partially enclosed by land."
    },
    {
        "title": "Why Is the Sky Blue?",
        "text": " Blue light is scattered in all directions by the tiny molecules of air in Earth's atmosphere. "
                "Blue is scattered more than other colors because it travels as shorter, smaller waves. "
                "This is why we see a blue sky most of the time."
    },
]


def init_db(db: Session) -> None:
    Base.metadata.create_all(bind=engine)

    admin = crud_user.user.read_by_username(db, username=settings.ADMIN_USERNAME)

    if not admin:
        user_in = UserCreate(username=settings.ADMIN_USERNAME,
                             email=settings.ADMIN_EMAIL,
                             is_moderator=True,
                             password=settings.ADMIN_PASSWORD)
        admin = crud_user.user.create(db, obj_in=user_in)

    if not admin.posts:
        for post in TEST_POSTS:
            post_in = PostCreate(title=post["title"],
                                 text=post["text"],
                                 creation_time=datetime.now())
            crud_post.post.create(db, obj_in=post_in, author=admin)


init_db(SessionLocal())
