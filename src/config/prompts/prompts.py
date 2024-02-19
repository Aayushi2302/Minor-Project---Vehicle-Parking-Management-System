"""Module for loading prompts of project."""
import yaml

from src.config.app_config import AppConfig

class Prompts:
    """
        This class contains methods for loading prompts from yaml file.
        ...
        Methods
        -------
        load() -> None:
            This method loads the variables from yaml to py.
    """
    EMP_ID_HEADER = None
    NAME_HEADER = None
    AGE_HEADER = None
    GENDER_HEADER = None
    MOBILE_NO_HEADER = None
    EMAIL_ADDRESS_HEADER = None
    USERNAME_HEADER = None
    ROLE_HEADER = None
    STATUS_HEADER = None
    CUSTOMER_ID_HEADER = None
    VEHICLE_NO_HEADER = None
    VEHICLE_TYPE_NAME_HEADER = None
    PARKING_SLOT_NO_HEADER = None
    VEHICLE_TYPE_HEADER = None
    BOOKING_ID_HEADER = None
    IN_DATE_HEADER = None
    IN_TIME_HEADER = None
    OUT_DATE_HEADER = None
    OUT_TIME_HEADER = None
    HOURS_HEADER = None
    CHARGES_HEADER = None
    VEHICLE_TYPE_ID = None
    PRICE_PER_HOUR = None
    WELCOME_MESSAGE = None
    EXIT_MESSAGE = None
    ENTER_CHOICE = None
    INVALID_INPUT = None
    INPUT_USERNAME = None
    INPUT_NAME = None
    INPUT_MOBILE_NUMBER = None
    ZERO_RECORD = None
    DETAILS_NOT_EXIST = None
    NEW_DETAIL_INPUT = None
    SUCCESSFUL_LOGOUT = None
    CANNOT_PERFORM_UPDATION = None
    CANNOT_PERFORM_DELETION = None
    CANNOT_UPDATE_RECORD = None
    CANNOT_DEACTIVATE = None
    INPUT_CREDENTIAL = None
    INPUT_PASSWORD = None
    SUCCESSFUL_LOGIN = None
    LOGIN_ATTEMPTS_LEFT= None
    LOGIN_ATTEMPTS_EXHAUSTED = None
    CHANGE_PASSWORD = None
    INPUT_NEW_PASSWORD = None
    INPUT_CONFIRM_PASSWORD = None
    PASSWORD_NOT_MATCH = None
    PASSWORD_CHANGE_SUCCESSFUL = None
    NO_ADMIN_FOUND = None
    INPUT_EMPLOYEE_DETAILS = None
    INPUT_EMPLOYEE_AGE = None
    INPUT_EMPLOYEE_GENDER = None
    INPUT_EMPLOYEE_ROLE = None
    INPUT_EMPLOYEE_EMAIL = None
    USER_ALREADY_EXIST = None
    EMPLOYEE_REGISTRATION_SUCCESSFUL = None
    NO_DEFAULT_PASSWORD = None
    PRINT_DEFAULT_PASSWORD = None
    INPUT_DETAILS_FOR_REMOVAL = None
    UPDATE_DETAILS_FOR_INACTIVE_STATUS = None
    EMPLOYEE_REMOVAL_SUCCESSFUL = None
    INPUT_DETAILS_FOR_UPDATION = None
    EMPLOYEE_UPDATION_SUCCESSFUL = None
    CREATE_USER_CREDENTIALS = None
    NOT_VALID_USERNAME = None
    NOT_VALID_ROLE = None
    DETAILS_FOR_GIVEN_EMPLOYEE = None
    CANNOT_INPUT_PAST_DATE = None
    CANNOT_REMOVE_ADMIN = None
    CANNOT_UPDATE_ADMIN = None
    USERNAME_FORMAT = None
    CANNOT_CREATE_ADMIN = None
    AGE_RESTRICTION = None
    NUMBER_INPUT = None
    VEHICLE_NUMBER_FORMAT = None
    STRONG_PASSWORD_REQUIREMENTS = None
    WEAK_PASSWORD_INPUT = None
    INPUT_TYPE_NAME = None
    INPUT_PRICE = None
    VEHICLE_TYPE_REGISTRATION_SUCCESSFUL = None
    VEHICLE_TYPE_DETAILS_UPDATION_SUCCESSFUL = None
    VEHICLE_TYPE_REMOVAL_SUCCESSFUL = None
    INPUT_TYPE_ID = None
    VEHICLE_TYPE_DOES_NOT_EXIST = None
    VEHCILE_TYPE_ALREADY_EXIST = None
    TYPEID_DOES_NOT_EXIST = None
    CURRENT_PRICE_PER_HOUR = None
    INPUT_PARKING_SLOT_NUMBER = None
    PARKING_SLOT_REGISTRATION_SUCCESSFUL = None
    PARKING_SLOT_ACTIVATION_SUCCESSFUL = None
    PARKING_SLOT_UPDATION_SUCCESSFUL = None
    PARKING_SLOT_REMOVAL_SUCCESSFUL = None
    PARKING_SLOT_NUMBER_ALREADY_EXIST = None
    PARKING_SLOT_NUMBER_DOES_NOT_EXIST = None
    PARKING_SLOT_DEACTIVATION_SUCCESSFUL = None
    PARKING_SLOT_DELETION_SUCCESSFUL = None
    PARKING_SLOT_ALREADY_VACANT = None
    PARKING_SLOT_INACTIVE = None
    PARKING_SLOT_DELETED = None
    CANNOT_VACATE_PARKING_SLOT = None
    INPUT_DETAIL_TO_VACATE_PARKING_SLOT = None
    CUSTOMER_DETAILS_INPUT = None
    VEHICLE_NUMBER_INPUT = None
    CUSTOMER_CREATION_SUCCESSFUL = None
    CUSTOMER_ALREADY_EXIST = None
    CUSTOMER_DOES_NOT_EXIST = None
    CUSTOMER_UPDATION_SUCCESSFUL = None
    CUSTOMER_OUT_DATE_INPUT = None
    INPUT_DETAILS_FOR_SLOT_BOOKING = None
    VEHCILE_NO_NOT_FOUND = None
    PARKING_SLOT_ASSIGNED = None
    BOOKING_RECORD_NOT_FOUND = None
    NO_UPDATION_FOR_CHECKOUT_VEHICLE = None
    SLOT_BOOKING_UPDATION_SUCCESSFUL = None
    INPUT_BOOKING_ID = None
    PARKING_SLOT_VACANT = None
    VEHICLE_ALREADY_VACATE_PARKING_SLOT = None
    PRINT_PARKING_CHARGES = None
    INTEGRITY_ERROR_MESSAGE = None
    OPERATIONAL_ERROR_MESSAGE = None
    PROGRAMMING_ERROR_MESSAGE = None
    GENERAL_EXCEPTION_MESSAGE = None
    ADMIN_MENU_WELCOME_MESSAGE = None
    EMPLOYEE_MENU_WELCOME_MESSAGE = None
    PRESS_KEY_TO_CONTINUE = None
    EXIT_SYSTEM = None
    ADMIN_MENU = None
    MANAGE_PROFILE_MENU = None
    EMPLOYEE_DETAIL_UPDATE_MENU = None
    MANAGE_VEHICLE_TYPE_MENU = None
    MANAGE_PARKING_SLOT_MENU = None
    EMPLOYEE_MENU = None
    CUSTOMER_DETAIL_UPDATE_MENU = None
    VIEW_PARKING_STATUS_MENU = None
    CANNOT_VIEW_RECORD = None

    # API Prompts starts here
    ERROR_STATUS_400 = None
    ERROR_STATUS_409 = None
    ERROR_STATUS_404 = None
    ERROR_STATUS_500 = None
    VEHICLE_TYPE_CONFLICT_MSG = None
    INTERNAL_SERVER_ERROR_MSG = None
    VEHICLE_TYPE_NOT_FOUND = None
    VEHICLE_TYPE_REGISTER_SUCCESS = None
    VEHICLE_TYPE_GET_SUCCESS = None
    CANNOT_UPDATE_VEHICLE_TYPE_NAME = None
    VEHICLE_TYPE_UPDATE_SUCCESS = None
    ERROR_STATUS_422 = None
    VEHICLE_TYPE_ID_REGEX_INVALID = None
    PARKING_SLOT_CONFLICT_MSG = None
    PARKING_SLOT_NOT_FOUND = None
    PARKING_SLOT_REGISTER_SUCCESS = None
    PARKING_SLOT_GET_SUCCESS = None
    PARKING_SLOT_UPDATE_SUCCESS = None
    PARKING_SLOT_DELETE_SUCCESS = None
    
    @classmethod
    def load(cls) -> None:
        """
            Method to load variables from yaml to py
            Parameters = cls
            Return Type = None
        """
        with open(AppConfig.PROMPTS_FILE_YAML_PATH, "r") as file:
            data = yaml.safe_load(file)
        
        # ---- table header constants ----
        cls.EMP_ID_HEADER = data["EMP_ID_HEADER"]
        cls.NAME_HEADER = data["NAME_HEADER"]
        cls.AGE_HEADER = data["AGE_HEADER"]
        cls.GENDER_HEADER = data["GENDER_HEADER"]
        cls.MOBILE_NO_HEADER = data["MOBILE_NO_HEADER"]
        cls.EMAIL_ADDRESS_HEADER = data["EMAIL_ADDRESS_HEADER"]
        cls.USERNAME_HEADER = data["USERNAME_HEADER"]
        cls.ROLE_HEADER = data["ROLE_HEADER"]
        cls.STATUS_HEADER = data["STATUS_HEADER"]
        cls.CUSTOMER_ID_HEADER = data["CUSTOMER_ID_HEADER"]
        cls.VEHICLE_NO_HEADER = data["VEHICLE_NO_HEADER"]
        cls.VEHICLE_TYPE_NAME_HEADER = data["VEHICLE_TYPE_NAME_HEADER"]
        cls.PARKING_SLOT_NO_HEADER = data["PARKING_SLOT_NO_HEADER"]
        cls.VEHICLE_TYPE_HEADER = data["VEHICLE_TYPE_HEADER"]
        cls.BOOKING_ID_HEADER = data["BOOKING_ID_HEADER"]
        cls.IN_DATE_HEADER = data["IN_DATE_HEADER"]
        cls.IN_TIME_HEADER = data["IN_TIME_HEADER"]
        cls.OUT_DATE_HEADER = data["OUT_DATE_HEADER"]
        cls.OUT_TIME_HEADER = data["OUT_TIME_HEADER"]
        cls.HOURS_HEADER = data["HOURS_HEADER"]
        cls.CHARGES_HEADER = data["CHARGES_HEADER"]
        cls.VEHICLE_TYPE_ID = data["VEHICLE_TYPE_ID"]
        cls.PRICE_PER_HOUR = data["PRICE_PER_HOUR"]

        # ---- prompts - input and print statements ----
        cls.WELCOME_MESSAGE = data["WELCOME_MESSAGE"]
        cls.EXIT_MESSAGE = data["EXIT_MESSAGE"]

        # common prompts
        cls.ENTER_CHOICE = data["ENTER_CHOICE"]
        cls.INVALID_INPUT = data["INVALID_INPUT"]
        cls.INPUT_USERNAME = data["INPUT_USERNAME"]
        cls.INPUT_NAME = data["INPUT_NAME"]
        cls.INPUT_MOBILE_NUMBER = data["INPUT_MOBILE_NUMBER"]
        cls.ZERO_RECORD = data["ZERO_RECORD"]
        cls.DETAILS_NOT_EXIST = data["DETAILS_NOT_EXIST"]
        cls.NEW_DETAIL_INPUT = data["NEW_DETAIL_INPUT"]
        cls.SUCCESSFUL_LOGOUT = data["SUCCESSFUL_LOGOUT"]
        cls.CANNOT_PERFORM_UPDATION = data["CANNOT_PERFORM_UPDATION"]
        cls.CANNOT_PERFORM_DELETION = data["CANNOT_PERFORM_DELETION"]
        cls.CANNOT_UPDATE_RECORD = data["CANNOT_UPDATE_RECORD"]
        cls.CANNOT_DEACTIVATE = data["CANNOT_DEACTIVATE"]
        cls.CANNOT_VIEW_RECORD = data["CANNOT_VIEW_RECORD"]

        # authentication module prompts
        cls.INPUT_CREDENTIAL = data["INPUT_CREDENTIAL"]
        cls.INPUT_PASSWORD = data["INPUT_PASSWORD"]
        cls.SUCCESSFUL_LOGIN = data["SUCCESSFUL_LOGIN"]
        cls.LOGIN_ATTEMPTS_LEFT= data["LOGIN_ATTEMPTS_LEFT"]
        cls.LOGIN_ATTEMPTS_EXHAUSTED = data["LOGIN_ATTEMPTS_EXHAUSTED"]
        cls.CHANGE_PASSWORD = data["CHANGE_PASSWORD"]
        cls.INPUT_NEW_PASSWORD = data["INPUT_NEW_PASSWORD"]
        cls.INPUT_CONFIRM_PASSWORD = data["INPUT_CONFIRM_PASSWORD"]
        cls.PASSWORD_NOT_MATCH = data["PASSWORD_NOT_MATCH"]
        cls.PASSWORD_CHANGE_SUCCESSFUL = data["PASSWORD_CHANGE_SUCCESSFUL"]
        cls.NO_ADMIN_FOUND = data["NO_ADMIN_FOUND"]
        cls.EXIT_SYSTEM = data["EXIT_SYSTEM"]

        # admin_controller module prompts
        cls.INPUT_EMPLOYEE_DETAILS = data["INPUT_EMPLOYEE_DETAILS"]
        cls.INPUT_EMPLOYEE_AGE = data["INPUT_EMPLOYEE_AGE"]
        cls.INPUT_EMPLOYEE_GENDER = data["INPUT_EMPLOYEE_GENDER"]
        cls.INPUT_EMPLOYEE_ROLE = data["INPUT_EMPLOYEE_ROLE"]
        cls.INPUT_EMPLOYEE_EMAIL = data["INPUT_EMPLOYEE_EMAIL"]
        cls.USER_ALREADY_EXIST = data["USER_ALREADY_EXIST"]
        cls.EMPLOYEE_REGISTRATION_SUCCESSFUL = data["EMPLOYEE_REGISTRATION_SUCCESSFUL"]
        cls.NO_DEFAULT_PASSWORD = data["NO_DEFAULT_PASSWORD"]
        cls.PRINT_DEFAULT_PASSWORD = data["PRINT_DEFAULT_PASSWORD"]
        cls.INPUT_DETAILS_FOR_REMOVAL = data["INPUT_DETAILS_FOR_REMOVAL"]
        cls.UPDATE_DETAILS_FOR_INACTIVE_STATUS = data["UPDATE_DETAILS_FOR_INACTIVE_STATUS"]
        cls.EMPLOYEE_REMOVAL_SUCCESSFUL = data["EMPLOYEE_REMOVAL_SUCCESSFUL"]
        cls.INPUT_DETAILS_FOR_UPDATION = data["INPUT_DETAILS_FOR_UPDATION"]
        cls.EMPLOYEE_UPDATION_SUCCESSFUL = data["EMPLOYEE_UPDATION_SUCCESSFUL"]
        cls.CREATE_USER_CREDENTIALS = data["CREATE_USER_CREDENTIALS"]
        cls.NOT_VALID_USERNAME = data["NOT_VALID_USERNAME"]
        cls.NOT_VALID_ROLE = data["NOT_VALID_ROLE"]
        cls.DETAILS_FOR_GIVEN_EMPLOYEE = data["DETAILS_FOR_GIVEN_EMPLOYEE"]
        cls.CANNOT_INPUT_PAST_DATE = data["CANNOT_INPUT_PAST_DATE"]
        cls.CANNOT_REMOVE_ADMIN = data["CANNOT_REMOVE_ADMIN"]
        cls.CANNOT_UPDATE_ADMIN = data["CANNOT_UPDATE_ADMIN"]

        # validator modules prompts
        cls.USERNAME_FORMAT = data["USERNAME_FORMAT"]
        cls.CANNOT_CREATE_ADMIN = data["CANNOT_CREATE_ADMIN"]
        cls.AGE_RESTRICTION = data["AGE_RESTRICTION"]
        cls.NUMBER_INPUT = data["NUMBER_INPUT"]
        cls.VEHICLE_NUMBER_FORMAT = data["VEHICLE_NUMBER_FORMAT"]

        # helpers module prompts
        cls.STRONG_PASSWORD_REQUIREMENTS = data["STRONG_PASSWORD_REQUIREMENTS"]
        cls.WEAK_PASSWORD_INPUT = data["WEAK_PASSWORD_INPUT"]

        # vehicle_type module prompts
        cls.INPUT_TYPE_NAME = data["INPUT_TYPE_NAME"]
        cls.INPUT_PRICE = data["INPUT_PRICE"]
        cls.VEHICLE_TYPE_REGISTRATION_SUCCESSFUL = data["VEHICLE_TYPE_REGISTRATION_SUCCESSFUL"]
        cls.VEHICLE_TYPE_DETAILS_UPDATION_SUCCESSFUL = data["VEHICLE_TYPE_DETAILS_UPDATION_SUCCESSFUL"]
        cls.VEHICLE_TYPE_REMOVAL_SUCCESSFUL = data["VEHICLE_TYPE_REMOVAL_SUCCESSFUL"]
        cls.INPUT_TYPE_ID = data["INPUT_TYPE_ID"]
        cls.VEHICLE_TYPE_DOES_NOT_EXIST = data["VEHICLE_TYPE_DOES_NOT_EXIST"]
        cls.VEHCILE_TYPE_ALREADY_EXIST = data["VEHCILE_TYPE_ALREADY_EXIST"]
        cls.TYPEID_DOES_NOT_EXIST = data["TYPEID_DOES_NOT_EXIST"]
        cls.CURRENT_PRICE_PER_HOUR = data["CURRENT_PRICE_PER_HOUR"]

        # parking_slot module prompts
        cls.INPUT_PARKING_SLOT_NUMBER = data["INPUT_PARKING_SLOT_NUMBER"]
        cls.PARKING_SLOT_REGISTRATION_SUCCESSFUL = data["PARKING_SLOT_REGISTRATION_SUCCESSFUL"]
        cls.PARKING_SLOT_ACTIVATION_SUCCESSFUL = data["PARKING_SLOT_ACTIVATION_SUCCESSFUL"]
        cls.PARKING_SLOT_UPDATION_SUCCESSFUL = data["PARKING_SLOT_UPDATION_SUCCESSFUL"]
        cls.PARKING_SLOT_REMOVAL_SUCCESSFUL = data["PARKING_SLOT_REMOVAL_SUCCESSFUL"]
        cls.PARKING_SLOT_NUMBER_ALREADY_EXIST = data["PARKING_SLOT_NUMBER_ALREADY_EXIST"]
        cls.PARKING_SLOT_NUMBER_DOES_NOT_EXIST = data["PARKING_SLOT_NUMBER_DOES_NOT_EXIST"]
        cls.PARKING_SLOT_DEACTIVATION_SUCCESSFUL = data["PARKING_SLOT_DEACTIVATION_SUCCESSFUL"]
        cls.PARKING_SLOT_DELETION_SUCCESSFUL = data["PARKING_SLOT_DELETION_SUCCESSFUL"]
        cls.PARKING_SLOT_ALREADY_VACANT = data["PARKING_SLOT_ALREADY_VACANT"]
        cls.PARKING_SLOT_INACTIVE = data["PARKING_SLOT_INACTIVE"]
        cls.PARKING_SLOT_DELETED = data["PARKING_SLOT_DELETED"]
        cls.CANNOT_VACATE_PARKING_SLOT = data["CANNOT_VACATE_PARKING_SLOT"]
        cls.INPUT_DETAIL_TO_VACATE_PARKING_SLOT = data["INPUT_DETAIL_TO_VACATE_PARKING_SLOT"]
        

        # employee_controller modul prompts
        cls.CUSTOMER_DETAILS_INPUT = data["CUSTOMER_DETAILS_INPUT"]
        cls.VEHICLE_NUMBER_INPUT = data["VEHICLE_NUMBER_INPUT"]
        cls.CUSTOMER_CREATION_SUCCESSFUL = data["CUSTOMER_CREATION_SUCCESSFUL"]
        cls.CUSTOMER_ALREADY_EXIST = data["CUSTOMER_ALREADY_EXIST"]
        cls.CUSTOMER_DOES_NOT_EXIST = data["CUSTOMER_DOES_NOT_EXIST"]
        cls.CUSTOMER_UPDATION_SUCCESSFUL = data["CUSTOMER_UPDATION_SUCCESSFUL"]

        # slot_booking module prompts
        cls.CUSTOMER_OUT_DATE_INPUT = data["CUSTOMER_OUT_DATE_INPUT"]
        cls.INPUT_DETAILS_FOR_SLOT_BOOKING = data["INPUT_DETAILS_FOR_SLOT_BOOKING"]
        cls.VEHCILE_NO_NOT_FOUND = data["VEHCILE_NO_NOT_FOUND"]
        cls.PARKING_SLOT_ASSIGNED = data["PARKING_SLOT_ASSIGNED"]
        cls.BOOKING_RECORD_NOT_FOUND = data["BOOKING_RECORD_NOT_FOUND"]
        cls.NO_UPDATION_FOR_CHECKOUT_VEHICLE = data["NO_UPDATION_FOR_CHECKOUT_VEHICLE"]
        cls.SLOT_BOOKING_UPDATION_SUCCESSFUL = data["SLOT_BOOKING_UPDATION_SUCCESSFUL"]
        cls.INPUT_BOOKING_ID = data["INPUT_BOOKING_ID"]
        cls.PARKING_SLOT_VACANT = data["PARKING_SLOT_VACANT"]
        cls.VEHICLE_ALREADY_VACATE_PARKING_SLOT = data["VEHICLE_ALREADY_VACATE_PARKING_SLOT"]

        # parking_charges prompts
        cls.PRINT_PARKING_CHARGES = data["PRINT_PARKING_CHARGES"]

        # query executor module prompts
        cls.INTEGRITY_ERROR_MESSAGE = data["INTEGRITY_ERROR_MESSAGE"]
        cls.OPERATIONAL_ERROR_MESSAGE = data["OPERATIONAL_ERROR_MESSAGE"]
        cls.PROGRAMMING_ERROR_MESSAGE = data["PROGRAMMING_ERROR_MESSAGE"]
        cls.GENERAL_EXCEPTION_MESSAGE = data["GENERAL_EXCEPTION_MESSAGE"]

        # handler modules prompts
        cls.ADMIN_MENU_WELCOME_MESSAGE = data["ADMIN_MENU_WELCOME_MESSAGE"]
        cls.EMPLOYEE_MENU_WELCOME_MESSAGE = data["EMPLOYEE_MENU_WELCOME_MESSAGE"]
        cls.PRESS_KEY_TO_CONTINUE = data["PRESS_KEY_TO_CONTINUE"]

        # ---- menu prompts ----
        cls.ADMIN_MENU = data["ADMIN_MENU"]
        cls.MANAGE_PROFILE_MENU = data["MANAGE_PROFILE_MENU"]
        cls.EMPLOYEE_DETAIL_UPDATE_MENU = data["EMPLOYEE_DETAIL_UPDATE_MENU"]
        cls.MANAGE_VEHICLE_TYPE_MENU = data["MANAGE_VEHICLE_TYPE_MENU"]
        cls.MANAGE_PARKING_SLOT_MENU = data["MANAGE_PARKING_SLOT_MENU"]
        cls.EMPLOYEE_MENU = data["EMPLOYEE_MENU"]
        cls.CUSTOMER_DETAIL_UPDATE_MENU = data["CUSTOMER_DETAIL_UPDATE_MENU"]
        cls.VIEW_PARKING_STATUS_MENU = data["VIEW_PARKING_STATUS_MENU"]

        # API prompts starts here
        cls.ERROR_STATUS_400 = data["ERROR_STATUS_400"]
        cls.ERROR_STATUS_409 = data["ERROR_STATUS_409"]
        cls.ERROR_STATUS_404 = data["ERROR_STATUS_404"]
        cls.ERROR_STATUS_422 = data["ERROR_STATUS_422"]
        cls.ERROR_STATUS_500 = data["ERROR_STATUS_500"]
        cls.VEHICLE_TYPE_CONFLICT_MSG = data["VEHICLE_TYPE_CONFLICT_MSG"]
        cls.INTERNAL_SERVER_ERROR_MSG = data["INTERNAL_SERVER_ERROR_MSG"]
        cls.VEHICLE_TYPE_NOT_FOUND = data["VEHICLE_TYPE_NOT_FOUND"]
        cls.VEHICLE_TYPE_REGISTER_SUCCESS = data["VEHICLE_TYPE_REGISTER_SUCCESS"]
        cls.VEHICLE_TYPE_GET_SUCCESS = data["VEHICLE_TYPE_GET_SUCCESS"]
        cls.CANNOT_UPDATE_VEHICLE_TYPE_NAME = data["CANNOT_UPDATE_VEHICLE_TYPE_NAME"]
        cls.VEHICLE_TYPE_UPDATE_SUCCESS = data["VEHICLE_TYPE_UPDATE_SUCCESS"]
        cls.VEHICLE_TYPE_ID_REGEX_INVALID = data["VEHICLE_TYPE_ID_REGEX_INVALID"]
        cls.PARKING_SLOT_CONFLICT_MSG = data["PARKING_SLOT_CONFLICT_MSG"]
        cls.PARKING_SLOT_NOT_FOUND = data["PARKING_SLOT_NOT_FOUND"]
        cls.PARKING_SLOT_REGISTER_SUCCESS = data["PARKING_SLOT_REGISTER_SUCCESS"]
        cls.PARKING_SLOT_GET_SUCCESS = data["PARKING_SLOT_GET_SUCCESS"]
        cls.PARKING_SLOT_UPDATE_SUCCESS = data["PARKING_SLOT_UPDATE_SUCCESS"]
        cls.PARKING_SLOT_DELETE_SUCCESS = data["PARKING_SLOT_DELETE_SUCCESS"]