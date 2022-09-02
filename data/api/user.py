#  Copyright (c)  2022 Fraudik (Blinov Ilya)

from typing import Any

from fastapi import APIRouter, Depends, HTTPException

from fastapi.security import OAuth2PasswordRequestForm

from data.models.user import User
from data.schemas.user import User as schemas_User, UserCreate
from data.crud import crud_user

from sqlalchemy.orm.session import Session
from data.database.session import get_db

from data.api.auth import *

users_router = APIRouter()


# --- Token for OAuth2 ---


@users_router.post("/token")
def login(db: Session = Depends(get_db),
          data_in: OAuth2PasswordRequestForm = Depends()) -> Any:

    user = authenticate(username_in=data_in.username, password_in=data_in.password, db=db)

    if not user:
        raise HTTPException(status_code=400, detail="Invalid username or password")

    return {"access_token": create_access_token(sub=user.id), "token_type": "bearer"}


# --- Create ---


@users_router.post("/signup", response_model=schemas_User, status_code=201)
def create_signup(*,
                  db: Session = Depends(get_db),
                  user_in: UserCreate) -> Any:

    # Checking username and email

    is_used_email = db.query(User).filter(User.email == user_in.email).first()
    if is_used_email is not None:
        raise HTTPException(status_code=400, detail="This email is already being used by another user")

    is_used_username = db.query(User).filter(User.username == user_in.username).first()
    if is_used_username:
        raise HTTPException(status_code=400, detail="This username is already being used by another user")

    # Creating user

    user = crud_user.user.create(db=db, obj_in=user_in)

    return user


@users_router.get("/me", response_model=schemas_User)
def read_me(current_user: User = Depends(check_current_user_permissions)):
    return current_user
