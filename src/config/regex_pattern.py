""" Module that contains regex patterns for input validation."""

class RegexPattern:
    """Class containing regex patterns used throughout the project."""
    BOOKING_ID_REGEX = r"^BOOK[a-zA-Z0-9]+$"
    EMAIL_REGEX = r"^[a-z0-9]+@[a-z]+\.[a-z]{2,3}"
    MOBILE_NO_REGEX = r"[6-9][0-9]{9}$"
    NAME_REGEX = r"^[a-zA-Z]+(([',. -][a-zA-Z ])?[a-zA-Z]*)*$"
    PARKING_SLOT_NUMBER_REGEX = r"^PSN[0-9]+$"
    PASSWORD_PATTERN = r"^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[@#$%&]).{8,}$"
    ROLE_REGEX = r"^([a-z]){5,}$"
    STRING_REGEX = r"^[a-zA-Z]+\s*"
    TYPE_ID_REGEX = r"^TYPE[a-zA-Z0-9]+$"
    USERNAME_REGEX = r"(^user@)([a-z]{5,})"
    VEHICLE_NUMBER_REGEX = r"^[A-Z]{2}[-][0-9]{2}[-][A-Z]{2}[-][0-9]{4}$"
    AGE_REGEX = r"(^[1][4-9]$)|(^[2-5][0-9]$)|60"
    PRICE_REGEX = r"(^[0-9]+$)|([0-9]+\.[0-9]+$)"
    GENDER_REGEX = r"^(Male|Female|Other)$"
    