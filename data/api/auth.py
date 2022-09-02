#  Copyright (c)  2022 Fraudik (Blinov Ilya)

from typing import Optional
from datetime import datetime, timedelta

from pydantic import BaseModel

from fastapi import Depends, HTTPException, status

from jose import jwt, JWTError

from data.configuration import settings, auth_scheme, password_context

from data.models.user import User

from sqlalchemy.orm.session import Session
from data.database.session import get_db


# --- Checking current user ---


class TokenData(BaseModel):
    username: Optional[str] = None


def check_current_user_permissions(db: Session = Depends(get_db),
                                   token: str = Depends(auth_scheme)) -> User:

    credentials_exception = HTTPException(
       status_code=status.HTTP_401_UNAUTHORIZED,
       detail="Invalid credentials",
       headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(token, settings.JWT_SECRET,
                             algorithms=[settings.ALGORITHM],
                             options={"verify_aud": False})
        username: str = payload.get("sub")

        if username is None:
            raise JWTError

        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception

    user = db.query(User). \
        filter(User.id == token_data.username). \
        first()

    if user is None:
        raise credentials_exception

    return user


# --- Password and token ---


def verify_password(password_in: str, hashed_password: str) -> bool:
    return password_context.verify(password_in, hashed_password)


def authenticate(*, username_in: str, password_in: str, db: Session) -> Optional[User]:
    user = db.query(User). \
        filter(User.username == username_in). \
        first()

    if not user:
        return None

    if not verify_password(password_in, user.password):
        return None

    return user


def create_access_token(*, sub: str) -> str:
    # "iat" -- issued at
    # "exp" -- expiration time
    # "sub" -- subject
    payload = {
        "type": "access_token",
        "iat": datetime.utcnow(),
        "exp": datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_TIME),
        "sub": str(sub)
    }
    return jwt.encode(payload, settings.JWT_SECRET, algorithm=settings.ALGORITHM)

