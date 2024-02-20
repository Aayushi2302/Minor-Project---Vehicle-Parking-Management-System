"""Module containing request and response schemas for refresh purpose."""

from marshmallow import Schema, fields
from src.schemas.base_schema import BaseSchema


class RefreshSchema(BaseSchema):
    """
        Schema for login request and response body.
        ...
        Fields
        ------
        success -> bool (response)
        message -> str (response)
        access_token -> str (response)
        refresh_token -> str (response)

    """
    success = fields.Bool(dump_only=True)
    message = fields.Str(dump_only=True)
    access_token = fields.Str(dump_only=True)
    refresh_token = fields.Str(dump_only=True)