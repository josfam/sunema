"""For various pytest fixtures"""

import pytest
from back_end.api.v1.app_factory import create_app
from back_end.models.engine.database import db


@pytest.fixture(scope='module')
def test_client():
    """Sets up necessary configurations for a test client, that can be reused
    by all test functions that use this fixture"""
    app = create_app(
        {
            'TESTING': True,
            'SQLALCHEMY_DATABASE_URI': 'sqlite:///test.db',  # test database
        }
    )

    with app.test_client() as testing_client:
        with app.app_context():
            db.create_all()  # creating tables in the test environment
            yield testing_client
            db.drop_all()  # clean up logic after test run
