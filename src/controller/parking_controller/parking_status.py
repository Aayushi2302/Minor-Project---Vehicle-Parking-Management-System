"""Module containing controller logic for parking status module."""

from datetime import datetime
import pytz

from config.query import QueryConfig
from models.database import db

class ParkingStatus:
    """
        Class contaning methods and attributes for managing parking status module.
        ...
        Methods:
        -------
        get_current_date_status() -> method to get current date status.
        get_current_year_status() -> method to get current year status.
    """
    def get_current_date_status(self) -> list:
        """
            Method for view current date booking status.
            Parameter -> self
            Return type -> list
        """
        time_zone = pytz.timezone('Asia/Kolkata')
        current = datetime.now(time_zone)
        curr_date = current.strftime('%d-%m-%Y')
        data =  db.fetch_data_from_database(
                    QueryConfig.FETCH_CURRENT_DATE_RECORD,
                    (curr_date, )
                )
        return data

    def get_current_year_status(self) -> list:
        """
            Method to see current year booking details.
            Parameter -> self
            Return type -> list
        """
        time_zone = pytz.timezone('Asia/Kolkata')
        current = datetime.now(time_zone)
        curr_year = int(current.strftime('%Y'))
        curr_year_query = f"%-%-{curr_year}"
        data =  db.fetch_data_from_database(
                    QueryConfig.FETCH_CURRENT_YEAR_RECORD,
                    (curr_year_query, )
                )
        return data
