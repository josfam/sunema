from flask import Flask
from models.engine.database import db
from views import app_views

# from .models import User  # Import your models here
# from .routes import main  # Assuming you have a blueprint named 'main'


def create_app(config_name):
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
