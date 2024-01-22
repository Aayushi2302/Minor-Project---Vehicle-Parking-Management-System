"""Module containing common helper methods which are shared across the project."""
from datetime import datetime
import hashlib
import logging
import re
import maskpass
import pytz
from tabulate import tabulate

from config.app_config import AppConfig
from config.prompts.prompts import Prompts
from config.query import QueryConfig
from config.query import TableHeader
from config.regex_pattern import RegexPattern
from models.database import db

logger = logging.getLogger(__name__)

class CommonHelper:
    """
        This class contain helper methods to be shared throughout the project.
        ...
        Methods
        -------
        is_admin_registered() -> Method to check whether the admin is registered or not.
        create_new_password() -> Method to create new password.
        view_individual_employee_details() -> Method for viewing details of individual employee.
        display_table() -> Method to print table using tabulate.
        input_validation() -> Method to validate input on basis of regex.
        get_current_date_and_time() -> Method to get current date and time using datetime library.
    """
    def is_admin_registered(self) -> bool:
        """
            Method for checking whether admin(first user of the system) is registered.
            Parameter -> self
            Return type -> bool
        """
        logger.info("Checking if admin exist in the system.")
        user_data = db.fetch_data_from_database(
                    QueryConfig.FETCH_EMPID_FROM_ROLE_AND_STATUS,
                    (AppConfig.ADMIN_ROLE, AppConfig.STATUS_ACTIVE)
                )
        if user_data:
            return True
        else:
            return False

    @staticmethod
    def display_table(data: list, headers: list) -> None:
        """
            Method to display data in tabular format using tabulate.
            Parameter -> data: list, headers: list
            Return type -> None
        """
        row_id = [i for i in range(1, len(data) + 1)]
        print(
            tabulate(
                data,
                headers,
                showindex = row_id,
                tablefmt = "simple_grid"
            )
        )

    @staticmethod
    def input_validation(regular_exp: str, input_field: str) -> bool:
        """
            Method to validate input on basis of regex.
            Parameter -> regular_exp: str, input_field: str
            Return type -> bool
        """
        logger.info("Validating input based on regex.")
        result = re.match(regular_exp, input_field)
        if result is not None:
            return True
        else:
            print(Prompts.INVALID_INPUT + "\n")
            logger.debug("Invalid input entered.")
            return False

    @staticmethod
    def get_current_date_and_time() -> tuple:
        """
            For recording current date and time.
            Parameter -> None
            Return type -> tuple
        """
        time_zone = pytz.timezone('Asia/Kolkata')
        current = datetime.now(time_zone)
        curr_time = current.strftime('%H:%M')
        curr_date = current.strftime('%d-%m-%Y')
        logger.info("Getting current date and time in IST format.")
        return (curr_date, curr_time)
    
    @staticmethod
    def jsonify_data(data: list, keys: list) -> dict:
        json_data = [dict(zip(keys, record)) for record in data]
        return json_data

