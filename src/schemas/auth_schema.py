"""Module containing request and response schemas for authentication purpose."""

from marshmallow import Schema, fields, validate
from config.regex_pattern import RegexPattern

class LoginRequestSchema(Schema):
    """
        Schema for login request body.
        ...
        Fields
        ------
        username -> mandatory, str
        password -> mandatory, str
    """
    username = fields.Str(required=True, validate=validate.Regexp(RegexPattern.USERNAME_REGEX))
    password = fields.Str(required=True, load_only=True,
                            validate=validate.Regexp(RegexPattern.PASSWORD_PATTERN))

class LoginResponseSchema(Schema):
    """
        Schema for response after successful login.
        ...
        Fields
        ------
        success -> bool
        message -> str
        access_token -> str
        refresh_token -> str
    """
    success = fields.Bool(dump_only=True)
    message = fields.Str(dump_only=True)
    access_token = fields.Str(dump_only=True)
    refresh_token = fields.Str(dump_only=True)
    