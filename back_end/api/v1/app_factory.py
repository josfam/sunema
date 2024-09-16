from flask import Flask
from flask_cors import CORS
from back_end.models.engine.database import db
from back_end.views import app_views
from back_end.views import weather_views

def create_app(config=None):
    """Creates and returns the flask application instance"""

    app = Flask(__name__)

    # apply CORS to the whole app
    CORS(app, resources={r"/*": {"origins": "*"}})

    # Configure your app
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///sunema.db"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['TESTING'] = False  # dev environment by default

    # apply custom configuration if provided
    if config:
        app.config.update(config)

    # Initialize extensions
    db.init_app(app)

    # create database tables
    with app.app_context():
        db.create_all()

    # # Register blueprints
    app.register_blueprint(app_views)
    app.register_blueprint(weather_views)

    return app
