from datetime import datetime
import random
from mysql import connector

from src.config.app_config import AppConfig
from src.config.query import QueryConfig
from src.models.database import Database
from src.utils.custom_exceptions import DBException


class SlotReservationHelper:

    def __init__(self, db: Database) -> None:
        self.db = db

    def get_vacant_parking_slot_randomly(self, type_id: str) -> str:
        try:
            parking_slot_no = self.db.fetch_data_from_database(
                QueryConfig.FETCH_PARKING_SLOT_NO_FOR_BOOKING,
                (type_id, AppConfig.PARKING_SLOT_STATUS_VACANT)
            )
            random_index = random.randrange(len(parking_slot_no))
            return parking_slot_no[random_index]["parking_slot_no"]

        except connector.Error:
            raise DBException(500, "Internal Server Error", "...")

    def get_details_for_vacating_parking_slot(self, vehicle_no: str) -> list:
        """
            Method to fetch details for vacating parking slot.
            Parameter -> self, vehicle_no: str
            Return type -> list
        """
        try:
            data = self.db.fetch_data_from_database(
                QueryConfig.FETCH_DETAIL_FOR_VACATING_PARKING_SLOT,
                (vehicle_no,)
            )
            return data

        except connector.Error:
            raise DBException(500, "Internal Server Error", "...")

    def calculate_hours_spent_in_parking(self, in_date: str, in_time: str,
                                         out_date: str, out_time: str) -> float:
        """
            Method to calculate the number of hours spent by vehicle in parking facility.
            Parameter -> self, in_date: str, in_time: str, out_date: str, out_time: str
            Return type -> float
        """
        in_date_time = in_date + " " + in_time
        in_date_time_obj = datetime.strptime(in_date_time, "%d-%m-%Y %H:%M")
        out_date_time = out_date + " " + out_time
        out_date_time_obj = datetime.strptime(out_date_time, "%d-%m-%Y %H:%M")
        time_difference = out_date_time_obj - in_date_time_obj
        hours_spent = time_difference.total_seconds() / (60 * 60)
        total_hours_spent = round(hours_spent, 3)
        return total_hours_spent

    def __get_charges_for_vehicle_type(self, type_id: str) -> float:
        try:
            data = self.db.fetch_data_from_database(
                QueryConfig.FETCH_PRICE_PER_HOUR_FROM_TYPE_ID,
                (type_id,)
            )
            return data[0]["price_per_hour"]

        except connector.Error:
            raise DBException(500, "Internal Server Error", "...")

    def calculate_charges(self, hours_spent: float, type_id: str) -> float:
        """
            Method for calculating total charges based on the number of hours spent.
            Parameter -> self, hours_spent: float, booking_id: str
            Return type -> float
        """

        price_per_hour = self.__get_charges_for_vehicle_type(type_id)
        total_charges = hours_spent * price_per_hour
        total_charges = round(total_charges, 2)
        return total_charges
