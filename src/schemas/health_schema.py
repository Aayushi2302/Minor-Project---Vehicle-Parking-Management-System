from marshmallow import fields
from src.schemas.base_schema import BaseSchema


class HealthSchema(BaseSchema):
    """
        Schema for checking whether the API is up.
        ...
        Fields
        ------
        success -> bool (response)
        message -> str (response)
    """
    success = fields.Bool(dump_only=True)
    message = fields.Str(dump_only=True)
