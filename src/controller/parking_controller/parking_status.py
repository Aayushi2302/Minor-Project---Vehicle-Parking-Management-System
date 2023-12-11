"""Module for maintaing methods for showing booking status to admin."""
from datetime import datetime
import pytz

from config.query import QueryConfig
from models.database import db

class ParkingStatus:
    """This class contains methods for displaying different booking status to admin."""
    def get_current_date_status(self) -> list:
        """Method for view current date booking status."""
        time_zone = pytz.timezone('Asia/Kolkata')
        current = datetime.now(time_zone)
        curr_date = current.strftime('%d-%m-%Y')
        data =  db.fetch_data_from_database(
                    QueryConfig.FETCH_CURRENT_DATE_RECORD,
                    (curr_date, )
                )
        return data
            
    def get_current_year_status(self) -> None:
        """Method to see current year booking details."""
        time_zone = pytz.timezone('Asia/Kolkata')
        current = datetime.now(time_zone)
        curr_year = int(current.strftime('%Y'))
        curr_year_query = f"%-%-{curr_year}"
        data =  db.fetch_data_from_database(
                    QueryConfig.FETCH_CURRENT_YEAR_RECORD,
                    (curr_year_query, )
                )
        return data
