#  Copyright (c)  2022 Fraudik (Blinov Ilya)

import uvicorn

from fastapi import FastAPI, APIRouter

from data.api.post import posts_router
from data.api.user import users_router

from fastapi import Depends, Request
from sqlalchemy.orm import Session

from data.crud import crud_post
from data.database.session import get_db

# initialize database
import data.database.init_db # noqa

from fastapi.templating import Jinja2Templates
from pathlib import Path

TEMPLATES = Jinja2Templates(directory=str(Path(__file__).resolve().parent / "templates"))
root_router = APIRouter()


@root_router.get("/", status_code=200)
def index(request: Request, db: Session = Depends(get_db)):
    return TEMPLATES.TemplateResponse(
        "index.html",
        {"request": request,
         "posts": crud_post.post.read_many(db=db, limit=10)},
    )


app = FastAPI()
app.include_router(root_router, tags=["root"])
app.include_router(posts_router, prefix="/posts", tags=["posts"])
app.include_router(users_router, prefix="/auth", tags=["users"])


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)
