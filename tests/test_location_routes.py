"""Module: test_location_routes"""
from typing import assert_type
import flask
import requests


def get_country():
    """get country where the app is running"""
    response = requests.get('https://ipinfo.io')
    return response.json().get('country')


def test_get_location(
        test_client: flask.app.Flask.test_client,
):
    """Verify that the route returns the location information about the client"""
    response = test_client.get('/api/v1/location')
    assert response.status_code == 200
    assert_type(response.json, dict)
    assert response.json.get('country') == get_country()
