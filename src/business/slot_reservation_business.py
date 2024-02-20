"""Module containing business logic related to slot reservation."""

import pymysql

from src.config.app_config import AppConfig
from src.config.query import QueryConfig
from src.models.database import Database
from src.helpers.customer_helper import CustomerHelper
from src.helpers.slot_reservation_helper import SlotReservationHelper
from src.helpers.common_helper import generate_shortuuid, get_current_date_and_time
from src.utils.custom_exceptions import AppException, DBException


class SlotReservationBusiness:
    """
        Class responsible for storing business logic related to parking slot reservation.
        ...
        Attributes
        ----------
        db: Database Object
        slot_reservation_helper: SlotReservationHelper Object
        customer_helper: CustomerHelper Object

        Methods
        -------
        save_reservation_details(): list -> method to save parking slot reservation details.
        get_reservation_details(): list -> method to get all reservations.
        save_vacating_details(): list -> method to save parking slot vacating details.
    """
    def __init__(self, db: Database, slot_reservation_helper: SlotReservationHelper,
                 customer_helper: CustomerHelper) -> None:
        """Constructor for slot reservation business."""
        self.db = db
        self.slot_reservation_helper = slot_reservation_helper
        self.customer_helper = customer_helper

    def save_reservation_details(self, cust_vehicle_no: str, cust_out_date: str) -> list:
        """
            Method to save data for parking slot reservation.
            Parameters -> cust_vehicle_no: str, cust_out_date: str
            Returns -> None
        """
        try:
            booking_id = generate_shortuuid("RSR")
            data = self.customer_helper.get_cust_id_from_vehicle_no(cust_vehicle_no)

            if not data:
                raise AppException(404, "Data Not Found", "Given customer does not exist.")

            cust_id = data[0]["customer_id"]
            type_id = data[0]["type_id"]

            parking_slot_no = self.slot_reservation_helper.get_vacant_parking_slot_randomly(type_id)

            if not parking_slot_no:
                raise AppException(404, "Data Not Found", "Parking slots not found.")

            cust_in_date_time = get_current_date_and_time()
            cust_in_date = cust_in_date_time["date"]
            cust_in_time = cust_in_date_time["time"]

            slot_booing_data = (booking_id, cust_id, parking_slot_no, cust_in_date, cust_in_time, cust_out_date)
            parking_slot_data = (AppConfig.PARKING_SLOT_STATUS_BOOKED, parking_slot_no)

            query = [QueryConfig.CREATE_SLOT_BOOKING, QueryConfig.UPDATE_PARKING_SLOT_STATUS_FROM_PARKING_SLOT_NO]

            self.db.save_data_to_database(
                query,
                [slot_booing_data, parking_slot_data]
            )
            return [{"parking_slot_no" : parking_slot_no}]

        except pymysql.Error as error:
            print(error)
            raise DBException(500, "Internal Server Error", "...")

    def get_reservation_details(self) -> list:
        """
            Method to get all the reservations.
            Parameters -> None
            Returns -> list
        """
        try:
            data = self.db.fetch_data_from_database(
                QueryConfig.VIEW_SLOT_BOOKING_DETAIL
            )
            return data
        except pymysql.Error:
            raise DBException(500, "Internal Server Error", "...")

    def save_vacating_details(self, vehicle_no: str) -> list:
        """
            Method to save parking slot vacating details.
            Parameters -> vehicle_no: str
            Returns -> dict
        """
        try:
            data = self.slot_reservation_helper.get_details_for_vacating_parking_slot(vehicle_no)

            if not data:
                raise AppException(404, "Data Not Found", "...")

            booking_id = data[0]["booking_id"]
            parking_slot_no = data[0]["parking_slot_no"]
            type_id = data[0]["type_id"]
            cust_in_date = data[0]["in_date"]
            cust_in_time = data[0]["in_time"]
            cust_out_time = data[0]["out_time"]

            if cust_out_time != AppConfig.DEFAULT_OUT_TIME:
                raise AppException(403, "Forbidden", "Customer already left parking")

            cust_out_date_time = get_current_date_and_time()
            cust_out_date = cust_out_date_time["date"]
            cust_out_time = cust_out_date_time["time"]

            hours_spent = self.slot_reservation_helper.calculate_hours_spent_in_parking(
                cust_in_date, cust_in_time, cust_out_date, cust_out_time
            )
            charges = self.slot_reservation_helper.calculate_charges(hours_spent, type_id)

            slot_booking_data = (cust_out_date, cust_out_time, hours_spent, charges, booking_id)
            parking_slot_data = (AppConfig.PARKING_SLOT_STATUS_VACANT, parking_slot_no)

            query = [QueryConfig.UPDATE_DETAIL_FOR_VACATIG_PARKING_SLOT,
                     QueryConfig.UPDATE_PARKING_SLOT_STATUS_FROM_PARKING_SLOT_NO]

            self.db.save_data_to_database(
                query,
                [slot_booking_data, parking_slot_data]
            )

            return [{
                "hours": hours_spent,
                "charges": charges
            }]
        except pymysql.Error:
            raise DBException(500, "Internal Server Error", "...")
