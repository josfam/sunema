"""Testing authentication routes"""

import flask


def test_user_cannot_register_more_than_once(
    test_client: flask.app.Flask.test_client,
):
    # first attempt
    data = {'username': 'jane doe', 'password': 'janespassword'}
    response = test_client.post('/api/v1/users', data=data)
    assert response.status_code == 200
    assert response.json == {'username': 'jane doe', 'message': 'user created'}

    # second attempt
    response = test_client.post('/api/v1/users', data=data)
    assert 400 <= response.status_code < 500
    assert response.json == {'message': 'username already registered'}
