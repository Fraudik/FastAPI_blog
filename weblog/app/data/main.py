import uvicorn

from fastapi import FastAPI, APIRouter, Query, HTTPException, Depends

from typing import Optional, Any
from sqlalchemy.orm import Session

from data.schemas.post import PostSearchResults, Post, PostCreate
from data.database.session import get_db
from data.crud import crud_post

# initialize database
import data.database.init_db # noqa


api_router = APIRouter()


@api_router.get("/", status_code=200)
def root(*, db: Session = Depends(get_db)) -> dict:
    return {"posts": crud_post.post.read_many(db=db, is_limit=True, limit=10)}


@api_router.get("/post/{post_id}", status_code=200, response_model=Post)
def fetch_post(*, post_id: int, db: Session = Depends(get_db)) -> Any:
    result = crud_post.post.read(db=db, requested_id=post_id)

    if not result:
        raise HTTPException(status_code=404, detail=f"Post with id {post_id} does not exist")

    return result


@api_router.get("/search/", status_code=200, response_model=PostSearchResults)
def search_posts(*,
                 keyword: Optional[str] = Query(None, min_length=3, example="sea"),
                 max_len: Optional[int] = 10,
                 db: Session = Depends(get_db)) -> dict:

    posts = crud_post.post.read_many(db=db)

    if not keyword:
        return {"results": posts}

    result = filter(lambda post: keyword.lower() in post.title.lower(), posts)
    return {"results": list(result)[:max_len]}


@api_router.post("/posts/", status_code=201, response_model=Post)
def create_post(*,
                post_in: PostCreate,
                db: Session = Depends(get_db)) -> dict:

    return crud_post.post.create(db=db, obj_in=post_in)


app = FastAPI()
app.include_router(api_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)
