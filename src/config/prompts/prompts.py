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
    ERROR_STATUS_400 = None
    ERROR_STATUS_409 = None
    ERROR_STATUS_404 = None
    ERROR_STATUS_500 = None
    ERROR_STATUS_422 = None
    VEHICLE_TYPE_CONFLICT_MSG = None
    INTERNAL_SERVER_ERROR_MSG = None
    VEHICLE_TYPE_NOT_FOUND = None
    VEHICLE_TYPE_REGISTER_SUCCESS = None
    VEHICLE_TYPE_GET_SUCCESS = None
    CANNOT_UPDATE_VEHICLE_TYPE_NAME = None
    VEHICLE_TYPE_UPDATE_SUCCESS = None
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

        cls.ERROR_STATUS_400 = data["ERROR_STATUS_400"]
        cls.ERROR_STATUS_409 = data["ERROR_STATUS_409"]
        cls.ERROR_STATUS_404 = data["ERROR_STATUS_404"]
        cls.ERROR_STATUS_422 = data["ERROR_STATUS_422"]
        cls.ERROR_STATUS_500 = data["ERROR_STATUS_500"]

        cls.INTERNAL_SERVER_ERROR_MSG = data["INTERNAL_SERVER_ERROR_MSG"]

        cls.VEHICLE_TYPE_CONFLICT_MSG = data["VEHICLE_TYPE_CONFLICT_MSG"]
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