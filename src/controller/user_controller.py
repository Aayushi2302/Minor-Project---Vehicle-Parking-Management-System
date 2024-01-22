import hashlib
import logging

from config.app_config import AppConfig
from config.prompts.prompts import Prompts
from config.query import QueryConfig
from models.database import Database
from utils.common_helper import CommonHelper

logger = logging.getLogger(__name__)

class UserController:

    def __init__(self, db: Database):
        self.db = db

    def view_user_details(self, username: str):
        """
            Method to display a particular user details.
            Parameter -> self, username
            Return type -> None
        """
        emp_data =  self.db.fetch_data_from_database(
                        QueryConfig.VIEW_SINGLE_EMPLOYEE_DETAIL,
                        (username, )
                    )
        json_response = emp_data[0]
        return json_response

    def change_password(self, username: str, new_password: str, confirm_password: str) -> None:
        """
            Method for creating new password for the user following strong password recommendation.
            Parameter -> self, username: str
            Return type -> None
        """
        if new_password != confirm_password:
            return 0
        else:
            hashed_password = hashlib.sha256(confirm_password.encode('utf-8')).hexdigest()

            self.db.save_data_to_database(
                QueryConfig.UPDATE_DEFAULT_PASSWORD,
                (hashed_password, AppConfig.PERMANENT_PASSWORD, username)
            )
            return 1

