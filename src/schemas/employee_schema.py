"""Module containing request and response schemas for employee related operations."""

from marshmallow import Schema, fields, validate
from marshmallow.validate import Range
from config.regex_pattern import RegexPattern


class EmployeeSchema(Schema):
    """
        Schema for employee request or response body.
        ...
        Fields
        ------
        success : bool
        message : str
        employee_id -> str
        name -> mandatory, str
        age ->  mandatory, int
        gender ->  mandatory, str
        mobile_no ->  mandatory, str
        email_address ->  mandatory, str
        username ->  mandatory, str
        role ->  mandatory, str
        status -> str
    """
    success = fields.Bool(dump_only=True)
    message = fields.Str(dump_only=True)
    emp_id = fields.Str(dump_only=True)
    name = fields.Str(required=True, validate=validate.Regexp(RegexPattern.NAME_REGEX))
    age = fields.Int(required=True, validate=Range(min=15, max=60, error="Age should be between 15 to 60."))
    gender = fields.Str(required=True, validate=validate.Regexp(RegexPattern.GENDER_REGEX))
    mobile_no = fields.Str(required=True, validate=validate.Regexp(RegexPattern.MOBILE_NO_REGEX))
    email_address = fields.Str(required=True, validate=validate.Regexp(RegexPattern.EMAIL_REGEX))
    username = fields.Str(required=True, validate=validate.Regexp(RegexPattern.USERNAME_REGEX))
    role = fields.Str(required=True, validate=validate.Regexp(RegexPattern.ROLE_REGEX))
    status = fields.Str(dump_only=True)


class EmployeeResponseSchema(Schema):
    """
        Schema for employee response body.
        ...
        Fields
        ------
        success : bool
        message : str
    """
    success = fields.Bool(dump_only=True)
    message = fields.Str(dump_only=True)


class EmployeeDefaultPasswordSchema(Schema):
    """
        Schema for default password response.
        ...
        Fields
        ------
        success -> bool
        message -> str
        default_password -> str
        password_type -> str
    """
    success = fields.Bool(dump_only=True)
    message = fields.Str(dump_only=True)
    default_password = fields.Str(dump_only=True)
    password_type = fields.Str(dump_only=True)
