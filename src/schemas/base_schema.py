import typing

from marshmallow import Schema, ValidationError
from src.utils.custom_exceptions import AppException


class BaseSchema(Schema):
    def handle_error(
        self, error: ValidationError, data: typing.Any, *, many: bool, **kwargs
    ):
        raise AppException(422, "Unprocessable Entity", "Invalid request parameters.")