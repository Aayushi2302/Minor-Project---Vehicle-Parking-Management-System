from marshmallow import Schema, fields, validate
from marshmallow.validate import Range
from config.regex_pattern import RegexPattern

class VehicleTypeSchema(Schema):
    success = fields.Bool(dump_only=True)
    message = fields.Str(dump_only=True)
    type_id = fields.Str(dump_only=True)
    type_name = fields.Str(required=True, validate=validate.Regexp(RegexPattern.TYPE_NAME_REGEX))
    price_per_hour = fields.Float(required=True, validate=Range(min=10.0))
