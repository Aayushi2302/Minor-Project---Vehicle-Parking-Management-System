"""Module having end points related to authentication."""

from flask import current_app as app
from flask_jwt_extended import jwt_required
from flask.views import MethodView
from flask_smorest import Blueprint

from src.config.app_config import AppConfig
from src.schemas.health_schema import HealthSchema
from src.utils.responses import SuccessResponse, ErrorResponse

blp = Blueprint("health", __name__, description="Health check for API")


@blp.route("/v1/health")
class Health(MethodView):
    """
        Class containing various methods applicable to /v1/health route.
        ...
        Methods
        -------
        GET
    """

    @blp.response(AppConfig.HTTP_STATUS_OK, HealthSchema)
    def get(self) -> tuple:
        """
            Method for checking if API is up..
            ...
            On Success -> Follows LoginSchema and returns access and refresh tokens.
            On Failure -> Returns success = False and error message.
        """
        return SuccessResponse.jsonify_data("API is healthy"), 200


