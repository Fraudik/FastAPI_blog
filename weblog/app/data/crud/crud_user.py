from typing import Any, Dict, Optional, Union

from sqlalchemy.orm import Session

from data.crud.base import CRUDBase
from data.models.user import User
from data.schemas.user import UserCreate, UserUpdate

from data.configuration import password_context


def get_hashed_password(password: str) -> str:
    return password_context.hash(password)


class CRUDUser(CRUDBase[User, UserCreate, UserUpdate]):
    def create(self, db: Session, *, obj_in: UserCreate) -> User:
        new_user_fields = obj_in.dict()
        new_user_fields.pop("password")

        new_user = User(**new_user_fields)
        new_user.password = get_hashed_password(obj_in.password)

        db.add(new_user)
        db.commit()

        return new_user

    def read_by_username(self, db: Session, *, username: str) -> Optional[User]:
        return db.query(User). \
            filter(User.username == username). \
            first()

    def is_moderator(self, user: User) -> bool:
        return user.is_moderator


user = CRUDUser(User)
