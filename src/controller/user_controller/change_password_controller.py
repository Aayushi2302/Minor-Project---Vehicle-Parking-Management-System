"""Module for changing password of user on first login."""

from business.authentication_business.auth_business import AuthBusiness
from business.token_business.auth_token_business import AuthTokenBusiness
from business.user_business import UserBusiness
from models.database import db
from utils.custom_error_handler import custom_error_handler
from utils.responses import SuccessResponse

class ChangePasswordController:
    """
        Class containing method to invoke business logic for changing password on first login.
        ...
        Methods
        -------
        change_user_password(): dict -> Method to change user password.
    """
    @custom_error_handler
    def change_user_password(self, user_data: dict, username: str, role: str) -> dict:
        """
            Method to change user password on first login.
            Parameter -> user_data: dict, username: str, role: str
            Return type -> dict
        """
        current_password = user_data["current_password"]
        new_password = user_data["new_password"]

        auth_business_obj = AuthBusiness(db)
        token_obj = AuthTokenBusiness(db)
        user_business_obj = UserBusiness(db, auth_business_obj, token_obj, username, role)

        response = user_business_obj.change_password(current_password, new_password)
        return SuccessResponse.jsonify_data("Password changed successfully.", response), 200
