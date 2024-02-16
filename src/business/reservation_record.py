"""Module containing business logic to show reservation record as according to year and date."""

from mysql import connector

from src.config.query import QueryConfig
from src.models.database import Database
from src.utils.custom_exceptions import DBException


class ReservationRecord:
    """
        Class containing methods to show year-wise or date-wise reservation records.
        ...
        Attributes
        ----------
        db: Database Object

        Methods
        -------
        get_date_record(): list -> method to get date wise record.
        get_year_record(): list -> method to get year wise record.
    """
    def __init__(self, db: Database) -> None:
        """Constructor for reservation record"""
        self.db = db

    def get_date_record(self, date: str) -> list:
        """
            Method to get date-wise record.
            Parameters -> date: str
            Returns -> list
        """
        try:
            data = self.db.fetch_data_from_database(
                        QueryConfig.FETCH_CURRENT_DATE_RECORD,
                        (date, )
                    )
            return data

        except connector.Error:
            raise DBException(500, "Internal Server Error", "...")

    def get_year_record(self, year: str) -> list:
        """
            Method to get year-wise record.
            Parameters -> year: str
            Returns -> list
        """
        try:
            year_query = f"%-%-{year}"
            data = self.db.fetch_data_from_database(
                        QueryConfig.FETCH_CURRENT_YEAR_RECORD,
                        (year_query, )
                    )
            return data

        except connector.Error:
            raise DBException(500, "Internal Server Error", "...")