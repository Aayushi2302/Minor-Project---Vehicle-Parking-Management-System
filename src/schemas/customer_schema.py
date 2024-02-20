"""Module containing request and response schemas for customer related operations."""

from marshmallow import Schema, fields, validate

from src.config.regex_pattern import RegexPattern
from src.schemas.base_schema import BaseSchema


class CustomerSchema(BaseSchema):
    """
        Schema for employee request or response body.
        ...
        Fields
        ------
        success : bool
        message : str
        customer_id -> str
        name -> mandatory, str
        mobile_no ->  mandatory, str
        vehicle_no ->  mandatory, str
        type_name ->  mandatory, str
        status -> str
    """
    success = fields.Bool(dump_only=True)
    message = fields.Str(dump_only=True)
    customer_id = fields.Str(dump_only=True)
    name = fields.Str(required=True, validate=validate.Regexp(RegexPattern.NAME_REGEX))
    mobile_no = fields.Str(required=True, validate=validate.Regexp(RegexPattern.MOBILE_NO_REGEX))
    vehicle_no = fields.Str(required=True, validate=validate.Regexp(RegexPattern.VEHICLE_NUMBER_REGEX))
    vehicle_type_name = fields.Str(required=True, validate=validate.Regexp(RegexPattern.TYPE_NAME_REGEX))
    status = fields.Str(dump_only=True)

class CustomerUpdateSchema(BaseSchema):
    name = fields.Str(required=True, validate=validate.Regexp(RegexPattern.NAME_REGEX))
    mobile_no = fields.Str(required=True, validate=validate.Regexp(RegexPattern.MOBILE_NO_REGEX))
    vehicle_no = fields.Str(required=True, validate=validate.Regexp(RegexPattern.VEHICLE_NUMBER_REGEX))
    vehicle_type_name = fields.Str(required=True, validate=validate.Regexp(RegexPattern.TYPE_NAME_REGEX))

class CustomerResponseSchema(BaseSchema):
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

