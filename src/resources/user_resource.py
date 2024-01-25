from flask.views import MethodView
from flask_smorest import Blueprint
from flask_jwt_extended import jwt_required
from schemas.user_schema import UserProfileSchema, ChangePasswordSchema

from controller.user_controller.user_profile_controller import UserProfileController
from controller.user_controller.change_password_controller import ChangePasswordController
from tokens.token import Token

blp = Blueprint("user", __name__, description = "User related operations")

@blp.route("/my-profile")
class UserProfile(MethodView):
    @blp.doc(
        parameters = [
        {
            'name': 'Authorization',
            'in': 'header',
            'description': 'Authorization: Bearer <access_token>',
            'required': 'true'
        }
    ])
    @blp.response(200, UserProfileSchema)
    @jwt_required()
    def get(self):
        token_obj = Token()
        user_profile_controller_obj = UserProfileController(token_obj)
        return user_profile_controller_obj.get_user_profile_data()

@blp.route("/change-password")
class ChangeUserPassword(MethodView):
    @blp.doc(
        parameters = [
        {
            'name': 'Authorization',
            'in': 'header',
            'description': 'Authorization: Bearer <access_token>',
            'required': 'true'
        }
    ])
    @blp.arguments(ChangePasswordSchema)
    @blp.response(200, ChangePasswordSchema)
    @jwt_required()
    def put(self, user_data):
        token_obj = Token()
        change_profile_controller_obj = ChangePasswordController(token_obj)
        return change_profile_controller_obj.change_user_password(user_data)