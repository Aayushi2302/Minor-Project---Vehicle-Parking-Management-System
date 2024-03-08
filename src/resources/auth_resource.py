"""Module having end points related to authentication."""

from flask import current_app as app
from flask_jwt_extended import jwt_required
from flask.views import MethodView
from flask_smorest import Blueprint

from src.business.token_business.auth_token_business import AuthTokenBusiness
from src.config.app_config import AppConfig
from src.controller.auth_controller.login_controller import LoginController
from src.controller.auth_controller.logout_controller import LogoutController
from src.models.database import Database
from src.schemas.auth_schema import LoginSchema, LogoutSchema

blp = Blueprint("authentication", __name__, description="Authentication related operations")

# This is a dummy comment.

@blp.route("/v1/login")
class Login(MethodView):
    """
        Class containing various methods applicable to /v1/login route.
        ...
        Methods
        -------
        POST
    """

    @blp.arguments(LoginSchema)
    @blp.response(AppConfig.HTTP_STATUS_OK, LoginSchema)
    def post(self, credentials: dict) -> dict:
        """
            Method for login into system.
            ...
            On Success -> Follows LoginSchema and returns access and refresh tokens.
            On Failure -> Returns success = False and error message.
        """
        app.logger.info("User trying to login into the system.")
        return LoginController().user_login(credentials)


@blp.route("/v1/logout")
class Logout(MethodView):
    """
        Class containing various methods applicable to /v1/logout route.
        ...
        Methods
        -------
        POST
    """

    @blp.response(AppConfig.HTTP_STATUS_OK, LogoutSchema)
    @jwt_required()
    def post(self) -> dict:
        """
            Method for logout into system.
            ...
            On Success -> Follows LogoutSchema and returns success message.
            On Failure -> Returns success = False and error message.
        """
        app.logger.info("User trying to logout of the system.")
        db = Database()
        auth_token_business = AuthTokenBusiness(db)
        token_claims = auth_token_business.get_user_claims()
        return LogoutController().user_logout(token_claims)
