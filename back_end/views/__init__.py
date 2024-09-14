from flask import Blueprint

app_views = Blueprint('app_views', __name__)

from views.auth_routes import *
