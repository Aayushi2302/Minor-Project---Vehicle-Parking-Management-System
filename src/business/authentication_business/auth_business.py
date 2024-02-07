"""Module contaning business logic for authentication related tasks."""
import logging

from mysql import connector

from src.config.app_config import AppConfig
from src.config.query import QueryConfig
from src.models.database import Database
from src.helpers.common_helper import hash_password
from src.helpers.log_helper import get_request_id
from src.utils.custom_exceptions import DBException, InvalidLogin

logger = logging.getLogger(__name__)
# logger.addFilter(CustomFilter())

class AuthBusiness:
    """
        Class containing logic for handling authentication.
        ...
        Methods
        -------
        get_authentication_details() : dict -> get the password, role and password type details.
        verify_user_password() : bool -> use to verify the input and actual password.
    """
    def __init__(self, db: Database) -> None:
        """Constructor for auth business."""
        self.db = db

    def get_authentication_details(self, username: str) -> dict:
        """
            Method to get password, role and password type details.
            Parameters -> username: str
            Return type -> dict
        """
        try:
            user_data = self.db.fetch_data_from_database(
                            QueryConfig.FETCH_EMPLOYEE_CREDENTIALS,
                            (username, AppConfig.STATUS_ACTIVE)
                        )
            if not user_data:
                logger.warning(f"[{get_request_id()}] : Invalid login by user.")
                raise InvalidLogin(401, "Unauthorized", "Invalid user credentials.")

            logger.info(f"[{get_request_id()}] : Valid login by user.")
            return user_data[0]

        except connector.Error:
            raise DBException(500, "Internal Server Error", "Something wrong with the server.")

    def verify_user_password(self,
                            input_password: str,
                            actual_password: str,
                            password_type: str
    ) -> bool:
        """
            Method to verify the input and actual password.
            Parameter -> input_password: str, actual_password: str, password_type: str
            Return type -> bool
        """
        if password_type == AppConfig.PERMANENT_PASSWORD:
            input_password = hash_password(input_password)

        return actual_password == input_password
