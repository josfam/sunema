#!/usr/bin/env python3

"""Watchlist model for the application"""

from ..app import db
from base import Base


class Watchlist(db.Model, Base):
    """Models a Watchlist of a user"""

    __tablename__ = 'watchlists'

    id = db.Column(
        db.Integer, primary_key=True, nullable=False, autoincrement=True
    )
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    film_id = db.Column(db.Integer, nullable=False)

    # Relationships
    user = db.relationship('User', back_populates='watchlists')
