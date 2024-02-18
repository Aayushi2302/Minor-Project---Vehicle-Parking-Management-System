"""Module for fetching loggedin user related details."""

from models.database import db
from business.authentication_business.auth_business import AuthBusiness
from business.token_business.auth_token_business import AuthTokenBusiness
from business.user_business import UserBusiness
from utils.responses import SuccessResponse
from utils.custom_error_handler import custom_error_handler

class UserProfileController:
    """
        Class containing method for calling business for fetching user profile.
        ...
        Methods
        ------
        get_user_profile_data() : tuple -> Method to invoke business logic for fetching user details.
    """
    @custom_error_handler
    def get_user_profile_data(self, username: str, role: str) -> tuple:
        """
            Method to call business logic for user fetching user profile.
            Parameters -> username: str
            Returns -> tuple
        """
        auth_business = AuthBusiness(db)
        token = AuthTokenBusiness(db)
        user_business = UserBusiness(db, auth_business, token, username, role)

        data = user_business.get_user_details()
        return SuccessResponse.jsonify_data("Data fetched successfully.", data), 200
