#!/usr/bin/env python3
"""Authentication module"""
import bcrypt
import uuid
from sqlalchemy.orm.exc import NoResultFound
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
        from models.engine.database import DBQueries

        self._db = DBQueries()

    def register_user(self, username: str, password: str) -> User:
        """Register a new user if the email doesn't exist."""

        # Check if the user already exists by email
        print('username', username, 'password', password)
        user = self._db.find_user_by(username=username)

        if user is not None:
            raise ValueError()
        # If the user is found, raise ValueError
        else:
            # If user is not found, create a new user
            hashed_password = _hash_password(password)
            new_user = User(username, hashed_password)
            new_user.save()
            return new_user

    def valid_login(self, username: str, password: str) -> bool:
        """Validates login credentials."""
        user = self._db.find_user_by(username=username)
        return bcrypt.checkpw(password.encode('utf-8'), user.hashed_password)

    def create_session(self, username: str) -> str:
        """Creates a new session for the user with the given email."""
        user = self._db.find_user_by(username=username)
        session_id = _generate_uuid()
        # Update the user's session_id and commit the changes
        self._db.update_user(user.id, session_id=session_id)
        return session_id

    def get_user_from_session_id(self, session_id: str) -> User:
        """Retrieves a user based on the session ID."""
        if session_id is None:
            return None

        try:
            user = self._db.find_user_by(session_id=session_id)
            return user
        except NoResultFound:
            return None

    def destroy_session(self, user_id: int) -> None:
        """Destroys a session by setting the session ID to None."""
        try:
            self._db.update_user(user_id, session_id=None)
        except NoResultFound:
            pass
