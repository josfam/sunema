#!/usr/bin/env python3

"""The database for the application"""

from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound
from app import db
from models.user import User


class DBQueries:
    """DB class for handling queries"""

    def __init__(self) -> None:
        """Initialize a new DB instance"""
        self.__session = db.session

    def find_user_by(self, **kwargs) -> User:
        """Find a user by arbitrary keyword arguments."""
        try:
            query = select(User).filter_by(**kwargs)
            user = db.session.execute(query).scalars().first()
        except NoResultFound:
            raise NoResultFound()
        except InvalidRequestError:
            raise InvalidRequestError()

        return user

    def update_user(self, user_id: int, **kwargs) -> None:
        """Update a user's attributes"""
        # Find the user by id
        user = self.find_user_by(id=user_id)

        # Update the user's attributes
        for key, value in kwargs.items():
            # Check if the attribute exists on the User model
            if not hasattr(user, key):
                raise ValueError(f"Invalid attribute: {key}")
            setattr(user, key, value)  # edit the user

        self.__session.commit()

    def save(self, obj):
        """Saves the provided object to the db"""
        self.__session.add(obj)
        self.__session.commit()
