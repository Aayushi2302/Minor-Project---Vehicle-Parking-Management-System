"""
    Module for validating user related inputs.
"""
import re
import logging 

from config.statements.config import Config
from logs.logs_config import LogConfig

NAME_REGEX = r"^([A-Za-z]{2,25}\s*)"
EMAIL_REGEX = r"^[a-z0-9]+@[a-z]+\.[a-z]{2,3}"
USERNAME_REGEX = r"(^user@)([a-z]{5,})"
ROLE_REGEX = r"^([a-z]){5,}$"
MOBILE_NO_REGEX = r"[6-9][0-9]{9}$"

logger = logging.getLogger('validations')

def error_handling_input(func):
    """
        decorator for input validation and error handling during customer registration
    """
    def wrapper(*args, **kwargs):
        try:
            res = func(*args, **kwargs)
            if res == False:
                raise Exception
        except:
            logger.debug(LogConfig.invalid_input_exception_prompt)
            print(Config.invalid_input_prompt + "\n")
        finally:
            return res
    return wrapper
    
@error_handling_input
def input_validation(regular_exp, input_field) -> bool:
    """
        Function to validate input on basis of regex.
    """
    r = re.match(regular_exp, input_field) 
    if r != None:
        return True
    else:
        return False

class UserInputValidation:
    @staticmethod
    def input_name() -> str:
        """
            validation of name using regular expression
        """
        while True:
            name = input(Config.input_name_prompt).strip()
            check = input_validation(NAME_REGEX, name)
            if check:
                return name.title()

    @staticmethod
    def input_username() -> str:
        """
            validation for username using regular expression
        """
        while True:
            print(Config.username_format_prompt)
            username = input(Config.input_username_prompt).strip()
            check = input_validation(USERNAME_REGEX, username)
            if check:
                return username.lower()
            
    @staticmethod
    def input_age() -> int:
        """
            validation of age
        """
        while True:
            try:
                age = int(input(Config.input_employee_age_prompt))
                if age > 60 or age < 15:
                    print(Config.age_restriction_prompt + "\n")
                    continue
                return age
            except Exception as e:
                logger.debug(e)
                print(Config.number_input_prompt.format("Age") + "\n")

    @staticmethod
    def input_gender() -> str:
        """
            validation of gender
        """
        while True:
            try:
                gender = input(Config.input_employee_gender_prompt).strip().capitalize()
                if gender == "F":
                    return "Female"
                elif gender == "M":
                    return "Male"
                else:
                    raise Exception
            except:
                print(Config.invalid_input_prompt)
    
    @staticmethod
    def input_role() -> str:
        """
            validation of role using regular expression
        """
        while True:
            role = input(Config.input_employee_role_prompt).strip().lower()
            check = input_validation(ROLE_REGEX, role)
            if role == "admin":
                print(Config.cannot_create_admin_prompt + "\n")
                continue
            if check:
                return role
            
    @staticmethod
    def input_email_address() -> str:
        """
            validation of email address using regular expression
        """
        while True:
            email = input(Config.input_employee_email_prompt).strip()
            check = input_validation(EMAIL_REGEX, email)
            if check:
                return email.lower()

    @staticmethod
    def input_mobile_number() -> str:
        """
            validation of phone number using regular expression
        """
        while True:
            mobile_number = input(Config.employee_mobile_no_input_prompt).strip()
            check = input_validation(MOBILE_NO_REGEX, mobile_number)
            if check:
                return mobile_number