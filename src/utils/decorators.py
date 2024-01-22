"""Module containing decorators used throughout the project."""
from flask_smorest import abort
from functools import wraps
import logging
import sqlite3
from typing import Callable

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
        except sqlite3.IntegrityError as error:
            logger.exception(error)
            print(Prompts.INTEGRITY_ERROR_MESSAGE + "\n")
            abort(409, message=Prompts.INTEGRITY_ERROR_MESSAGE)
        except sqlite3.OperationalError as error:
            logger.exception(error)
            print(Prompts.OPERATIONAL_ERROR_MESSAGE + "\n")
            abort(500, message="Something wrong with the server. Please try again after some time.")
        except sqlite3.ProgrammingError as error:
            logger.exception(error)
            print(Prompts.PROGRAMMING_ERROR_MESSAGE + "\n")
            abort(500, message="Something wrong with the server. Please try again after some time.")
        except sqlite3.Error as error:
            logger.exception(error)
            print(Prompts.GENERAL_EXCEPTION_MESSAGE + "\n")
            abort(500, message="Something wrong with the server. Please try again after some time.")
        except Exception as error:
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
    