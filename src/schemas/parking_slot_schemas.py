"""Module containing request and response schema for parking slot resource."""

from marshmallow import Schema, fields, validate
from src.config.regex_pattern import RegexPattern
from src.schemas.base_schema import BaseSchema


class ParkingSlotSchema(BaseSchema):
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
    vehicle_type_name = fields.Str(required=True, validate=validate.Regexp(RegexPattern.TYPE_NAME_REGEX))
    parking_slot_no = fields.Str(required=True, validate=validate.Regexp(RegexPattern.PARKING_SLOT_NUMBER_REGEX))
    status = fields.Str(dump_only=True)

class ParkingSlotUpdateSchema(BaseSchema):
    success = fields.Bool(dump_only=True)
    message = fields.Str(dump_only=True)
    vehicle_type_name = fields.Str(required=True, validate=validate.Regexp(RegexPattern.TYPE_NAME_REGEX))
    new_status = fields.Str(required=True)

class ParkingSlotWriteResponseSchema(BaseSchema):
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
