"""
    Module for authenticating users(both admin and employee) based on their credentials.
    The user password is stored in hashed format.
    The default password of the user is changed on 1st login of user.
"""
import logging

from business.auth_business import AuthBusiness
from models.database import db
from tokens.token import Token
from utils.custom_error_handler import custom_error_handler
from utils.responses import SuccessResponse

logger = logging.getLogger(__name__)

class LoginController:

    @custom_error_handler
    def user_login(self, credentials):
        token_obj = Token()
        auth_business_obj = AuthBusiness(db, token_obj)
        username = credentials["username"]
        password = credentials["password"]
        data = auth_business_obj.authenticate_user(username, password)
        return SuccessResponse.jsonify_data("User loggedin successfully.", data), 200
