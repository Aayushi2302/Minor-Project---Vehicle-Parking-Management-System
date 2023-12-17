"""Module for maintaing functionalities related to parking slot booking."""
from datetime import datetime
import random

from config.app_config import AppConfig
from config.query import QueryConfig
from models.database import db
from controller.employee_controller import EmployeeController

class SlotBooking:
    """This class contains methods for maintaing functionalities related to parking slot booking."""
    def __init__(self) -> None:
        self.employee_controller_obj = EmployeeController()

    def get_vacant_parking_slot(self, type_id: str) -> str:
        parking_slot_no =   db.fetch_data_from_database(
                                QueryConfig.FETCH_PARKING_SLOT_NO_FOR_BOOKING,
                                (type_id, AppConfig.PARKING_SLOT_STATUS_VACANT)
                            )
        random_index = random.randrange(len(parking_slot_no))
        print(random_index)
        return parking_slot_no[random_index][0]

    def save_booking_details(self, booking_id: str, cust_vehicle_no: str,
                                cust_in_date: str, cust_in_time: str, cust_out_date: str) -> str:
        data = self.employee_controller_obj.get_cust_id_from_vehicle_no(cust_vehicle_no)

        if not data:
            return ""

        cust_id = data[0][0]
        type_id = data[0][1]

        parking_slot_no = self.get_vacant_parking_slot(type_id)

        slot_booking_data = (booking_id, cust_id, parking_slot_no,
                                cust_in_date, cust_in_time, cust_out_date)
        parking_slot_data = (AppConfig.PARKING_SLOT_STATUS_BOOKED, parking_slot_no)

        query_for_updating_parking_slot_status = QueryConfig.\
                                                 UPDATE_PARKING_SLOT_DETAIL_FROM_PARKING_SLOT_NO.\
                                                 format(AppConfig.STATUS_ATTR)

        data = [slot_booking_data, parking_slot_data]
        query = [QueryConfig.CREATE_SLOT_BOOKING, query_for_updating_parking_slot_status]
        db.save_data_to_database(
            query,
            data
        )
        return parking_slot_no

    def get_booking_details(self) -> list:
        """Method to view booking details."""
        data =  db.fetch_data_from_database(
                    QueryConfig.VIEW_SLOT_BOOKING_DETAIL
                )
        return data

    def get_details_for_vacating_parking_slot(self, vehicle_no: str) -> list:
        data =  db.fetch_data_from_database(
                    QueryConfig.FETCH_DETAIL_FOR_VACATING_PARKING_SLOT,
                    (vehicle_no, )
                )
        return data

    def calculate_hours_spent_in_parking(self, in_date: str, in_time: str,
                                            out_date: str, out_time: str) -> float:
        """Method to calculate the number of hours spent by vehicle in parking facility."""
        in_date_time = in_date + " " + in_time
        in_date_time_obj = datetime.strptime(in_date_time, "%d-%m-%Y %H:%M")
        out_date_time = out_date + " " + out_time
        out_date_time_obj = datetime.strptime(out_date_time, "%d-%m-%Y %H:%M")
        time_difference = out_date_time_obj - in_date_time_obj
        hours_spent = time_difference.total_seconds() / (60 * 60)
        total_hours_spent = round(hours_spent, 3)
        return total_hours_spent

    def calculate_charges(self, hours_spent: float, booking_id: str) -> float:
        """Method for calculating total charges based on the number of hours spent."""
        type_id =   db.fetch_data_from_database(
                        QueryConfig.FETCH_TYPE_ID_FROM_BOOKING_ID,
                        (booking_id, )
                    )
        type_id = type_id[0][0]
        price_per_hour = db.fetch_data_from_database(
                            QueryConfig.FETCH_PRICE_PER_HOUR_FROM_TYPE_ID,
                            (type_id, )
                        )
        price_per_hour = price_per_hour[0][0]
        total_charges = hours_spent * price_per_hour
        total_charges = round(total_charges, 2)
        return total_charges

    def save_vacating_details(self, vehicle_no: str, out_date: str, out_time: str) -> tuple:
        data = self.get_details_for_vacating_parking_slot(vehicle_no)

        if not data:
            return (-1, )

        booking_id = data[0][0]
        parking_slot_no = data[0][1]
        in_date = data[0][2]
        in_time = data[0][3]
        curr_out_time = data[0][4]

        if curr_out_time != AppConfig.DEFAULT_OUT_TIME:
            return (0, )
        else:
            hours_spent = self.calculate_hours_spent_in_parking(in_date, in_time,
                                                                    out_date, out_time)
            charges = self.calculate_charges(hours_spent, booking_id)

            slot_booking_data = (out_date, out_time, hours_spent, charges, booking_id)
            parking_slot_data = (AppConfig.PARKING_SLOT_STATUS_VACANT, parking_slot_no)

            query_for_parking_slot_updation = QueryConfig.\
                                              UPDATE_PARKING_SLOT_DETAIL_FROM_PARKING_SLOT_NO.\
                                              format(AppConfig.STATUS_ATTR)
            query = [QueryConfig.UPDATE_DETAIL_FOR_VACATIG_PARKING_SLOT,
                        query_for_parking_slot_updation]
            data = [slot_booking_data, parking_slot_data]
            db.save_data_to_database(
                query,
                data
            )
            return (charges, hours_spent)
