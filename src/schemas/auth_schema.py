from marshmallow import Schema, fields, validate
from config.regex_pattern import RegexPattern

class LoginRequestSchema(Schema):
    username = fields.Str(required=True, validate=validate.Regexp(RegexPattern.USERNAME_REGEX))
    password = fields.Str(required=True, validate=validate.Regexp(RegexPattern.PASSWORD_PATTERN))

class LoginResponseSchema(Schema):
    access_token = fields.Str(dump_only=True)
    refresh_token = fields.Str(dump_only=True)
    message = fields.Str(dump_only=True)
