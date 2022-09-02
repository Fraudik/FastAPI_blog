#  Copyright (c)  2022 Fraudik (Blinov Ilya)

from typing import Any, Optional

from fastapi import APIRouter, Depends, HTTPException, Query, Request
from sqlalchemy.orm import Session

from data.crud import crud_post
from data.crud import crud_user
from data.api.user import check_current_user_permissions

from data.schemas.post import Post, PostCreate, PostSearchResults, PostUpdateRestricted
from data.models.user import User

from data.database.session import get_db


posts_router = APIRouter()


# --- Create ---


@posts_router.post("/new", status_code=201, response_model=Post)
def create_post(*,
                post_in: PostCreate,
                db: Session = Depends(get_db),
                current_user: User = Depends(check_current_user_permissions)) -> dict:

    return crud_post.post.create(db=db, obj_in=post_in, author=current_user)


# --- Read ---


@posts_router.get("/{post_id}", status_code=200, response_model=Post)
def read_post(*, post_id: int, db: Session = Depends(get_db)) -> Any:
    result = crud_post.post.read(db=db, requested_id=post_id)

    if not result:
        raise HTTPException(status_code=404, detail=f"Post with id {post_id} does not exist")

    return result


@posts_router.get("/my-posts/", status_code=200, response_model=PostSearchResults)
def read_user_posts(*, current_user: User = Depends(check_current_user_permissions)) -> Any:
    user_posts = current_user.posts

    if not user_posts:
        return {"results": []}

    return {"results": list(user_posts)}


@posts_router.get("/search/", status_code=200, response_model=PostSearchResults)
def search_posts(*,
                 keyword: Optional[str] = Query(None, min_length=3, example="sea"),
                 max_count: Optional[int] = 10,
                 db: Session = Depends(get_db)) -> dict:

    posts = crud_post.post.read_many(db=db)

    if not keyword:
        return {"results": posts}

    result = filter(lambda post: keyword.lower() in post.title.lower() + post.text.lower(), posts)
    return {"results": list(result)[:max_count]}


# --- Update ---


@posts_router.put("/{post_id}", status_code=201, response_model=Post)
def update_post(*, post_id: int, post_in: PostUpdateRestricted,
                db: Session = Depends(get_db),
                current_user: User = Depends(check_current_user_permissions)) -> dict:

    post = check_access(post_id=post_id, db=db, current_user=current_user)
    updated_post = crud_post.post.update(db=db, db_object=post, object_in=post_in)
    return updated_post


# --- Delete ---


@posts_router.delete("/delete/{post_id}", status_code=201, response_model=Post)
def delete_post(*, post_id: int,
                db: Session = Depends(get_db),
                current_user: User = Depends(check_current_user_permissions)) -> dict:

    post = check_access(post_id=post_id, db=db, current_user=current_user)
    updated_post = crud_post.post.delete(db=db, db_object=post)
    return updated_post


# -- Checker for update and delete  --


def check_access(post_id: int, db: Session, current_user: User) -> Any:
    post = crud_post.post.read(db, requested_id=post_id)

    if not post:
        raise HTTPException(status_code=404, detail=f"Post with id {post_id} does not exist")

    if post.author_id != current_user.id and \
            not crud_user.user.is_moderator(current_user):
        raise HTTPException(status_code=403, detail=f"You can update or delete only your posts")

    return post

