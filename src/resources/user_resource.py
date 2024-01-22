from flask.views import MethodView
from flask_smorest import Blueprint
from flask_jwt_extended import jwt_required, get_jwt_identity
from schemas.user_schema import UserProfileSchema

from controller.user_controller import UserController
from utils.decorators import error_handler

blp = Blueprint("user", __name__, description = "User related operations")

@blp.route("/my-profile")
class UserProfile(MethodView):
    @error_handler
    @jwt_required
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
    def get(self):
        username = get_jwt_identity()
        user_controller_obj = UserController()
        response = user_controller_obj.view_user_details(username)
        print(response)

        return response