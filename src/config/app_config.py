"""Module containing constants of the project."""

class AppConfig:
    """This class contains all the constants of the project."""
    DATABASE_PATH = "src\\models\\parking_management.db"
    LOG_FILE_PATH = "logs.log"
    PROMPTS_FILE_YAML_PATH = "src\\config\\prompts\\prompts.yaml"
    LOG_FILE_YAML_PATH = "src\\config\\log_prompts\\log_prompts.yaml"
    MAXIMUM_LOGIN_ATTEMPTS = 3
    
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
    