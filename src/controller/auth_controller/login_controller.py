"""
    Module for authenticating users based on their credentials.
    The user password is stored in hashed format.
    Default password is un-hashed.
    User is directed to change-password on logging in with default password.
"""

from flask import current_app as app

from src.business.authentication_business.auth_business import AuthBusiness
from src.business.authentication_business.login_business import LoginBusiness
from src.business.token_business.auth_token_business import AuthTokenBusiness
from src.models.database import Database
from src.utils.custom_error_handler import custom_error_handler
from src.utils.responses import SuccessResponse


class LoginController:
    """Class containing method for calling business for login.
       Methods
       -------
       user_login() : tuple -> Returns dictionary response based on success or failure.
    """

    @custom_error_handler
    def user_login(self, credentials: dict) -> tuple:
        """Method responsible for calling business logic for authentication.
           Parameters -> credentials : dict
           Returns -> tuple
        """
        username = credentials["username"]
        password = credentials["password"]

        app.logger.info(f"User credentials retrieved successfully : {username}")

        db = Database()
        token = AuthTokenBusiness(db)
        auth_business = AuthBusiness(db)
        login_business = LoginBusiness(db, token, auth_business)

        data = login_business.authenticate_user(username, password)

        app.logger.info(f"Successful user login : {username}")
        return SuccessResponse.jsonify_data("User logged in successfully.", data), 200
