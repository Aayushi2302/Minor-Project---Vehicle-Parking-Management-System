from flask import Flask, jsonify
from flask_smorest import Api
from flask_jwt_extended import JWTManager

from models.database import db
from resources.auth_resource import blp as AuthBlueprint
from resources.user_resource import blp as UserBlueprint
from resources.employee_resource import blp as EmployeeBlueprint
from resources.vehicle_type_resource import blp as VehicleTypeBlueprint
from blocklist import BLOCKLIST

BASE_URL = "/parking-management/v1"

def create_app():
    app = Flask(__name__)
    # app.register_error_handler - explore about it.

    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "Vehicle Parking Management System REST API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/parking-management/v1"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    db.create_all_tables()

    api = Api(app)

    app.config["JWT_SECRET_KEY"] = "301495134280069334565810139557053278463"
    jwt = JWTManager(app)

    @jwt.expired_token_loader
    def expired_token_callback(jwt_header, jwt_payload):
        return (
            jsonify({"message": "The token has expired.", "error": "token_expired"}),
            401,
        )

    @jwt.invalid_token_loader
    def invalid_token_callback(error):
        return (
            jsonify(
                {"message": "Signature verification failed.", "error": "invalid_token"}
            ),
            401,
        )

    @jwt.unauthorized_loader
    def missing_token_callback(error):
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
    def check_if_token_in_blocklist(jwt_header, jwt_payload):
        return jwt_payload["jti"] in BLOCKLIST

    @jwt.revoked_token_loader
    def revoked_token_callback(jwt_header, jwt_payload):
        return (
            jsonify(
                {"description": "The token has been revoked.", "error": "token_revoked"}
            ),
            401,
        )

    api.register_blueprint(AuthBlueprint, url_prefix = BASE_URL)
    api.register_blueprint(UserBlueprint, url_prefix = BASE_URL)
    api.register_blueprint(EmployeeBlueprint, url_prefix = BASE_URL)
    api.register_blueprint(VehicleTypeBlueprint, url_prefix = BASE_URL)
    
    return app
