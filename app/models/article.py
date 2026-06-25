from sqlalchemy import Column, Integer, String, Text, DateTime
from app.database.db import Base

class Article(Base):
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String, nullable=False)

    url = Column(String, unique=True, nullable=False)

    source = Column(String)

    summary = Column(Text)

    published_at = Column(DateTime)
