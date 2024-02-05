class CustomBaseException(Exception):
    def __init__(self, error_code, error, message):
        super().__init__(message)
        self.error_code = error_code
        self.error = error
        self.message = message

class InvalidLogin(CustomBaseException):
    ...

class DBException(CustomBaseException):
    ...

class DataAlreadyExists(CustomBaseException):
    ...

class DataNotFound(CustomBaseException):
    ...

class InvalidRegex(CustomBaseException):
    ...
