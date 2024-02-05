"""Module contaning business logic for login functionality."""

from config.app_config import AppConfig
from business.authentication_business.auth_business import AuthBusiness
from business.token_business.token_access import TokenAccess
from models.database import Database
from utils.custom_exceptions import InvalidLogin
from utils.role_mapping import RoleMapping

class LoginBusiness:
    """
        Class containing logic for login.
        ...
        Methods
        -------
        authenticate_user() : bool -> method to validate user credentials.
    """
    def __init__(self,
                db: Database,
                token_obj: TokenAccess,
                auth_business_obj: AuthBusiness
    ) -> None:
        """Constructor for login business."""
        self.db = db
        self.token_obj = token_obj
        self.auth_business_obj = auth_business_obj

    def authenticate_user(self, username: str, input_password: str) -> bool:
        """
            Method to validate user credentials.
            Parameters -> credentials: dict
            Return type -> bool
        """
        user_data = self.auth_business_obj.get_authentication_details(username)

        actual_password = user_data["password"]
        role = user_data["role"]
        password_type = user_data["password_type"]

        if self.auth_business_obj.verify_user_password(input_password,
                                                        actual_password, password_type):
            mapped_role = RoleMapping[role]

            if password_type == AppConfig.DEFAULT_PASSWORD:
                p_type = 0
            else:
                p_type = 1

            tokens = self.token_obj.create_token(True, username,
                                                    {"usr": mapped_role, "pty": p_type})
            access_token =  tokens[0]
            refresh_token = tokens[1]
            return  {
                        "access_token" : access_token,
                        "refresh_token" : refresh_token
                    }
        else:
            raise InvalidLogin(401, "Unauthorized", "Invalid user login.")
