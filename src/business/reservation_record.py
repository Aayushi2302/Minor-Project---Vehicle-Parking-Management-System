"""Module containing business logic to show reservation record as according to year and date."""

from datetime import datetime
import pytz
from mysql import connector

from src.config.query import QueryConfig
from src.models.database import Database
from src.utils.custom_exceptions import DBException

class ReservationRecord:

    def __init__(self, db: Database) -> None:
        self.db = db
    def __get_current_date(self) -> str:
        time_zone = pytz.timezone('Asia/Kolkata')
        current = datetime.now(time_zone)
        curr_date = current.strftime('%d-%m-%Y')
        return curr_date

    def __get_current_year(self) -> int:
        time_zone = pytz.timezone('Asia/Kolkata')
        current = datetime.now(time_zone)
        curr_year = int(current.strftime('%Y'))
        return curr_year

    def get_current_date_record(self) -> list:
        try:
            curr_date = self.__get_current_date()
            data = self.db.fetch_data_from_database(
                        QueryConfig.FETCH_CURRENT_DATE_RECORD,
                        (curr_date, )
                    )
            return data

        except connector.Error:
            raise DBException(500, "Internal Server Error", "...")

    def get_current_year_record(self) -> list:
        try:
            curr_year = self.__get_current_year()
            curr_year_query = f"%-%-{curr_year}"
            data = self.db.fetch_data_from_database(
                        QueryConfig.FETCH_CURRENT_YEAR_RECORD,
                        (curr_year_query, )
                    )
            return data

        except connector.Error:
            raise DBException(500, "Internal Server Error", "...")