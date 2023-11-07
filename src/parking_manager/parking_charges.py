"""
    Module for calculating charges for parking.
"""
import datetime

from config.statements.config import Config
from config.query.query_config import QueryConfig
from database.query_executor import QueryExecutor
from parking_manager.vehicle_type import VehicleType

class ParkingCharges:
    """
        Class for calculating charges for parking.
    """
    def calculate_hours_spent_in_parking(self, in_date: str, in_time: str, out_date: str, out_time: str) -> float:
        """
            Method to calculate the number of hours spent by vehicle in parking facility.
        """
        in_date_list = in_date.split("-")
        in_date_list = [int(val) for val in in_date_list]
        in_time_list = in_time.split(":")
        in_time_list = [int(val) for val in in_time_list]

        out_date_list = out_date.split("-")
        out_date_list = [int(val) for val in out_date_list]
        out_time_list = out_time.split(":")
        out_time_list = [int(val) for val in out_time_list]

        time_obj_1 = datetime.datetime(
                        in_date_list[2],
                        in_date_list[1],
                        in_date_list[0],
                        in_time_list[0],
                        in_time_list[1]
                    )
        time_obj_2 = datetime.datetime(
                        out_date_list[2],
                        out_date_list[1],
                        out_date_list[0],
                        out_time_list[0],
                        out_time_list[1]
                    )
        time_difference = time_obj_2 - time_obj_1
        hours_spent = time_difference.total_seconds() / (60 * 60)
        total_hours_spent = round(hours_spent, 3)
        return total_hours_spent

    def calculate_charges(self, hours_spent: float, booking_id: str) -> float:
        """
            Method for calculating total charges based on the number of hours spent.
        """
        type_id =   QueryExecutor.fetch_data_from_database(
                        QueryConfig.query_for_fetching_type_id_from_booking_id,
                        (booking_id, )
                    )
        type_id = type_id[0][0]
        price_per_hour = QueryExecutor.fetch_data_from_database(
                            QueryConfig.query_for_fetching_price_per_hour_from_type_id,
                            (type_id, )
                        )
        if not any(price_per_hour):
            print(Config.vehicle_type_does_not_exist_prompt + "\n")
            return 0.0
        else:
            price_per_hour = price_per_hour[0][0]
            total_charges = hours_spent * price_per_hour
            total_charges = round(total_charges, 2)
            return total_charges

    @staticmethod
    def view_parking_charges_for_vehicle_type() -> None:
        """
            Method to view charges for each vehicle type.
        """
        vehicle_type_obj = VehicleType()
        vehicle_type_obj.view_vehicle_type()