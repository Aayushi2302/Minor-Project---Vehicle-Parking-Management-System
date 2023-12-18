"""
    Module for authenticating users(both admin and employee) based on their credentials.
    The user password is stored in hashed format.
    The default password of the user is changed on 1st login of user.
"""
import hashlib
import logging

from config.app_config import AppConfig
from config.log_prompts.log_prompts import LogPrompts
from config.query import QueryConfig
from models.database import db
from utils.common_helper import CommonHelper
from views.admin_views import AdminViews
from views.employee_views import EmployeeViews

logger = logging.getLogger('auth_controller')

class AuthController:
    """
        Class containing methods for authenticating user based on their credentails.
        This class also grant role based access to user.
        ...
        Methods
        -------
        valid_first_login() -> Method for granting access to user on 1st login.
        role_based_access() -> Method for granting role based access to user based on credentails.
        authenticate_user() -> Method for validating user based on credentials.
    """
    def __init__(self):
        self.common_helper_obj = CommonHelper()

    def valid_first_login(self, username: str, password: str, actual_password: str) -> bool:
        """
            Method for changing default password on first valid login.
            Parameter -> self, username: str, password: str, actual_password: str
            Return type -> bool
        """
        logger.info(LogPrompts.FIRST_LOGIN_INFO)
        if actual_password != password:
            return False
        else:
            self.common_helper_obj.create_new_password(username)
            return True

    def role_based_access(self, role: str, username: str) -> bool:
        """
            Method to assign role to user based on the credentials after authentication.
            Parameter -> self, role: str, username: str
            Return type -> bool
        """  
        if role == AppConfig.ADMIN_ROLE:
            admin_views_obj = AdminViews(username)
            admin_views_obj.admin_menu()
            return True
        elif role == AppConfig.ATTENDANT_ROLE:
            employee_handler_obj = EmployeeViews(username)
            employee_handler_obj.employee_menu()
            return True
        else:
            return False
    
    def authenticate_user(self, username: str, password: str) -> bool:
        """
            Method for validating user based on credentials.
            Parameter -> username: str, password: str
            Return type -> bool
        """
        data =  db.fetch_data_from_database(
                    QueryConfig.FETCH_EMPLOYEE_CREDENTIALS,
                    (username, AppConfig.STATUS_ACTIVE)
                )
        if data:
            actual_password = data[0][0]
            role = data[0][1]
            password_type = data[0][2]
            if password_type == AppConfig.DEFAULT_PASSWORD:
                return self.valid_first_login(username, password, actual_password)
            else:
                hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
                if hashed_password == actual_password:
                    return self.role_based_access(role, username)
        return False
                    