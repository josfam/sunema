#!/usr/bin/env python3

"""Base class from which other models will inherit"""


class Base:
    """Base class from which other models will inherit"""

    def __init__(self):
        from db import DBQueries

        self.queryDB = DBQueries()

    def save(self):
        """Saves the user to the database"""
        self.queryDB.save(self)
