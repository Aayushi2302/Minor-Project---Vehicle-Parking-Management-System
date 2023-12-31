"""
    Module for taking user login credentails as input.
    This module maintains a login attempts count for each user.
    Users are allowed only 3 valid login attempts.
"""
import logging
import time
import maskpass

from config.app_config import AppConfig
from config.log_prompts.log_prompts import LogPrompts
from config.prompts.prompts import Prompts
from controller.auth_controller import AuthController
from utils.common_helper import CommonHelper
from utils.decorators import looper
from views.admin_views import AdminViews

logger = logging.getLogger(__name__)

class AuthViews:
    """
        Class containing method for taking user login credentails as input.
        ...
        Attribute
        ---------
        max_login_attempts (private) -> Maximum login attempts with user for valid login (i.e. 3)

        Methods
        -------
        login() -> Method for taking login credentails as input.
    """

    def __init__(self) -> None:
        """
            Method for constructing auth views object.
            Parameters -> self
            Return type -> None
        """
        self.__max_login_attempts = AppConfig.MAXIMUM_LOGIN_ATTEMPTS
        self.auth_controller_obj = AuthController()
        self.common_helper_obj = CommonHelper()

    @looper
    def login(self) -> bool:
        """
            Method for taking user login credentails as input.
            Parameter -> self
            Return type -> bool
        """
        if not self.common_helper_obj.is_admin_registered():
            logger.info("Admin not found. Register Admin.")
            print(Prompts.NO_ADMIN_FOUND + "\n")
            admin_obj = AdminViews()
            admin_obj.employee_registration_form(AppConfig.ADMIN_ROLE)
            logger.info("Admin registered successfully.")

        if self.__max_login_attempts == 0:
            logger.warning("Login attempts exhausted. System in sleep for 10 seconds.")
            print(Prompts.LOGIN_ATTEMPTS_EXHAUSTED + "\n")
            self.__max_login_attempts = AppConfig.MAXIMUM_LOGIN_ATTEMPTS
            time.sleep(10)
            logger.info("System resumed for use.")
        else:
            logger.info("Enter login credentails.")
            print("\n" + Prompts.INPUT_CREDENTIAL)
            username = input(Prompts.INPUT_USERNAME).strip()
            password = maskpass.askpass(Prompts.INPUT_PASSWORD).strip()
            is_valid_user = self.auth_controller_obj.authenticate_user(username, password)

            if is_valid_user:
                logger.info("Resetting login attempts due to valid login.")
                self.__max_login_attempts = AppConfig.MAXIMUM_LOGIN_ATTEMPTS
            else:
                logger.warning("Reducing login attempts due to invalid login.")
                logger.warning(LogPrompts.INVALID_LOGIN_INFO)
                self.__max_login_attempts -= 1
                print(Prompts.LOGIN_ATTEMPTS_LEFT.format(self.__max_login_attempts) + "\n")

            choice = input(Prompts.EXIT_SYSTEM + "\n")
            if choice in ("Y", "y"):
                return True
        return False
