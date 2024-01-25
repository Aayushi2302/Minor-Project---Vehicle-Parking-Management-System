from mysql import connector

from config.app_config import AppConfig
from business.auth_business import AuthBusiness
from config.query import QueryConfig
from models.database import Database
from utils.custom_exceptions import DBException, PasswordNotMatch, InvalidLogin
from utils.common_helper import CommonHelper
from tokens.token import Token

class UserBusiness:
    def __init__(self, db: Database) -> None:
        self.db = db

    def get_user_details(self, username: str) -> dict:
        try:
            emp_data =  self.db.fetch_data_from_database(
                            QueryConfig.VIEW_SINGLE_EMPLOYEE_DETAIL,
                            (username, )
                        )
            return emp_data[0]
        except connector.Error:
            raise DBException(500, "Internal Server Error", "Something went wrong with the server.")

    def validate_current_password(self, username: str, token_obj: Token, current_password: str) -> dict:

        auth_business_obj = AuthBusiness(self.db, token_obj)
        auth_data = auth_business_obj.get_authentication_details(username)

        actual_password = auth_data["password"]
        password_type = auth_data["password_type"]

        return auth_business_obj.verify_user_password(current_password, actual_password, password_type)

    def change_password(self, username: str, token_obj: Token, current_password: str,
                        new_password: str, confirm_password: str) -> None:
        try:
            if new_password != confirm_password:
                raise PasswordNotMatch(400, "Bad Request", "The passwords you entered does not match.")

            result = self.validate_current_password(username, token_obj, current_password)

            if not result:
                raise InvalidLogin(401, "Unauthorized", "Invalid credentials.")

            hashed_password = CommonHelper.hash_password(new_password)
            self.db.save_data_to_database(
                QueryConfig.UPDATE_DEFAULT_PASSWORD,
                (hashed_password, AppConfig.PERMANENT_PASSWORD, username)
            )
        except connector.Error:
            raise DBException(500, "Internal Server Error", "Something went wrong with the server.")
