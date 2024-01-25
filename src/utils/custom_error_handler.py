from functools import wraps
from typing import Callable

from utils.custom_exceptions import CustomBaseException
from utils.responses import ErrorResponse

def custom_error_handler(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args: tuple, **kwargs: dict) -> None:
        try:
            return func(*args, **kwargs)
        except CustomBaseException as custom_error:
            return ErrorResponse.jsonify_error(custom_error), custom_error.error_code
    return wrapper
