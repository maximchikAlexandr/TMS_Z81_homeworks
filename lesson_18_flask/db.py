from typing import Optional

from sqlalchemy import TIMESTAMP, URL, Column, Integer, String, create_engine
from sqlalchemy.engine.base import Engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()


class PostModel(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    created = Column(TIMESTAMP, nullable=False, default=func.current_timestamp())
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)


class EngineDB:
    url_obj = URL.create(
        "postgresql",
        username="postgres",
        password="1234",
        host="127.0.0.1",
        port=5432,
        database="blog_db",
    )
    __instance: Optional[Engine] = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = create_engine(url=cls.url_obj)
        return cls.__instance
