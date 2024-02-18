"""This module contains the business logic related to parking slots."""

import pymysql

from config.app_config import AppConfig
from config.prompts.prompts import Prompts
from config.query import QueryConfig
from business.vehicle_type_business import VehicleTypeBusiness
from models.database import Database
from utils.custom_exceptions import AppException, DBException

class ParkingSlotBusiness:
    """
        Class containing business logic for handling operations on parking slots.
        ...
        Attributes
        ----------
        db : Database Object
        vehicle_type_business_obj : VehicleTypeBusiness Object

        Methods
        -------
        register_parking_slot() : None -> method to register or add a parking slot.
        get_all_parking_slots() : list -> method to get all the existing parking slots.
        get_individual_parking_slot() : list -> method to get individual parking slot.
        update_parking_slot_status() : None -> method to update parking slot status.
    """
    def __init__(self, db: Database) -> None:
        """Constructor for parking slot business."""
        self.db = db
        self.vehicle_type_business_obj = VehicleTypeBusiness(db)
    
    def register_parking_slot(self, parking_slot_no: str, type_name: str) -> None:
        """
            Method to register parking slot.
            Parameters -> parking_slot_no: str, type_name: str
            Return type -> None
        """
        try:
            data = self.vehicle_type_business_obj.get_vehicle_type_id_from_type_name(type_name)

            if not data:
                raise AppException(404, "Data Not Found", "Vehicle type not found.")

            type_id = data[0]["type_id"]

            self.db.save_data_to_database(
                QueryConfig.CREATE_PARKING_SLOT,
                (parking_slot_no, type_id)
            )

        except pymysql.IntegrityError as error:
            raise AppException(409, "Conflict", "Parking slot already exist.")

        except pymysql.Error:
            raise DBException(500, "Internal Server Error", "Something went wrong with server.")

    def get_all_parking_slots(self) -> list:
        """
            Method to get all existing parking slots.
            Parameter -> None
            Return type -> list
        """
        try:
            data = self.db.fetch_data_from_database(QueryConfig.VIEW_PARKING_SLOT_DETAIL)
            return data

        except pymysql.Error:
            raise DBException(500, "Internal Server Error", "Something went wrong with server.")

    def get_individual_parking_slot(self, parking_slot_number: str) -> list:
        """
            Method to get individual parking slot.
            Parameter -> parking_slot_number: str
            Return type -> list
        """
        try:
            data = self.db.fetch_data_from_database(
                        QueryConfig.FETCH_PARKING_SLOT_DETAIL_FROM_PARKING_SLOT_NUMBER,
                        (parking_slot_number, )
                    )
            return data

        except pymysql.Error:
            raise DBException(500, "Internal Server Error", "Something went wrong with server.")

    def update_parking_slot_status(self, parking_slot_no: str, new_status: str) -> None:
        """
            Method to update the status of existing parking slot.
            Parameter -> parking_slot_no: str, type_name: str, new_status: str
            Return type -> None
        """
        try:
            data = self.get_individual_parking_slot(parking_slot_no)

            if not data:
                raise AppException(404, "Data Not Found", "Parking slot not exist.")

            self.db.save_data_to_database(
                QueryConfig.UPDATE_PARKING_SLOT_STATUS_FROM_PARKING_SLOT_NO,
                (new_status, parking_slot_no)
            )

        except pymysql.Error:
            raise DBException(500, "Internal Server Error", "Something went wrong with server.")
