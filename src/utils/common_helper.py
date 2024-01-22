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

    def create_new_password(self, username: str) -> None:
        """
            Method for creating new password for the user following strong password recommendation.
            Parameter -> self, username: str
            Return type -> None
        """
        while True:
            logger.info("Updating password of user.")
            print(Prompts.CHANGE_PASSWORD + "\n")
            print(Prompts.STRONG_PASSWORD_REQUIREMENTS + "\n")
            input_password = maskpass.askpass(Prompts.INPUT_NEW_PASSWORD)
            is_strong_password = CommonHelper.input_validation(
                                    RegexPattern.PASSWORD_PATTERN,
                                    input_password
                                )
            if not is_strong_password:
                logger.warning("Strong password requirements not met.")
                print(Prompts.WEAK_PASSWORD_INPUT + "\n")

            else:

                confirm_password = maskpass.askpass(Prompts.INPUT_CONFIRM_PASSWORD)
                if input_password != confirm_password:
                    logger.debug("New password and Confirm password do not match.")
                    print(Prompts.PASSWORD_NOT_MATCH + "\n")
                    continue
                hashed_password = hashlib.sha256(confirm_password.encode('utf-8')).hexdigest()

                db.save_data_to_database(
                    QueryConfig.UPDATE_DEFAULT_PASSWORD,
                    (hashed_password, AppConfig.PERMANENT_PASSWORD, username)
                )
                logger.info("Password changed successfully.")
                print(Prompts.PASSWORD_CHANGE_SUCCESSFUL + "\n")
                break

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

