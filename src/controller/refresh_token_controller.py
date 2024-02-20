"""Module for generating access and refresh token."""

from src.business.token_business.auth_token_business import AuthTokenBusiness
from src.business.token_business.refresh_token_business import RefreshTokenBusiness
from src.models.database import Database
from src.utils.custom_error_handler import custom_error_handler
from src.utils.responses import SuccessResponse


class RefreshTokenController:
    """Class containing method for calling business for generating new access and refresh token
       Methods
       -------
       refresh_token() : tuple -> Returns a tuple containing new access token and refresh token.
    """

    @custom_error_handler
    def refresh_token(self, refresh_jti: str, username: str, role: str, p_type: int) -> tuple:
        """Method responsible for calling business logic for creating new access and refresh token.
           Parameters -> refresh_jti: str, username: str, role: str, p_type: str
           Returns -> tuple
        """
        db = Database()
        token = AuthTokenBusiness(db)
        refresh_token_business = RefreshTokenBusiness(db, token)

        data = refresh_token_business.generate_new_token(refresh_jti, username, role, p_type)

        return SuccessResponse.jsonify_data("New tokens generated successfully.", data), 200
