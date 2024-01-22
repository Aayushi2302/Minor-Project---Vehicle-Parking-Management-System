from marshmallow import Schema, fields, validate
from marshmallow.validate import Range
from config.regex_pattern import RegexPattern

class EmployeeSchema(Schema):
    emp_id = fields.Str(dump_only=True)
    name = fields.Str(required=True, validate=validate.Regexp(RegexPattern.NAME_REGEX))
    age = fields.Int(required=True, validate=Range(min=15, max=60, error="Age should be between 15 to 60."))
    gender = fields.Str(required=True, validate=validate.Regexp(RegexPattern.GENDER_REGEX))
    mobile_no = fields.Str(required=True, validate=validate.Regexp(RegexPattern.MOBILE_NO_REGEX))
    email_address = fields.Str(required=True, validate=validate.Regexp(RegexPattern.EMAIL_REGEX))
    username = fields.Str(required=True, validate=validate.Regexp(RegexPattern.USERNAME_REGEX))
    role = fields.Str(required=True, validate=validate.Regexp(RegexPattern.ROLE_REGEX))
    status = fields.Str(dump_only=True)