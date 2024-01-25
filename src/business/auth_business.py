from mysql import connector

from config.app_config import AppConfig
from config.query import QueryConfig
from models.database import Database
from utils.common_helper import CommonHelper
from utils.custom_exceptions import InvalidLogin, DBException
from utils.role_mapping import RoleMapping
from tokens.authorization_token import AuthorizationToken

class AuthBusiness:

    def __init__(self, db: Database, token_obj: AuthorizationToken) -> None:
        self.db = db
        self.token_obj = token_obj

    def get_authentication_details(self, username: str) -> dict:
        try:
            user_data = self.db.fetch_data_from_database(
                            QueryConfig.FETCH_EMPLOYEE_CREDENTIALS,
                            (username, AppConfig.STATUS_ACTIVE)
                        )
            if not user_data:
                raise InvalidLogin(401, "Unauthorized", "Invalid user credentials.")
            
            return user_data[0]

        except connector.Error:
            raise DBException(500, "Internal Server Error", "Something wrong with the server.")

    def verify_user_password(self, input_password: str, actual_password: str, password_type: str) -> bool:
        if password_type == AppConfig.PERMANENT_PASSWORD:
            input_password = CommonHelper.hash_password(input_password)
        
        return actual_password == input_password
              
    def authenticate_user(self, username: str, input_password: str) -> bool:
        user_data = self.get_authentication_details(username)

        actual_password = user_data["password"]
        role = user_data["role"].upper()
        password_type = user_data["password_type"]

        if self.verify_user_password(input_password, actual_password, password_type):
            mapped_role = RoleMapping[role]
            tokens = self.token_obj.create_token(True, username, {"usr": mapped_role})
            access_token =  tokens[0]
            refresh_token = tokens[1]
            return  {
                        "access_token" : access_token,
                        "refresh_token" : refresh_token,
                        "password_type" : password_type
                    }
        else:
            raise InvalidLogin(401, "Unauthorized", "Invalid user login.")
