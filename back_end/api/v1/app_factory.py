from flask import Flask
from models.engine.database import db
from views import app_views

def create_app(config_name):
    """Creates and returns the flask application instance"""

    app = Flask(__name__)

    # Configure your app
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///sunema.db"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize extensions
    db.init_app(app)

    # create database tables
    with app.app_context():
        db.create_all()

    # # Register blueprints
    app.register_blueprint(app_views)
    # app.register_blueprint(main)

    return app
