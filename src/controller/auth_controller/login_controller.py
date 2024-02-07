"""
    Module for authenticating users based on their credentials.
    The user password is stored in hashed format.
    Default password is unhashed.
    User is directed to change-password on logging in with default password.
"""
import logging

from src.business.authentication_business.auth_business import AuthBusiness
from src.business.authentication_business.login_business import LoginBusiness
from src.business.token_business.auth_token_business import AuthTokenBusiness
from src.helpers.log_helper import get_request_id
from src.models.database import db
from src.utils.custom_error_handler import custom_error_handler
from src.utils.responses import SuccessResponse

logger = logging.getLogger(__name__)

class LoginController:
    """Class containing method for calling business for login.
       Methods
       -------
       user_login() : dict -> Returns dictionary response based on success or failure.
    """
    @custom_error_handler
    def user_login(self, credentials) -> tuple:
        """Method responsible for calling business logic for authentication.
           Parameters -> credentials : dict
           Return type -> dict
        """
        username = credentials["username"]
        password = credentials["password"]

        token_obj = AuthTokenBusiness(db)
        auth_business_obj = AuthBusiness(db)
        login_business_obj = LoginBusiness(db, token_obj, auth_business_obj)

        data = login_business_obj.authenticate_user(username, password)
        logger.info(f"[{get_request_id()}] : User loggedin successfully.")

        return SuccessResponse.jsonify_data("User loggedin successfully.", data), 200
