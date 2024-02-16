"""Module containing request and response schemas for authentication purpose."""

from marshmallow import Schema, fields, validate
from src.config.regex_pattern import RegexPattern


class LoginSchema(Schema):
    """
        Schema for login request and response body.
        ...
        Fields
        ------
        username -> mandatory, str (request)
        password -> mandatory, str (request)
        success -> bool (response)
        message -> str (response)
        access_token -> str (response)
        refresh_token -> str (response)

    """
    username = fields.Str(required=True, load_only=True,
                          validate=validate.Regexp(RegexPattern.USERNAME_REGEX))
    password = fields.Str(required=True, load_only=True,
                          validate=validate.Regexp(RegexPattern.PASSWORD_PATTERN))
    success = fields.Bool(dump_only=True)
    message = fields.Str(dump_only=True)
    access_token = fields.Str(dump_only=True)
    refresh_token = fields.Str(dump_only=True)


# class LoginResponseSchema(Schema):
#     """
#         Schema for response after successful login.
#         ...
#         Fields
#         ------
#         success -> bool
#         message -> str
#         access_token -> str
#         refresh_token -> str
#     """
#     success = fields.Bool(dump_only=True)
#     message = fields.Str(dump_only=True)
#     access_token = fields.Str(dump_only=True)
#     refresh_token = fields.Str(dump_only=True)
