"""
    Module for maintaing methods for showing booking status to admin.
"""
from datetime import datetime
import pytz

from config.statements.config import Config
from config.query.query_config import QueryConfig
from database.query_executor import QueryExecutor
from parking_manager.slot_booking import SlotBooking
from utils.common import Common

class ParkingStatus:
    """
        Class for display different booking status to admin.
    """
    @staticmethod
    def view_current_date_status() -> None:
        """
            Method for view current date booking status.
        """
        time_zone = pytz.timezone('Asia/Kolkata')
        current = datetime.now(time_zone)
        curr_date = current.strftime('%d-%m-%Y')
        data =  QueryExecutor.fetch_data_from_database(
                    QueryConfig.query_for_fetching_current_date_record,
                    (curr_date, )
                )
        if not any(data):
            print(Config.zero_record_prompt.format("booking") + "\n")
        else:
            common_obj = Common()
            headers = QueryConfig.slot_booking_detail_header
            common_obj.display_table(data, headers)
            
    @staticmethod
    def view_current_year_status() -> None:
        """
            Method to see current year booking details.
        """
        time_zone = pytz.timezone('Asia/Kolkata')
        current = datetime.now(time_zone)
        curr_year = int(current.strftime('%Y'))
        curr_year_query = f"%-%-{curr_year}"
        data =  QueryExecutor.fetch_data_from_database(
                    QueryConfig.query_for_fetching_past_year_record,
                    (curr_year_query, )
                )
        if not any(data):
            print(Config.zero_record_prompt.format("booking") + "\n")
        else:
            common_obj = Common()
            headers = QueryConfig.slot_booking_detail_header
            common_obj.display_table(data, headers)

    @staticmethod
    def view_total_vehicle_entries() -> None:
        slot_booking_obj = SlotBooking()
        slot_booking_obj.view_booking_details()