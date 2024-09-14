#!/usr/bin/env python3

"""User model for the application"""

# app = importlib.import_module("app")
from .engine.database import db
from models.base import Base


class User(db.Model, Base):
    """Models a user of the application"""

    __tablename__ = 'users'

    id = db.Column(
        db.Integer, primary_key=True, nullable=False, autoincrement=True
    )
    username = db.Column(db.String(250), nullable=False)
    hashed_password = db.Column(db.String(250), nullable=False)
    session_id = db.Column(db.String(250), nullable=True)
    reset_token = db.Column(db.String(250), nullable=True)

    def __init__(self, username, hashed_password):
        Base.__init__(self)
        self.username = username
        self.hashed_password = hashed_password
