"""Module containing request and response schema for parking slot reservation."""

from datetime import datetime
from marshmallow import Schema, fields, validate, validates_schema
from src.config.regex_pattern import RegexPattern
from src.schemas.base_schema import BaseSchema
from src.utils.custom_exceptions import AppException


class SlotReservationSchema(BaseSchema):
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
    out_date = fields.Str(required=True, load_only=True)

    @validates_schema
    def validate_out_date(self, data):
        present = datetime.now().date()
        try:
            out_date = datetime.strptime(data["out_date"], "%d-%m-%Y").date()
            if out_date < present:
                raise AppException(422, "Unprocessable Entity", "You entered a date that has already passed.")
        except ValueError:
            raise AppException(422, "Unprocessable Entity", "Invalid date entered.")



class SlotReservationGetSchema(BaseSchema):
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


class SlotVacateSchema(BaseSchema):
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
