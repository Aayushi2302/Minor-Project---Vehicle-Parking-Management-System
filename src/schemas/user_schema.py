from marshmallow import Schema, fields, validate
from config.regex_pattern import RegexPattern

class UserProfileSchema(Schema):
    success = fields.Bool(dump_only=True)
    message = fields.Str(dump_onlyt=True)
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
    success = fields.Bool(dump_only=True)
    message = fields.Str(dump_only=True)
    current_password = fields.Str(required=True, load_only=True, validate=validate.Regexp(RegexPattern.PASSWORD_PATTERN))
    new_password = fields.Str(required=True, load_only=True, validate=validate.Regexp(RegexPattern.PASSWORD_PATTERN))
    confirm_password = fields.Str(required=True, load_only=True, validate=validate.Regexp(RegexPattern.PASSWORD_PATTERN))
   
