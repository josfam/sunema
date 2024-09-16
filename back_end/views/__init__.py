from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1/')
weather_views = Blueprint(
    'weather_views', __name__, url_prefix='/api/v1/weather'
)
film_views = Blueprint('film_views', __name__, url_prefix='/api/v1/films')

from back_end.views.auth_routes import *
from back_end.views.location_routes import *
from back_end.views.weather import *
from back_end.views.film_routes import *
