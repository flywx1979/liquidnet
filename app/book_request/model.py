from sqlalchemy import Integer, Column, String, DateTime
from app import db
from .contract import BookRequestContract


class BookRequest(db.Model):  # type: ignore

    __tablename__ = "book_request"

    request_id = Column(Integer(), primary_key=True)
    title = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)
    request_datetime = Column(DateTime, nullable=False)
