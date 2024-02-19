"""Module containing constants of the project."""

class AppConfig:
    """This class contains all the constants of the project."""
    # DATABASE_PATH = "models\\parking_management.db"
    # LOG_FILE_PATH = "logs.log"
    # PROMPTS_FILE_YAML_PATH = "config\\prompts\\prompts.yaml"

    import os
    current_directory = os.path.dirname(__file__)
    # PROMPTS_FILE_YAML_PATH = os.path.abspath(os.curdir) + "/config/prompts/prompts.yaml"
    PROMPTS_FILE_YAML_PATH = os.path.join(current_directory, './prompts/prompts.yaml')

    MAXIMUM_LOGIN_ATTEMPTS = 3
    # PROJECT_DB = "parking_management_system"

    BLP_DOC_PARAMETERS = {
                            'name': 'Authorization',
                            'in': 'header',
                            'description': 'Authorization: Bearer <access_token>',
                            'required': 'true'
                        }

    # constants for shortuuid
    VEHICLE_TYPE = "TYPE"
    
    # role specific constants
    ADMIN_ROLE = "admin"
    ATTENDANT_ROLE = "attendant"

    # status specific constants
    STATUS_ACTIVE = "active"
    STATUS_INACTIVE = "inactive"

    # parking_slot table status constants
    PARKING_SLOT_STATUS_VACANT = "vacant"
    PARKING_SLOT_STATUS_INACTIVE = "inactive"
    PARKING_SLOT_STATUS_DELETED = "deleted"
    PARKING_SLOT_STATUS_BOOKED = "booked"

    # password type specific constants
    DEFAULT_PASSWORD = "default"
    PERMANENT_PASSWORD = "permanent"

    # out time specific constants
    DEFAULT_OUT_TIME = "XX:XX"

    # database attributes specific constants
    NAME_ATTR = "name"
    MOBILE_NO_ATTR = "mobile_no"
    OUT_DATE_ATTR = "out_date"
    STATUS_ATTR = "status"
    AGE_ATTR = "age"
    GENDER_ATTR = "gender"
    EMAIL_ADDRESS_ATTR = "email_address"
    USERNAME_ATTR = "username"
    ROLE_ATTR = "role"
    PRICE_PER_HOUR_ATTR = "price_per_hour"
    TYPE_ID_ATTR = "type_id"
    TYPE_NAME_ATTR = "type_name",
    PRICE_PER_HOUR_ATTR = "price_per_hour"
    PARKING_SLOT_NO_ATTR = "parking_slot_no"

    # token status
    TOKEN_ISSUED = "issued"
    TOKEN_REVOKED = "revoked"

    # various HTTP status codes
    HTTP_STATUS_OK = 200
    HTTP_STATUS_CREATED = 201
    HTTP_STATUS_CONFLICT = 409
    HTTP_STATUS_NOT_FOUND = 404
    HTTP_STATUS_BAD_REQUEST = 400
    HTTP_STATUS_UNPROCESSABLE_ENTITY = 422
    HTTP_STATUS_INTERNAL_SERVER_ERROR = 500
    