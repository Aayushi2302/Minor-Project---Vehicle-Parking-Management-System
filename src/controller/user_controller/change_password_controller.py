from business.user_business import UserBusiness
from models.database import db
from utils.custom_error_handler import custom_error_handler
from utils.responses import SuccessResponse
from tokens.authorization_token import AuthorizationToken

class ChangePasswordController:
    def __init__(self, token_obj: AuthorizationToken) -> None:
        self.token_obj = token_obj

    @custom_error_handler
    def change_user_password(self, user_data: dict) -> dict:
        username = self.token_obj.get_user_identity()

        current_password = user_data["current_password"]
        new_password = user_data["new_password"]
        confirm_password = user_data["confirm_password"]

        user_business_obj = UserBusiness(db)
        user_business_obj.change_password(username, self.token_obj, current_password,
                                            new_password, confirm_password)
        return SuccessResponse.jsonify_data("Password changed successfully."), 200
