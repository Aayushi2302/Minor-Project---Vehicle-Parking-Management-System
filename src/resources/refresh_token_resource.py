"""Module containing end points related to parking slot resource."""

from flask_jwt_extended import jwt_required
from flask.views import MethodView
from flask_smorest import Blueprint

from config.app_config import AppConfig
from business.token_business.auth_token_business import AuthTokenBusiness
from controller.refresh_token_controller import RefreshTokenController
from models.database import db
from schemas.refresh_schema import RefreshSchema


blp = Blueprint("refresh token", __name__, description="Refresh token related operations")


@blp.route("/v1/refresh")
class RefreshToken(MethodView):
    """
        Class containing various methods applicable to /v1/refresh route.
        ...
        Methods
        -------
        POST
    """

    @blp.doc(parameters=[AppConfig.BLP_DOC_PARAMETERS])
    @blp.response(200, RefreshSchema)
    @jwt_required(refresh=True)
    def post(self) -> dict:
        """
            Method for creating parking slot.
            ...
            On Success -> Follows ParkingSlotWriteResponseSchema and returns success message.
            On Failure -> Returns success = False and error message.
        """
        token_obj = AuthTokenBusiness(db)
        token_payload = token_obj.get_user_claims()
        refresh_jti = token_payload["jti"]
        username = token_payload["sub"]
        role = token_payload["usr"]
        p_type = token_payload["pty"]

        return RefreshTokenController().refresh_token(refresh_jti, username, role, p_type)
