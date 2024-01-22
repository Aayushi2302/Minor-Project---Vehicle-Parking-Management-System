from marshmallow import Schema, fields, validate
from config.regex_pattern import RegexPattern

class UserProfileSchema(Schema):
    employee_id = fields.Str(dump_only=True)
    name = fields.Str(dump_only=True)
    age = fields.Int(dump_only=True)
    gender = fields.Str(dump_only=True)
    mobile_no = fields.Str(dump_only=True)
    email = fields.Str(dump_only=True)
    username = fields.Str(dump_only=True)
    role = fields.Str(dump_only=True)
    status = fields.Str(dump_only=True)

class ChangePasswordSchema(Schema):
    new_password = fields.Str(load_only=True, validate=validate.Regexp(RegexPattern.PASSWORD_PATTERN))
    confirm_password = fields.Str(load_only=True, validate=validate.Regexp(RegexPattern.PASSWORD_PATTERN))
    message = fields.Str(dump_only=True)