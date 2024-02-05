"""Module for fetching loggedin user related details."""

from models.database import db
from business.authentication_business.auth_business import AuthBusiness
from business.token_business.auth_token_business import AuthTokenBusiness
from business.user_business import UserBusiness
from utils.responses import SuccessResponse
from utils.custom_error_handler import custom_error_handler

class UserProfileController:
    """
        Class contaning method for calling business for fetching user profile.
        ...
        Methods
        ------
        get_user_profile_data() : dict -> Method to invoke business logic for fetching user details.
    """
    @custom_error_handler
    def get_user_profile_data(self, username: str, role: str) -> dict:
        """
            Method to call business logic for user fetching user profile.
            Parameter -> username: str
            Return type -> dict
        """
        auth_business_obj = AuthBusiness(db)
        token_obj = AuthTokenBusiness(db)
        user_business_obj = UserBusiness(db, auth_business_obj, token_obj, username, role)

        data = user_business_obj.get_user_details()
        return SuccessResponse.jsonify_data("Data fetched successfully.", data), 200
