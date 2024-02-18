"""Module contating business logic for performing operations on vehicle type."""

import pymysql

from config.app_config import AppConfig
from config.prompts.prompts import Prompts
from config.query import QueryConfig
from config.regex_pattern import RegexPattern
from models.database import Database
from helpers.common_helper import (generate_shortuuid,
                                       get_constraint_failed_attribute,
                                       regex_validation)
from utils.custom_exceptions import AppException, DBException


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

    def __check_for_valid_type_id(self, type_id: str) -> None:
        """
            Method to check for invalid type id.
            Parameters -> emp_id: str
            Returns -> None
        """
        result = regex_validation(RegexPattern.TYPE_ID_REGEX, type_id)

        if not result:
            raise AppException(422, "Unprocessable Entity", "Type ID is not as per required standard.")

    def register_vehicle_type(self, vehicle_type_name: str, price_per_hour: float) -> None:
        """
            Method for registering vehicle type.
            Parameter -> type_name: str, price_per_hour: float
            Return type -> None
        """
        try:
            type_id = generate_shortuuid(AppConfig.VEHICLE_TYPE)
            self.db.save_data_to_database(
                QueryConfig.CREATE_VEHICLE_TYPE,
                (type_id, vehicle_type_name, price_per_hour)
            )

        except pymysql.IntegrityError as error:
            # constraint_failed_attribute = get_constraint_failed_attribute(error.msg)
            raise AppException(409, "Conflict", "Entered {constraint_failed_attribute} already exist.")

        except pymysql.Error:
            raise DBException(500, "Internal Server Error", "Something went wrong with server.")

    def get_all_vehicle_type(self) -> list:
        """
            Method to get a list of all existing vehicle types.
            Parameter -> None
            Return type -> list
        """
        try:
            data = self.db.fetch_data_from_database(QueryConfig.FETCH_VEHICLE_TYPE)
            return data
        except pymysql.Error:
            raise DBException(500, "Internal Server Error", "Something went wrong with server.")

    def __get_vehicle_type_name_from_type_id(self, type_id: str) -> list:
        """
            Method to get vehicle type_name from type_id.
            Parameter -> type_id: str
            Return type -> list
        """
        try:
            data = self.db.fetch_data_from_database(
                QueryConfig.FETCH_VEHICLE_TYPE_NAME_FROM_TYPE_ID,
                (type_id,)
            )
            return data

        except pymysql.Error:
            raise DBException(500, "Internal Server Error", "Something went wrong with server.")

    def get_vehicle_type_id_from_type_name(self, type_name: str) -> list:
        try:
            data = self.db.fetch_data_from_database(
                QueryConfig.FETCH_VEHICLE_TYPE_ID_FROM_TYPE_NAME,
                (type_name,)
            )
            return data

        except pymysql.Error:
            raise DBException(500, "Internal Server Error", "Something went wrong with server.")

    def get_individual_vehicle_type(self, type_id: str) -> list:
        """
            Method to get individual vehicle type details.
            Parameter -> type_id: str
            Return type -> list
        """
        try:
            self.__check_for_valid_type_id(type_id)
            data = self.db.fetch_data_from_database(
                QueryConfig.FETCH_VEHICLE_TYPE_FROM_TYPE_ID,
                (type_id,)
            )
            return data

        except pymysql.Error:
            raise DBException(500, "Internal Server Error", "Something went wrong with server.")

    def update_vehicle_type(self, type_id: str, vehicle_type_name: str, new_price_per_hour: float) -> None:
        """
            Method to update a particular vehicle type.
            Parameter -> type_id: str, type_name: str, new_price_per_hour: float
            Return type -> None
        """
        try:
            self.__check_for_valid_type_id(type_id)
            data = self.__get_vehicle_type_name_from_type_id(type_id)

            if not data:
                raise AppException(404, "Data Not Found", "Vehicle type does not exist.")

            if vehicle_type_name != data[0]["vehicle_type_name"]:
                raise AppException(403, "Forbidden", "Cannot update vehicle type name")

            self.db.save_data_to_database(
                QueryConfig.UPDATE_VEHICLE_TYPE_DETAIL_FROM_TYPE_ID,
                (vehicle_type_name, new_price_per_hour, type_id)
            )

        except pymysql.Error:
            raise DBException(500, "Internal Server Error", "Something went wrong with server.")
