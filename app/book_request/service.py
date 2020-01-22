from app import db
from typing import List
from .model import BookRequest
from .contract import BookRequestContract
import uuid
from datetime import datetime


class BookRequestService:

    @staticmethod
    def get_all() -> List[BookRequest]:
        return BookRequest.query.all()

    @staticmethod
    def get_by_id(request_id: int) -> BookRequest:
        return BookRequest.query.get(request_id)

    @staticmethod
    def delete_by_id(request_id: int) -> List[int]:
        book_request = BookRequest.query.filter(BookRequest.request_id == request_id).first()
        if not book_request:
            return []
        db.session.delete(book_request)
        db.session.commit()
        return [request_id]

    @staticmethod
    def create(attributes: BookRequestContract) -> BookRequest:
        new_request = BookRequest(id=uuid.uuid1(), name=new_attrs["name"], purpose=new_attrs["purpose"])

        db.session.add(new_request)
        db.session.commit()

        return new_request
