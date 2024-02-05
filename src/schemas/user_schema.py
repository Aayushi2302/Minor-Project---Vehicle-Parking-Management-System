"""Module contaning request and response schemas for user related operations."""

from marshmallow import Schema, fields, validate
from config.regex_pattern import RegexPattern

class UserProfileSchema(Schema):
    """
        Schema for user profile response body.
        ...
        Fields
        ------
        success -> bool
        message -> str
        employee_id -> str
        name -> str
        age -> int
        gender -> str
        mobile_no -> str
        email -> str
        username -> str
        role -> str
        status -> str
    """
    success = fields.Bool(dump_only=True)
    message = fields.Str(dump_onlyt=True)
    employee_id = fields.Str(dump_only=True)
    name = fields.Str(dump_only=True)
    age = fields.Int(dump_only=True)
    gender = fields.Str(dump_only=True)
    mobile_no = fields.Str(dump_only=True)
    email = fields.Str(dump_only=True)
    username = fields.Str(dump_only=True)
    role = fields.Str(dump_only=True)
    status = fields.Str(dump_only=True)

class ChangePasswordRequestSchema(Schema):
    """
        Schema for change password request body.
        ...
        Fields
        ------
        current_password -> mandatory, str
        new_password -> mandatory, str
    """
    current_password = fields.Str(required=True, load_only=True,
                                    validate=validate.Regexp(RegexPattern.PASSWORD_PATTERN))
    new_password = fields.Str(required=True, load_only=True,
                                    validate=validate.Regexp(RegexPattern.PASSWORD_PATTERN))

class ChangePasswordResponseSchema(Schema):
    """
        Schema for change password response body.
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
