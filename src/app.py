"""Module for initializing app."""

from flask import Flask, g
from flask_smorest import Api
from flask_cors import CORS


def create_app() -> Flask:
    """
        Function which will be invoked on starting of application.
        Parameters -> None
        Returns -> Flask application
    """
    app = Flask(__name__)
    CORS(app)

    app.logger.info("Application server started.")

    with app.app_context():
        from src.helpers.common_helper import generate_shortuuid
        from src.api_setup import app_setup, jwt_setup, register_blueprint, register_flask_custom_error_handler

        register_flask_custom_error_handler(app)
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
