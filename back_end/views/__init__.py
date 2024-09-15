from flask import Blueprint

app_views = Blueprint('app_views', __name__)

from back_end.views.auth_routes import *
