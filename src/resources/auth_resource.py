"""Module having end points related to authentication."""

from flask.views import MethodView
from flask_smorest import Blueprint

from schemas.auth_schema import LoginRequestSchema, LoginResponseSchema
from controller.auth_controller.login_controller import LoginController

blp = Blueprint("authentication", __name__, description = "Authentication related operations")

@blp.route("/v1/login")
class Login(MethodView):
    """
        Class containing various methods applicable to /v1/login route.
        ...
        Methods
        -------
        POST
    """
    @blp.arguments(LoginRequestSchema)
    @blp.response(200, LoginResponseSchema)
    def post(self, credentials: dict) -> dict:
        """
            Method for login into system.
            ...
            On Success -> Follows LoginResponseSchema and returns access and refresh tokens.
            On Failure -> Returns success = False and error message.
        """
        return LoginController().user_login(credentials)
