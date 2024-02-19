"""
    Module for logging out the user.
"""

from flask import current_app as app

from src.business.token_business.auth_token_business import AuthTokenBusiness
from src.models.database import db
from src.utils.custom_error_handler import custom_error_handler
from src.utils.responses import SuccessResponse


class LogoutController:
    """Class containing method for calling business for logout.
       Methods
       -------
       user_logout() : tuple -> Returns dictionary response based on success or failure.
    """

    @custom_error_handler
    def user_logout(self, token_claims: dict) -> tuple:
        """Method responsible for calling business logic for logging out the system for user..
           Parameters -> None
           Returns -> tuple
        """
        user_identity = token_claims["sub"]
        auth_token_business = AuthTokenBusiness(db)

        auth_token_business.revoke_token(user_identity)

        return SuccessResponse.jsonify_data("User logged out successfully."), 200
