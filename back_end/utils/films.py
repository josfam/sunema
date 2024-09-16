"""Utility functions an objects for dealing with film data"""

import requests
from datetime import datetime as dt, timedelta

MIN_RATING = 6

# genres and genre ids, as per TMDB's api
genres_map = {
    'Action': 28,
    'Adventure': 12,
    'Animation': 16,
    'Comedy': 35,
    'Crime': 80,
    'Documentary': 99,
    'Drama': 18,
    'Family': 10751,
    'Fantasy': 14,
    'History': 36,
    'Horror': 27,
    'Music': 10402,
    'Mystery': 9648,
    'Romance': 10749,
    'Science Fiction': 878,
    'TV Movie': 10770,
    'Thriller': 53,
    'War': 10752,
    'Western': 37,
}


def get_temperature_desc(temperature):
    """Returns a short descriptive name for temperature ranges"""
    if temperature <= -10:
        return 'Very Cold'
    if -9 <= temperature <= 15:
        return 'Cold'
    if 16 <= temperature <= 26:
        return 'Mild'
    if 27 <= temperature <= 35:
        return 'Hot'
    if temperature >= 36:
        return 'Very Hot'


def get_genres(temperature_desc):
    """Returns a tuple of genre ids, based on the temperature description"""
    temperature_genres = {
        'Very Cold': (
            genres_map.get('Family'),
            genres_map.get('Romance'),
            genres_map.get('Comedy'),
            genres_map.get('Fantasy'),
            genres_map.get('TV Movie'),
            genres_map.get('Music'),
        ),
        'Cold': (
            genres_map.get('Horror'),
            genres_map.get('Drama'),
            genres_map.get('Thriller'),
            genres_map.get('Crime'),
            genres_map.get('Mystery'),
            genres_map.get('War'),
        ),
        'Mild': (
            genres_map.get('Action'),
            genres_map.get('Adventure'),
            genres_map.get('Romance'),
            genres_map.get('History'),
            genres_map.get('Western'),
            genres_map.get('Documentary'),
        ),
        'Hot': (
            genres_map.get('Action'),
            genres_map.get('Comedy'),
            genres_map.get('Animation'),
            genres_map.get('Science Fiction'),
            genres_map.get('Fantasy'),
            genres_map.get('Adventure'),
        ),
        'Very Hot': (
            genres_map.get('Thriller'),
            genres_map.get('Crime'),
            genres_map.get('Mystery'),
            genres_map.get('War'),
            genres_map.get('Western'),
            genres_map.get('Music'),
        ),
    }

    return temperature_genres.get(temperature_desc)


def get_movies(url) -> dict:
    """"""
    try:
        response = requests.get(url)
    except request.RequestException:
        return {'status_code': response.status_code, 'data': response.json()}
    return response.json()


def years_in_the_past(count: int) -> str:
    """Returns a date that is approximately count years in the past from the
    current date, formatted as `YYYY-MM-DD`"""
    now = dt.now()
    years_earlier = now - timedelta(days=count * 365)
    return years_earlier.strftime(r'%Y-%m-%d')
