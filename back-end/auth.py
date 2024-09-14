#!/usr/bin/env python3
"""Authentication module"""
import bcrypt
import uuid
from sqlalchemy.orm.exc import NoResultFound

from db import DB
from models.user import User


def _hash_password(password: str) -> bytes:
    """Hashes a password using bcrypt & returns the salted hash."""
    password_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password_bytes, salt)
    return hashed_password


def _generate_uuid() -> str:
    """Generates a new UUID & returns its string representation."""
    return str(uuid.uuid4())


class Auth:
    """Auth class to interact with the authentication database."""

    def __init__(self):
        self._db = DB()

    def register_user(self, username: str, password: str) -> User:
        """Register a new user if the email doesn't exist."""
        try:
            # Check if the user already exists by email
            self._db.find_user_by(username=username)
            # If the user is found, raise ValueError
            raise ValueError(f"User {username} already exists")
        except NoResultFound:
            # If user is not found, create a new user
            hashed_password = _hash_password(password)
            new_user = self._db.add_user(username, hashed_password)
            return new_user

    def valid_login(self, username: str, password: str) -> bool:
        """Validates login credentials."""
        try:
            user = self._db.find_user_by(username=username)
            return bcrypt.checkpw(password.encode('utf-8'),
                                  user.hashed_password)
        except NoResultFound:
            return False

    def create_session(self, username: str) -> str:
        """Creates a new session for the user with the given email."""
        try:
            user = self._db.find_user_by(username=username)
            session_id = _generate_uuid()
            # Update the user's session_id and commit the changes
            self._db.update_user(user.id, session_id=session_id)
            return session_id
        except NoResultFound:
            return None
