"""Module contaning logic related to user operations."""

from mysql import connector

from src.config.app_config import AppConfig
from src.config.query import QueryConfig
from src.business.authentication_business.auth_business import AuthBusiness
from src.business.token_business.token_access import TokenAccess
from src.models.database import Database
from src.helpers.common_helper import hash_password
from src.utils.custom_exceptions import DBException, InvalidLogin

class UserBusiness:
    """
        Class contaning logic for fetching user profile and perform user related operations.
        ...
        Methods
        -------
        get_user_details(): dict -> method to get user related details.
        validate_current_password() : dict -> method to validate user current password.
        change_password() : dict -> method to change user current password and revoke previous 
                                    tokens and generate new tokens.
    """
    def __init__(self,
                db: Database,
                auth_business_obj: AuthBusiness,
                token_obj: TokenAccess,
                username: str,
                role: str
    ) -> None:
        """Constructors for user business."""
        self.db = db
        self.auth_business_obj = auth_business_obj
        self.token_obj = token_obj
        self.username = username
        self.role = role

    def get_user_details(self) -> dict:
        """
            Method to get user related details.
            Parameter -> username: str
            Return type -> dict
        """
        try:
            emp_data =  self.db.fetch_data_from_database(
                            QueryConfig.VIEW_SINGLE_EMPLOYEE_DETAIL,
                            (self.username, )
                        )
            if not emp_data:
                return emp_data
            return emp_data[0]
        except connector.Error:
            raise DBException(500, "Internal Server Error", "Something went wrong with the server.")

    def validate_current_password(self, current_password: str) -> dict:
        """
            Method to validate user current password.
            Parameter -> username: str, current_password: str
            Return type -> dict
        """
        auth_data = self.auth_business_obj.get_authentication_details(self.username)

        actual_password = auth_data["password"]
        password_type = auth_data["password_type"]

        return self.auth_business_obj.verify_user_password(current_password,
                                                             actual_password, password_type)

    def change_password(self, current_password: str, new_password: str) -> None:
        """
            Method to change user password.
            Parameter -> current_password: str, new_password: str
            Return type -> None
        """
        try:
            result = self.validate_current_password(current_password)

            if not result:
                raise InvalidLogin(401, "Unauthorized", "Invalid credentials.")

            hashed_password = hash_password(new_password)
            self.db.save_data_to_database(
                QueryConfig.UPDATE_DEFAULT_PASSWORD,
                (hashed_password, AppConfig.PERMANENT_PASSWORD, self.username)
            )

            self.token_obj.revoke_token(self.username)
            tokens = self.token_obj.create_token(True, self.username,
                                                    {"usr": self.role, "pty": 1})
            access_token =  tokens[0]
            refresh_token = tokens[1]
            return  {
                        "access_token" : access_token,
                        "refresh_token" : refresh_token
                    }
        except connector.Error:
            raise DBException(500, "Internal Server Error", "Something went wrong with the server.")
