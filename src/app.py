"""Module for initializing app."""

from flask import Flask
from flask_smorest import Api

from api_setup import app_setup, jwt_setup, register_blueprint

def create_app():
    """Function which will be invoked on starting of application."""
    app = Flask(__name__)
    app_setup(app)
    api = Api(app)
    jwt_setup(app)
    register_blueprint(api)

    return app
