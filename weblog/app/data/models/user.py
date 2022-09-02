from sqlalchemy import Integer, String, Column, Boolean
from sqlalchemy.orm import relationship

from data.database.base_class import Base


class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(100), unique=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    # password stored as hash
    password = Column(String, nullable=False)
    is_moderator = Column(Boolean, default=False)
    posts = relationship("Post", cascade="all,delete-orphan", back_populates="author", uselist=True)
