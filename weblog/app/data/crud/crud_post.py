from typing import Union

from datetime import datetime

from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder

from data.crud.base import CRUDBase
from data.models.post import Post
from data.schemas.post import PostCreate, PostUpdateRestricted, PostUpdate
from data.models.user import User


class CRUDPost(CRUDBase[Post, PostCreate, PostUpdate]):
    def create(self, db: Session, *, obj_in: PostCreate, author: User) -> Post:
        db_object = self.model(**jsonable_encoder(obj_in))
        db_object.author_id = author.id
        db_object.creation_time = datetime.now()

        db.add(db_object)
        db.commit()
        db.refresh(db_object)

        return db_object

    def update(self, db: Session, *,
               db_object: User,
               object_in: Union[PostUpdate, PostUpdateRestricted]) -> Post:
        return super().update(db, db_object=db_object, object_in=object_in)

    def delete(self, db: Session, *, db_object: User) -> Post:
        return super().delete(db, requested_id=db_object.id)


post = CRUDPost(Post)
