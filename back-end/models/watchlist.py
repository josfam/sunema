#!/usr/bin/env python3

"""Watchlist model for the application"""

from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Watchlist(Base):
    """Models a Watchlist of a user"""

    __tablename__ = 'watchlists'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    film_id = Column(Integer, nullable=False)

    # Relationships
    user = relationship('User', back_populates='watchlists')
