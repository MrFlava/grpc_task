from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, String

from db import engine


class Base(DeclarativeBase):
    pass


class Item(Base):
    __tablename__ = "items"

    id = Column(String, primary_key=True)
    description = Column(String)


Base.metadata.create_all(engine)
