"""Module containing helper methods for slot reservation."""

from datetime import datetime
import random
import pymysql

from config.app_config import AppConfig
from config.query import QueryConfig
from models.database import Database
from utils.custom_exceptions import DBException


class SlotReservationHelper:
    """
        Class containing helper methods for parking slot reservation.
        ...
        Attributes
        ----------
        db: Database Object

        Methods
        -------
        __get_charges_for_vehicle_type(): float -> method to calculate charges per hour for vehicle type.
        get_vacant_parking_slot_random(): str -> method to get a parking slot for a vehicle type.
        get_details_for_vacating_parking_slot(): list -> method to fetch details for vacating parking slot.
        calculate_hours_spent_in_parking(): float -> method to calculate total hours spent in parking.
        calculate_charges(): float -> method to calculate total charges.
    """
    def __init__(self, db: Database) -> None:
        """Constructor for slot reservation helper."""
        self.db = db

    def __get_charges_for_vehicle_type(self, type_id: str) -> float:
        """
            Method to calculate charges per hour for vehicle type.
            Parameters -> type_id: str
            Returns -> float
        """
        try:
            data = self.db.fetch_data_from_database(
                QueryConfig.FETCH_PRICE_PER_HOUR_FROM_TYPE_ID,
                (type_id,)
            )
            return data[0]["price_per_hour"]

        except pymysql.Error:
            raise DBException(500, "Internal Server Error", "...")

    def get_vacant_parking_slot_randomly(self, type_id: str) -> str:
        """
            Method to randomly get a parking slot for a vehicle type.
            Parameters -> type_id: str
            Returns -> str
        """
        try:
            parking_slot_no = self.db.fetch_data_from_database(
                QueryConfig.FETCH_PARKING_SLOT_NO_FOR_BOOKING,
                (type_id, AppConfig.PARKING_SLOT_STATUS_VACANT)
            )

            if not parking_slot_no:
                return ""
            random_index = random.randrange(len(parking_slot_no))
            return parking_slot_no[random_index]["parking_slot_no"]

        except pymysql.Error:
            raise DBException(500, "Internal Server Error", "...")

    def get_details_for_vacating_parking_slot(self, vehicle_no: str) -> list:
        """
            Method to fetch details for vacating parking slot.
            Parameters -> vehicle_no: str
            Returns -> list
        """
        try:
            data = self.db.fetch_data_from_database(
                QueryConfig.FETCH_DETAIL_FOR_VACATING_PARKING_SLOT,
                (vehicle_no,)
            )
            return data

        except pymysql.Error:
            raise DBException(500, "Internal Server Error", "...")

    def calculate_hours_spent_in_parking(self, in_date: str, in_time: str,
                                         out_date: str, out_time: str) -> float:
        """
            Method to calculate the number of hours spent by vehicle in parking facility.
            Parameters -> in_date: str, in_time: str, out_date: str, out_time: str
            Returns -> float
        """
        in_date_time = in_date + " " + in_time
        in_date_time_obj = datetime.strptime(in_date_time, "%d-%m-%Y %H:%M")
        out_date_time = out_date + " " + out_time
        out_date_time_obj = datetime.strptime(out_date_time, "%d-%m-%Y %H:%M")
        time_difference = out_date_time_obj - in_date_time_obj
        hours_spent = time_difference.total_seconds() / (60 * 60)
        total_hours_spent = round(hours_spent, 3)
        return total_hours_spent

    def calculate_charges(self, hours_spent: float, type_id: str) -> float:
        """
            Method for calculating total charges based on the number of hours spent.
            Parameters -> hours_spent: float, booking_id: str
            Returns -> float
        """

        price_per_hour = self.__get_charges_for_vehicle_type(type_id)
        total_charges = hours_spent * price_per_hour
        total_charges = round(total_charges, 2)
        return total_charges
