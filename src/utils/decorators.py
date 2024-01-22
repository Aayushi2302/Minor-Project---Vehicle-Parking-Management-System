"""Module containing decorators used throughout the project."""
import logging
from mysql import connector
from typing import Callable
from functools import wraps
from flask_smorest import abort
from flask_jwt_extended import verify_jwt_in_request, get_jwt

from config.prompts.prompts import Prompts

logger = logging.getLogger(__name__)

def error_handler(func: Callable) -> Callable:
    """
        Decorator function for handling sqlite3 exceptions happening in project.
        Parameter -> function: Callable
        Return type -> wrapper: Callable
    """
    @wraps(func)
    def wrapper(*args: tuple, **kwargs: dict) -> None:
        """
            Wrapper function for executing the function and handling exception whenever occur.
            Parameter -> *args: tuple, **kwargs: dict
            Return type -> None
        """
        try:
            return func(*args, **kwargs)
        except connector.IntegrityError as error:
            logger.exception(error)
            print(Prompts.INTEGRITY_ERROR_MESSAGE + "\n")
            abort(409, message=Prompts.INTEGRITY_ERROR_MESSAGE)
        except connector.OperationalError as error:
            logger.exception(error)
            print(Prompts.OPERATIONAL_ERROR_MESSAGE + "\n")
            abort(500, message="Something wrong with the server. Please try again after some time.")
        except connector.ProgrammingError as error:
            logger.exception(error)
            print(Prompts.PROGRAMMING_ERROR_MESSAGE + "\n")
            abort(500, message="Something wrong with the server. Please try again after some time.")
        except connector.Error as error:
            logger.exception(error)
            print(Prompts.GENERAL_EXCEPTION_MESSAGE + "\n")
            abort(500, message="Something wrong with the server. Please try again after some time.")
    return wrapper

def looper(func: Callable) -> Callable:
    """
        Decorator function for making the func loop until a condition is satisfied.
        Parameter -> func: Callable
        Return type -> wrapper: Callable
    """
    @wraps(func)
    def wrapper(*args: tuple, **kwargs: tuple) -> bool | str | int:
        """
            Wrapper function to loop the function until function returns True.
            Parameter -> *args: tuple, **kwargs: dict
            Return type -> bool | str | int
        """
        logger.info("Entering into loop")
        while True:
            result = func(*args, **kwargs)
            if result:
                logger.info("Exiting from loop")
                return result
    return wrapper

def role_based_access(allowed_roles: tuple):
    def wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs):
            verify_jwt_in_request()
            claims = get_jwt()
            if claims["usr"] not in allowed_roles:
                abort(403, message="You don't have permission to access this functionality.")
            else:
                return func(*args, **kwargs)
        return inner
    return wrapper