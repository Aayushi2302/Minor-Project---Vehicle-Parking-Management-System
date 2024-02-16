from dataclasses import dataclass


@dataclass
class AppException(Exception):
    """Class containing properties associated with application level exception."""
    error_code: int
    error: str
    message: str


@dataclass
class DBException(Exception):
    """Class containing properties associated with db level exception."""
    error_code: int
    error: str
    message: str
