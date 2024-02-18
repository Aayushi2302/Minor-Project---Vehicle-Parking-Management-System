"""Module containing request and response schema for vehicle type."""

from marshmallow import Schema, fields, validate
from marshmallow.validate import Range
from config.regex_pattern import RegexPattern

class VehicleTypeSchema(Schema):
    """
        Schema for vehicle type request or response body.
        ...
        Fields
        ------
        success : bool
        message : str
        type_id : str
        type_name : mandatory, str
        price_per_hour : mandatory, float
    """
    success = fields.Bool(dump_only=True)
    message = fields.Str(dump_only=True)
    vehicle_type_name = fields.Str(required=True, validate=validate.Regexp(RegexPattern.TYPE_NAME_REGEX))
    price_per_hour = fields.Float(required=True, validate=Range(min=10.0))

class VehicleTypeResponseSchema(Schema):
    """
        Schema for vehicle type response body.
        ...
        Fields
        ------
        success : bool
        message : str
    """ 
    success = fields.Bool(dump_only=True)
    message = fields.Str(dump_only=True)
