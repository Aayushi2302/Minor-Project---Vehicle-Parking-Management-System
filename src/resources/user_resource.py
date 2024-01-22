from flask.views import MethodView
from flask_smorest import Blueprint, abort
from flask_jwt_extended import jwt_required, get_jwt_identity
from schemas.user_schema import UserProfileSchema, ChangePasswordSchema

from controller.user_controller import UserController
from models.database import db
from utils.decorators import error_handler

blp = Blueprint("user", __name__, description = "User related operations")

@blp.route("/my-profile")
class UserProfile(MethodView):
    @error_handler
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
        username = get_jwt_identity()
        user_controller_obj = UserController(db)
        response = user_controller_obj.view_user_details(username)

        return response

@blp.route("/change-password")
class ChangeUserPassword(MethodView):
    @error_handler
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
    def put(self, passwords):
        username = get_jwt_identity()
        user_controller_obj = UserController(db)
        result = user_controller_obj.change_password(
                    username,
                    passwords["new_password"],
                    passwords["confirm_password"]
                )
        if result == 0:
            abort(400, message="New and confirm password does not match. Please try again.")
        else:
            return  {"message" : "Password changed successfully."}
            