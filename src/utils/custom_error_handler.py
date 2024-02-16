"""
    Module containing custom error handler decorator for handling app related or db related exceptions
    raised from business and handled over controller.
"""

from functools import wraps
from typing import Callable

from src.utils.custom_exceptions import AppException, DBException
from src.utils.responses import ErrorResponse


def custom_error_handler(func: Callable) -> Callable:
    """
        Decorator that will handle app and db exceptions.
    """
    @wraps(func)
    def wrapper(*args: tuple, **kwargs: dict) -> tuple:
        """
            Function to return error raised along with message and status code.
        """
        try:
            return func(*args, **kwargs)
        except AppException as app_error:
            return ErrorResponse.jsonify_error(app_error), app_error.error_code
        except DBException as db_error:
            return ErrorResponse.jsonify_error(db_error), db_error.error_code
    return wrapper
