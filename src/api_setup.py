"""Module containing different functions for initializing app."""

import logging
from logging.handlers import SysLogHandler
import os
from flask import jsonify, g, Flask
from flask.logging import default_handler
from flask_jwt_extended import JWTManager
from flask_smorest import Api

from src.business.token_business.auth_token_business import AuthTokenBusiness
from src.config.app_config import AppConfig
from src.models.database import db
from src.resources.auth_resource import blp as AuthBlueprint
from src.resources.customer_resource import blp as CustomerBlueprint
from src.resources.employee_resource import blp as EmployeeBlueprint
from src.resources.parking_slot_resource import blp as ParkingSlotBlueprint
from src.resources.refresh_token_resource import blp as RefreshTokenBlueprint
from src.resources.slot_reservation_resource import blp as SlotReservationBlueprint
from src.resources.user_resource import blp as UserBlueprint
from src.resources.vehicle_type_resource import blp as VehicleTypeBlueprint

PAPERTRAIL_HOSTNAME = "logs2.papertrailapp.com"
PAPERTRAIL_PORT = 33514

class CustomFormatter(logging.Formatter):
    """
        Custom log formatter to format the logs and add request_id in each log.
        ...
        Methods
        -------
        format(): str -> overriden the parent format method to add request_id field.
    """

    def format(self, record: logging.LogRecord) -> str:
        """
            Method to override the parent format methods.
            Parameters -> record
            Returns -> str
        """
        if hasattr(g, 'request_id'):
            record.request_id = g.request_id
        else:
            record.request_id = "REQapp01"
        return super().format(record)


def logging_configuration(app: Flask) -> None:
    """
        Function to set up logging configurations for app.
        Parameters -> Flask app
        Returns -> None
    """
    app.logger.removeHandler(default_handler)
    formatter = CustomFormatter(
        fmt='%(asctime)s %(levelname)-8s [%(filename)s %(funcName)s:%(lineno)d] %(message)s - [%(request_id)s]'
    )
    handler = SysLogHandler(address=(PAPERTRAIL_HOSTNAME, PAPERTRAIL_PORT))
    handler.setFormatter(formatter)
    handler.setLevel(logging.DEBUG)

    app.logger.addHandler(handler)
    app.logger.setLevel(logging.DEBUG)


def app_setup(app: Flask) -> None:
    """
        Function having statements for setting of app and document related configuration.
        Parameters -> Flask app
        Returns -> None
    """
    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "Vehicle Parking Management System REST API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/parking-management/v1"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    db.create_all_tables()
    logging_configuration(app)
    app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")


def jwt_setup(app: Flask) -> None:
    """
        Function for setting of JWT related configurations.
        Parameters -> Flask app
        Returns -> None
    """
    jwt = JWTManager(app)
    token = AuthTokenBusiness(db)

    @jwt.expired_token_loader
    def expired_token_callback(jwt_header: dict, jwt_payload: dict) -> tuple:
        """
            Function to check for expired JWT.
            Parameters -> jwt_header: dict, jwt_payload: dict
            Returns -> tuple
        """
        return (
            jsonify({"message": "The token has expired.", "error": "token_expired"}),
            401,
        )

    @jwt.invalid_token_loader
    def invalid_token_callback(error: str) -> tuple:
        """
            Function to check for invalid JWT.
            Parameters -> error: str
            Returns -> tuple
        """
        return (
            jsonify(
                {"message": "Signature verification failed.", "error": "invalid_token"}
            ),
            401,
        )

    @jwt.unauthorized_loader
    def missing_token_callback(error: str) -> tuple:
        """
            Function to check for missing JWT.
            Parameters -> error: str
            Returns -> tuple
        """
        return (
            jsonify(
                {
                    "description": "Request does not contain an access token.",
                    "error": "authorization_required",
                }
            ),
            401,
        )

    @jwt.token_in_blocklist_loader
    def check_if_token_in_blocklist(jwt_header, jwt_payload) -> bool:
        """
            Function to check for revoked JWT.
            Parameters -> jwt_header: dict, jwt_payload: dict
            Returns -> bool
        """
        check_access_token = token.is_token_revoked(jwt_payload["jti"], "access_token")
        check_refresh_token = token.is_token_revoked(jwt_payload["jti"], "refresh_token")
        return check_access_token or check_refresh_token

    @jwt.revoked_token_loader
    def revoked_token_callback(jwt_header: dict, jwt_payload: dict) -> tuple:
        """
            Function to check for revoked JWT.
            Parameters -> jwt_header: dict, jwt_payload: dict
            Returns -> tuple
        """
        return (
            jsonify(
                {"description": "The token has been revoked.", "error": "token_revoked"}
            ),
            401,
        )


def register_blueprint(api: Api) -> None:
    """
        Function for registering various blueprints of API.
        Parameters -> API
        Returns -> None
    """
    api.register_blueprint(AuthBlueprint)
    api.register_blueprint(UserBlueprint)
    api.register_blueprint(EmployeeBlueprint)
    api.register_blueprint(VehicleTypeBlueprint)
    api.register_blueprint(ParkingSlotBlueprint)
    api.register_blueprint(CustomerBlueprint)
    api.register_blueprint(SlotReservationBlueprint)
    api.register_blueprint(RefreshTokenBlueprint)
