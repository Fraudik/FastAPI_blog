from typing import Optional

from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    username: str
    email: Optional[EmailStr] = None
    is_moderator: bool = False


class UserCreate(UserBase):
    email: EmailStr
    password: str


class UserUpdate(UserBase):
    pass


class UserInDatabase(UserBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


class User(UserInDatabase):
    pass
