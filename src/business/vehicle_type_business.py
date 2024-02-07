"""Module contating business logic for performing operations on vehicle type."""

from mysql import connector

from config.app_config import AppConfig
from config.prompts.prompts import Prompts
from config.query import QueryConfig
from config.regex_pattern import RegexPattern
from models.database import Database
from utils.common_helper import (generate_shortuuid,
                                 get_constraint_failed_attribute,
                                 regex_validation)
from utils.custom_exceptions import (DataAlreadyExists,
                                     DBException,
                                     DataNotFound,
                                     CustomBaseException,
                                     InvalidRegex)

class VehicleTypeBusiness:
    """
        Class containing methods for performing operations on vehicle type.
        ...
        Attributes
        ---------
        db : Database -> Database object
        Methods
        -------
        __get_vehicle_type_name_from_type_id(): list -> method to get vehicle type name.
        register_vehicle_type(): None -> method for registering vehicle type.
        get_all_vehicle_type(): list -> method to get all vehicle type.
        get_particular_vehicle_type(): dict -> method to get a particular vehicle type.
        update_vehicle_type(): None -> method to update vehicle type.
    """
    def __init__(self, db: Database) -> None:
        """Constructor for vehicle type."""
        self.db = db

    def register_vehicle_type(self, type_name: str, price_per_hour: float) -> None:
        """
            Method for registering vehicle type.
            Parameter -> type_name: str, price_per_hour: float
            Return type -> None
        """
        try:
            type_id = generate_shortuuid(AppConfig.VEHICLE_TYPE)
            self.db.save_data_to_database(
                QueryConfig.CREATE_VEHICLE_TYPE,
                (type_id, type_name, price_per_hour)
            )

        except connector.IntegrityError as error:
            failed_attribute = get_constraint_failed_attribute(error.msg)
            raise DataAlreadyExists(409, Prompts.ERROR_STATUS_409,
                                        Prompts.VEHICLE_TYPE_CONFLICT_MSG.format(failed_attribute))

        except connector.Error:
            raise DBException(500, Prompts.ERROR_STATUS_500, Prompts.INTERNAL_SERVER_ERROR_MSG)

    def get_all_vehicle_type(self) -> list:
        """
            Method to get a list of all existing vehicle types.
            Parameter -> None
            Return type -> list
        """
        try:
            data = self.db.fetch_data_from_database(QueryConfig.FETCH_VEHICLE_TYPE)
            return data
        except connector.Error:
            raise DBException(500, Prompts.ERROR_STATUS_500, Prompts.INTERNAL_SERVER_ERROR_MSG)

    def __get_vehicle_type_name_from_type_id(self, type_id: str) -> list:
        """
            Method to get vehicle type_name from type_id.
            Parameter -> type_id: str
            Return type -> list
        """
        try:
            data =  self.db.fetch_data_from_database(
                        QueryConfig.FETCH_VEHICLE_TYPE_NAME_FROM_TYPE_ID,
                        (type_id, )
                    )
            return data

        except connector.Error:
            raise DBException(500, Prompts.ERROR_STATUS_500, Prompts.INTERNAL_SERVER_ERROR_MSG)


    def get_vehicle_type_id_from_type_name(self, type_name: str) -> list:
        try:
            data = self.db.fetch_data_from_database(
                QueryConfig.FETCH_VEHICLE_TYPE_ID_FROM_TYPE_NAME,
                (type_name,)
            )
            return data

        except connector.Error:
            raise DBException(500, Prompts.ERROR_STATUS_500, Prompts.INTERNAL_SERVER_ERROR_MSG)

    def get_individual_vehicle_type(self, type_id: str) -> list:
        """
            Method to get individual vehicle type details.
            Parameter -> type_id: str
            Return type -> list
        """
        try:
            data =  self.db.fetch_data_from_database(
                        QueryConfig.FETCH_VEHICLE_TYPE_FROM_TYPE_ID,
                        (type_id, )
                    )
            return data

        except connector.Error:
            raise DBException(500, Prompts.ERROR_STATUS_500, Prompts.INTERNAL_SERVER_ERROR_MSG)

    def update_vehicle_type(self, type_id: str, type_name: str, new_price_per_hour: float) -> None:
        """
            Method to update a particular vehicle type.
            Parameter -> type_id: str, type_name: str, new_price_per_hour: float
            Return type -> None
        """
        try:

            result = regex_validation(RegexPattern.TYPE_ID_REGEX, type_id)

            if not result:
                raise InvalidRegex(422, Prompts.ERROR_STATUS_422,
                                    Prompts.VEHICLE_TYPE_ID_REGEX_INVALID)

            data = self.__get_vehicle_type_name_from_type_id(type_id)

            if not data:
                raise DataNotFound(404, Prompts.ERROR_STATUS_404, Prompts.VEHICLE_TYPE_NOT_FOUND)

            if type_name != data[0][AppConfig.TYPE_NAME_ATTR]:
                raise CustomBaseException(403, "Forbidden", "Cannot update vehicle type name")

            self.db.save_data_to_database(
                QueryConfig.UPDATE_VEHICLE_TYPE_DETAIL_FROM_TYPE_ID,
                (type_name, new_price_per_hour, type_id)
            )

        except connector.Error:
            raise DBException(500, Prompts.ERROR_STATUS_500, Prompts.INTERNAL_SERVER_ERROR_MSG)
