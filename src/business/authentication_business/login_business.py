"""Module containing business logic for login functionality."""

from flask import current_app as app

from config.app_config import AppConfig
from business.authentication_business.auth_business import AuthBusiness
from business.token_business.token_access import TokenAccess
from models.database import Database
from utils.custom_exceptions import AppException
from utils.role_mapping import RoleMapping


class LoginBusiness:
    """
        Class containing logic for login.
        ...
        Attributes
        ----------
        db: Database Object
        token: TokenAccess Object
        auth_business: AuthBusiness Object

        Methods
        -------
        authenticate_user() : list -> method to validate user credentials.
    """

    def __init__(self,
                 db: Database,
                 token: TokenAccess,
                 auth_business: AuthBusiness
                 ) -> None:
        """Constructor for login business."""
        self.db = db
        self.token = token
        self.auth_business = auth_business

    def authenticate_user(self, username: str, input_password: str) -> list:
        """
            Method to validate user credentials.
            Parameters -> username: str, input_password: str
            Returns -> list
        """
        user_data = self.auth_business.get_authentication_details(username)

        actual_password = user_data[0]["password"]
        role = user_data[0]["role"]
        password_type = user_data[0]["password_type"]

        if self.auth_business.verify_user_password(input_password,
                                                   actual_password, password_type):
            mapped_role = RoleMapping[role]

            if password_type == AppConfig.DEFAULT_PASSWORD:
                p_type = 0
            else:
                p_type = 1

            tokens = self.token.create_token(True, username,
                                             {"usr": mapped_role, "pty": p_type})
            access_token = tokens[0]
            refresh_token = tokens[1]
            app.logger.info(f"User logged in and token generated successfully : {username}")
            return [{
                "access_token": access_token,
                "refresh_token": refresh_token
            }]

        else:
            app.logger.warning(f"Invalid user login : {username}")
            raise AppException(401, "Unauthorized", "Invalid user login.")
