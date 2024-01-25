from flask.views import MethodView
from flask_smorest import Blueprint

from schemas.auth_schema import LoginRequestSchema, LoginResponseSchema
from controller.auth_controller.login_controller import LoginController

blp = Blueprint("authentication", __name__, description = "Authentication related operations")

@blp.route("/login")
class Login(MethodView):
    @blp.arguments(LoginRequestSchema)
    @blp.response(200, LoginResponseSchema)
    def post(self, credentials):
        login_controller_obj = LoginController()
        return login_controller_obj.user_login(credentials)
