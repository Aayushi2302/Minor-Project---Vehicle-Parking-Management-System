"""Module for changing password of user on first login."""

from src.business.authentication_business.auth_business import AuthBusiness
from src.business.token_business.auth_token_business import AuthTokenBusiness
from src.business.user_business import UserBusiness
from src.models.database import db
from src.utils.custom_error_handler import custom_error_handler
from src.utils.responses import SuccessResponse


class ChangePasswordController:
    """
        Class containing method to invoke business logic for changing password on first login.
        ...
        Methods
        -------
        change_user_password(): tuple -> Method to change user password.
    """
    @custom_error_handler
    def change_user_password(self, user_data: dict, username: str, role: str) -> tuple:
        """
            Method to change user password on first login.
            Parameters -> user_data: dict, username: str, role: str
            Returns -> tuple
        """
        current_password = user_data["current_password"]
        new_password = user_data["new_password"]

        auth_business = AuthBusiness(db)
        token = AuthTokenBusiness(db)
        user_business= UserBusiness(db, auth_business, token, username, role)

        response = user_business.change_password(current_password, new_password)
        return SuccessResponse.jsonify_data("Password changed successfully.", response), 200
