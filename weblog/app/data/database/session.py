from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from data.configuration import settings

#SQLALCHEMY_DATABASE_URI = "postgresql://postgres:password@db:5432/app"

engine = create_engine(settings.SQLALCHEMY_DATABASE_URI)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db() -> Generator:
    db = SessionLocal()
    db.current_user_id = None
    try:
        yield db
    finally:
        db.close()
