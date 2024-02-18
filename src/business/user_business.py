"""Module containing logic related to user operations."""

import pymysql

from config.app_config import AppConfig
from config.query import QueryConfig
from business.authentication_business.auth_business import AuthBusiness
from business.token_business.token_access import TokenAccess
from models.database import Database
from helpers.common_helper import hash_password
from utils.custom_exceptions import AppException, DBException


class UserBusiness:
    """
        Class containing logic for fetching user profile and perform user related operations.
        ...
        Attributes
        ----------
        db: Database Object
        auth_business: AuthBusiness Object
        token: TokenAccess Object
        username: str
        role: str
        Methods
        -------
        get_user_details(): list -> method to get user related details.
        validate_current_password() : dict -> method to validate user current password.
        change_password() : dict -> method to change user current password and revoke previous 
                                    tokens and generate new tokens.
    """
    def __init__(self,
                db: Database,
                auth_business: AuthBusiness,
                token: TokenAccess,
                username: str,
                role: str
    ) -> None:
        """Constructors for user business."""
        self.db = db
        self.auth_business = auth_business
        self.token = token
        self.username = username
        self.role = role

    def get_user_details(self) -> list:
        """
            Method to get user related details.
            Parameters -> None
            Returns -> dict
        """
        try:
            emp_data =  self.db.fetch_data_from_database(
                            QueryConfig.VIEW_SINGLE_EMPLOYEE_DETAIL,
                            (self.username, )
                        )
            return emp_data
        except pymysql.Error:
            raise DBException(500, "Internal Server Error", "Something went wrong with the server.")

    def validate_current_password(self, current_password: str) -> bool:
        """
            Method to validate user current password.
            Parameter -> username: str, current_password: str
            Return type -> dict
        """
        auth_data = self.auth_business.get_authentication_details(self.username)

        actual_password = auth_data[0]["password"]
        password_type = auth_data[0]["password_type"]

        return self.auth_business.verify_user_password(current_password,
                                                             actual_password, password_type)

    def change_password(self, current_password: str, new_password: str) -> list:
        """
            Method to change user password.
            Parameters -> current_password: str, new_password: str
            Returns -> None
        """
        try:
            result = self.validate_current_password(current_password)

            if not result:
                raise AppException(401, "Unauthorized", "Invalid credentials.")

            hashed_password = hash_password(new_password)
            self.db.save_data_to_database(
                QueryConfig.UPDATE_DEFAULT_PASSWORD,
                (hashed_password, AppConfig.PERMANENT_PASSWORD, self.username)
            )

            self.token.revoke_token(self.username)
            tokens = self.token.create_token(True, self.username,
                                                    {"usr": self.role, "pty": 1})
            access_token =  tokens[0]
            refresh_token = tokens[1]
            return  [{
                        "access_token" : access_token,
                        "refresh_token" : refresh_token
                    }]
        except pymysql.Error:
            raise DBException(500, "Internal Server Error", "Something went wrong with the server.")
