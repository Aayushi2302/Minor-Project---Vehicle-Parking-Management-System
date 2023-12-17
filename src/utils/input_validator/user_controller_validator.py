"""Module for validating user related inputs."""
import logging

from config.app_config import AppConfig
from config.prompts.prompts import Prompts
from config.regex_pattern import RegexPattern
from utils.common_helper import CommonHelper
from utils.decorators import looper

logger = logging.getLogger(__name__)

class UserControllerValidator:
    """
        This class contains methods for validating user realted input.
        ...
        Methods
        -------
        input_name() -> Method to take name as input.
        input_username() -> Method to take username as input.
        input_age() -> Method to take age as input.
        input_gender() -> Method to take gender as input.
        input_role() -> Method to take role as input.
        input_email_address() -> Method to take email address as input.
        input_mobile_number() -> Method to take mobile number as input.
    """
    @looper
    @staticmethod
    def input_name() -> str:
        """
            Validation of name using regular expression.
            Parameter -> None
            Return type -> str
        """
        name = input(Prompts.INPUT_NAME).strip()
        is_valid_name = CommonHelper.input_validation(RegexPattern.NAME_REGEX, name)
        if is_valid_name:
            return name.title()

    @looper
    @staticmethod
    def input_username() -> str:
        """
            Validation for username using regular expression.
            Parameter -> None
            Return type -> str
        """
        print(Prompts.USERNAME_FORMAT)
        username = input(Prompts.INPUT_USERNAME).strip()
        is_valid_username = CommonHelper.input_validation(RegexPattern.USERNAME_REGEX, username)
        if is_valid_username:
            return username.lower()

    @looper
    @staticmethod
    def input_age() -> int:
        """
            Validation of age.
            Parameter -> None
            Return type -> int
        """
        print("\n" + Prompts.AGE_RESTRICTION)
        age = input(Prompts.INPUT_EMPLOYEE_AGE)
        is_valid_age = CommonHelper.input_validation(RegexPattern.AGE_REGEX, age)
        if is_valid_age:
            return int(age)

    @looper
    @staticmethod
    def input_gender() -> str:
        """
            Validation of gender.
            Parameter -> None
            Return type -> str
        """
        gender = input(Prompts.INPUT_EMPLOYEE_GENDER).strip().capitalize()
        if gender == "F":
            return "Female"
        elif gender == "M":
            return "Male"
        else:
            logger.debug(Prompts.INVALID_INPUT)
            print(Prompts.INVALID_INPUT + "\n")

    @looper
    @staticmethod
    def input_role() -> str:
        """ 
            Validation of role using regular expression.
            Parameter -> role: Union[str, None]
            Return type -> str
        """
        input_role = input(Prompts.INPUT_EMPLOYEE_ROLE).strip().lower()
        if input_role == AppConfig.ADMIN_ROLE:
            print(Prompts.CANNOT_CREATE_ADMIN + "\n")
            return
        is_valid_role = CommonHelper.input_validation(RegexPattern.ROLE_REGEX, input_role)
        if is_valid_role:
            return input_role

    @looper
    @staticmethod
    def input_email_address() -> str:
        """
            Validation of email address using regular expression.
            Parameter -> None
            Return type -> str
        """
        email = input(Prompts.INPUT_EMPLOYEE_EMAIL).strip()
        is_valid_email = CommonHelper.input_validation(RegexPattern.EMAIL_REGEX, email)
        if is_valid_email:
            return email.lower()

    @looper
    @staticmethod
    def input_mobile_number() -> str:
        """
            Validation of phone number using regular expression.
            Parameter -> None
            Return type -> str
        """
        mobile_number = input(Prompts.INPUT_MOBILE_NUMBER).strip()
        is_valid_mobile_number =    CommonHelper.input_validation(
                                        RegexPattern.MOBILE_NO_REGEX,
                                        mobile_number
                                    )
        if is_valid_mobile_number:
            return mobile_number
