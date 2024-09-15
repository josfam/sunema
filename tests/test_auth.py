"""Testing authentication routes"""

import flask
from sqlalchemy import select
from back_end.models.engine.database import db
from back_end.models.user import User

def test_user_cannot_register_more_than_once(
    test_client: flask.app.Flask.test_client,
):
    # first attempt
    data = {'username': 'jane doe', 'password': 'janespassword'}
    response = test_client.post('/api/v1/users', data=data)
    assert response.status_code == 200
    assert response.json == {'username': 'jane doe', 'message': 'user created'}

    # user is present in the db
    query = select(User).filter_by(username='jane doe')
    user = db.session.execute(query).scalars().first()
    assert user is not None
    assert user.username == 'jane doe'

    # second attempt
    response = test_client.post('/api/v1/users', data=data)
    assert 400 <= response.status_code < 500
    assert response.json == {'message': 'username already registered'}

    # only the one user entry from before should be in the db
    query = select(User).filter_by(username='jane doe')
    user = db.session.execute(query).scalars().all()
    assert len(user) == 1
