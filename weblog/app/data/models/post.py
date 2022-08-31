from sqlalchemy import Column, Integer, DateTime, String, Text, ForeignKey
from sqlalchemy.orm import relationship

from data.database.base_class import Base


class Post(Base):
    id = Column(Integer, primary_key=True, index=True)
    creation_time = Column(DateTime, nullable=False)
    title = Column(String(100), nullable=False)
    text = Column(Text,  nullable=False)
    # author_id = Column(Integer, ForeignKey("user.id"), nullable=True)
    # author = relationship("User", back_populates="posts")
