from functools import wraps
from flask_jwt_extended import verify_jwt_in_request, get_jwt

from utils.custom_exceptions import CustomBaseException
from utils.custom_error_handler import custom_error_handler

def role_based_access(allowed_roles: tuple):
    def wrapper(func):
        @wraps(func)
        @custom_error_handler
        def inner(*args, **kwargs):
            verify_jwt_in_request()
            claims = get_jwt()
            if claims["usr"] not in allowed_roles or claims["pty"] == 0:
                raise CustomBaseException(403, "Forbidden", "You don't have permission to access this functionality.")
            else:
                return func(*args, **kwargs)
        return inner
    return wrapper
