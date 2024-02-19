"""Module containing common helper methods which are shared across the project."""
from datetime import datetime
import hashlib
import logging
import re
import string
import random
import pytz
import shortuuid
from tabulate import tabulate

from src.config.regex_pattern import RegexPattern
from src.config.app_config import AppConfig
from src.config.prompts.prompts import Prompts
from src.config.query import QueryConfig
from src.models.database import db

logger = logging.getLogger(__name__)


def is_admin_registered() -> bool:
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


def hash_password(password: str) -> str:
    hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
    return hashed_password


def regex_validation(regular_exp: str, input_field: str) -> bool:
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
        logger.debug("Invalid input entered.")
        return False


def get_current_date_and_time() -> dict:
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
    return {
        "date": curr_date,
        "time": curr_time
    }


def generate_shortuuid(prefix: str) -> str:
    id = prefix + shortuuid.ShortUUID().random(length=5)
    return id


def generate_random_password() -> str:
    emp_password = ""
    while not regex_validation(RegexPattern.PASSWORD_PATTERN, emp_password):
        characters = string.ascii_letters + string.digits + "@#$&%"
        emp_password = ''.join(random.choice(characters) for _ in range(8))
    return emp_password


def get_constraint_failed_attribute(error_msg: str) -> str:
    msg = error_msg.split(" ")
    msg = msg[-1].strip("'")
    msg = msg.split(".")[-1]
    error_column = msg.replace("_", " ").capitalize()
    return error_column

