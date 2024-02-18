"""Module containing decorator to check for various validations related to JWT on routes."""

from functools import wraps
from typing import Callable
from flask_jwt_extended import verify_jwt_in_request, get_jwt

from utils.custom_exceptions import AppException
from utils.custom_error_handler import custom_error_handler


def route_access(allowed_roles: tuple) -> Callable:
    """
        Function to check for validations related to JWT on routes.
        Parameters -> allowed_roles: tuple
        Returns -> Callable
    """
    def wrapper(func: Callable) -> Callable:
        """
            Function to check for validations related to JWT on routes.
            Parameters -> func: Callable
            Returns -> Callable
        """
        @wraps(func)
        @custom_error_handler
        def inner(*args: tuple, **kwargs: dict) -> list:
            """
                Function to check for validations related to JWT on routes.
                Parameters -> *args: tuple, **kwargs: dict
                Returns -> list
            """
            verify_jwt_in_request()
            claims = get_jwt()

            if claims["type"] == "refresh":
                raise AppException(401, "Unauthorized", "Wrong token supplied. Please provide a valid token.")

            if not claims["pty"] or claims["usr"] not in allowed_roles:
                raise AppException(403, "Forbidden", "You don't have permission to access this functionality.")
            else:
                return func(*args, **kwargs)

        return inner
    return wrapper
