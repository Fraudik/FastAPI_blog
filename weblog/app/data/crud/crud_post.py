from typing import Union

from sqlalchemy.orm import Session

from data.crud.base import CRUDBase
from data.models.post import Post
from data.schemas.post import PostCreate, PostUpdateRestricted, PostUpdate
from data.models.user import User


class CRUDPost(CRUDBase[Post, PostCreate, PostUpdate]):
    def update(self, db: Session, *,
               db_obj: User,
               obj_in: Union[PostUpdate, PostUpdateRestricted]) -> Post:
        return super().update(db, db_obj=db_obj, obj_in=obj_in)


post = CRUDPost(Post)
