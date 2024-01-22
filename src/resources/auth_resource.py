from flask.views import MethodView
from flask_smorest import Blueprint, abort
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt
from schemas.auth_schema import LoginRequestSchema, LoginResponseSchema
from controller.auth_controller import AuthController
from utils.role_mapping import RoleMapping
from blocklist import BLOCKLIST

blp = Blueprint("authentication", __name__, description = "Authentication related operations")

@blp.route("/login")
class Login(MethodView):
    @blp.arguments(LoginRequestSchema)
    @blp.response(200, LoginResponseSchema)
    def post(self, credentials):
        auth_controller_obj = AuthController()
        role =  auth_controller_obj.authenticate_user(
                    credentials["username"],
                    credentials["password"]
                )
        if role:
            role = role.upper()
            get_mapped_role = RoleMapping[role]
            access_token =  create_access_token(
                                identity = credentials["username"],
                                additional_claims = {"usr": get_mapped_role}
                            )
            refresh_token = create_refresh_token(
                                identity = credentials["username"],
                                additional_claims = {"usr": get_mapped_role}
                            )
            return {
                    "access_token" : access_token, 
                    "refresh_token" : refresh_token, 
                    "message" : "User login successfully"
                }
        else:
            abort(401, message="Invalid login.")

@blp.route("/logout")
class Logout(MethodView):

    @jwt_required()
    @blp.doc(
        parameters = [
        {
            'name': 'Authorization', 
            'in': 'header', 
            'description': 'Authorization: Bearer <access_token>', 
            'required': 'true'
        }
    ])
    def post(self):
        jti = get_jwt()["jti"]
        BLOCKLIST.add(jti)
        return {"message" : "User logged out successfully."}
