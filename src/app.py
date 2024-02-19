"""Module for initializing app."""

import logging
from flask import Flask, g
from flask_smorest import Api

from src.helpers.common_helper import generate_shortuuid
from src.api_setup import app_setup, jwt_setup, register_blueprint, logging_configuration

logger = logging.getLogger(__name__)


def create_app() -> Flask:
    """
        Function which will be invoked on starting of application.
        Parameters -> None
        Returns -> Flask application
    """
    app = Flask(__name__)
    app_setup(app)
    api = Api(app)
    jwt_setup(app)
    register_blueprint(api)

    @app.before_request
    def get_request_id() -> None:
        """
            Function that will be invoked before every request to reset request id.
            Parameters -> None
            Returns -> None
        """
        new_request_id = generate_shortuuid("REQ")
        g.request_id = new_request_id

    return app
