"""Module containing request and response schema for parking slot reservation."""

from marshmallow import Schema, fields, validate
from config.regex_pattern import RegexPattern


class SlotReservationSchema(Schema):
    """
        Schema for parking slot reservation request and response body.
        ...
        Fields
        ------
        success : bool
        message : str
        vehicle_no : mandatory, str
        out_date : mandatory, str
    """
    success = fields.Bool(dump_only=True)
    message = fields.Str(dump_only=True)
    vehicle_no = fields.Str(required=True, load_only=True, validate=validate.Regexp(RegexPattern.VEHICLE_NUMBER_REGEX))
    out_date = fields.Float(required=True, load_only=True)


class SlotReservationGetSchema(Schema):
    """
        Schema for response body of get operations on reservation.
        ...
        Fields
        ------
        success : bool
        message : str
        customer_id : str
        name : str
        mobile_no : str
        vehicle_no : str
        type_name : str
        booking_id : str
        parking_slot_no : str
        in_date : str
        in_time : str
        out_date : str
        out_time : str
        hours : float
        charges : float
    """
    success = fields.Bool(dump_only=True)
    message = fields.Str(dump_only=True)
    customer_id = fields.Str(dump_only=True)
    name = fields.Str(dump_only=True)
    mobile_no = fields.Str(dump_only=True)
    vehicle_no = fields.Str(dump_only=True)
    type_name = fields.Str(dump_only=True)
    booking_id = fields.Str(dump_only=True)
    parking_slot_no = fields.Str(dump_only=True)
    in_date = fields.Str(dump_only=True)
    in_time = fields.Str(dump_only=True)
    out_date = fields.Str(dump_only=True)
    out_time = fields.Str(dump_only=True)
    hours = fields.Float(dump_only=True)
    charges = fields.Float(dump_only=True)


class SlotVacateSchema(Schema):
    """
        Schema for request and response body for vacating parking slot.
        ...
        Fields
        ------
        success : bool
        message : str

    """
    success = fields.Bool(dump_only=True)
    message = fields.Str(dump_only=True)
    vehicle_no = fields.Str(required=True, load_only=True, validate=validate.Regexp(RegexPattern.VEHICLE_NUMBER_REGEX))
    hours = fields.Float(dump_only=True)
    charges = fields.Float(dump_only=True)
