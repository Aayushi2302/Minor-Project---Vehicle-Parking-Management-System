"""Module containing business logic for authentication related tasks."""

import pymysql

from config.app_config import AppConfig
from config.query import QueryConfig
from models.database import Database
from helpers.common_helper import hash_password
from utils.custom_exceptions import AppException, DBException


class AuthBusiness:
    """
        Class containing logic for handling authentication.
        ...
        Attributes
        ----------
        db: Database Object

        Methods
        -------
        get_authentication_details() : list -> get the password, role and password type details.
        verify_user_password() : bool -> use to verify the input and actual password.
    """

    def __init__(self, db: Database) -> None:
        """Constructor for auth business."""
        self.db = db

    def get_authentication_details(self, username: str) -> list:
        """
            Method to get password, role and password type details.
            Parameters -> username: str
            Returns -> list
        """
        try:
            user_data = self.db.fetch_data_from_database(
                QueryConfig.FETCH_EMPLOYEE_CREDENTIALS,
                (username, AppConfig.STATUS_ACTIVE)
            )

            if not user_data:
                raise AppException(401, "Unauthorized", "Invalid user credentials.")

            return user_data

        except pymysql.Error:
            raise DBException(500, "Internal Server Error", "Something wrong with the server.")

    def verify_user_password(self,
                             input_password: str,
                             actual_password: str,
                             password_type: str
                             ) -> bool:
        """
            Method to verify the input and actual password.
            Parameters -> input_password: str, actual_password: str, password_type: str
            Returns -> bool
        """
        if password_type == AppConfig.PERMANENT_PASSWORD:
            input_password = hash_password(input_password)

        return actual_password == input_password
