from datetime import datetime
import pandas as pd
import numpy as np
from flask_script import Command

from app import db
from app.book_request,model import BookRequest
from datetime import datetime


def seeds():
    classes = [BookRequest]
    for klass in classes:
        seed_me(klass)


def seed_me(cls):
    rows = [
        {"request_id": "1234", "title": "book1", "email":"123@gmail.com", "created_datetime": datetime.now()},
        {"request_id": "3456", "title": "book2", "email":"345@gmail.com", "created_datetime": datetime.now()},
    ]
    db.session.bulk_insert_mappings(cls, rows)


class SeedCommand(Command):
    """ Seed the DB."""

    def run(self):
        if (
            input(
                "Are you sure you want to drop all tables and recreate? (y/N)\n"
            ).lower()
            == "y"
        ):
            print("Dropping tables...")
            db.drop_all()
            db.create_all()
            seeds()
            db.session.commit()
            print("DB successfully seeded.")
