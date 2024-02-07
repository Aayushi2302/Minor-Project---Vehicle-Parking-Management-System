"""Module containing request and response schema for parking slot resource."""

from marshmallow import Schema, fields, validate
from marshmallow.validate import Range
from src.config.regex_pattern import RegexPattern


class ParkingSlotSchema(Schema):
    """
        Schema for vehicle type request or response body.
        ...
        Fields
        ------
        success : bool
        message : str
        type_name : mandatory, str
        parking_slot_no : mandatory, str
        status : str
    """
    success = fields.Bool(dump_only=True)
    message = fields.Str(dump_only=True)
    type_name = fields.Str(required=True, validate=validate.Regexp(RegexPattern.TYPE_NAME_REGEX))
    parking_slot_no = fields.Float(required=True, validate=validate.Regexp(RegexPattern.PARKING_SLOT_NUMBER_REGEX))
    status = fields.Str(dump_only=True)


class ParkingSlotWriteResponseSchema(Schema):
    """
        Schema for parking slot response body.
        ...
        Fields
        ------
        success : bool
        message : str
    """
    success = fields.Bool(dump_only=True)
    message = fields.Str(dump_only=True)
