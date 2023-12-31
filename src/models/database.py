"""Module for performing database operations on data."""
import logging
import sqlite3
from typing import Optional

from config.app_config import AppConfig
from config.log_prompts.log_prompts import LogPrompts
from config.prompts.prompts import Prompts
from config.query import QueryConfig
from utils.decorators import error_handler

logger = logging.getLogger('db_helper')

class Database:
    """
        This class contains methods for executing database queries fetched from QueryConfig.
        ...
        Attributes
        ---------
        connection -> sqlite3.Connection
        cursor -> sqlite3.Cursor

        Methods
        -------
        create_all_tables() -> Method for creating all database tables.
        save_data_to_database() -> Method for saving data to single or multiple tables in database.
        fetch_data_from_database() -> Method for fetching data from database tables.   
    """
    @error_handler
    def __init__(self) -> None:
        """
            Method for initializing the sqlite3 connection and cursor object
            Parameter -> self
            Return type -> None
        """
        try:
            self.connection = sqlite3.connect(AppConfig.DATABASE_PATH)
            self.cursor = self.connection.cursor()
            logger.info(LogPrompts.SUCCESSFUL_CONNECTION_ESTABLISHED_INFO)
        except Exception:
            raise sqlite3.Error

    def create_all_tables(self) -> None:
        """ 
            Method for creating all tables of database
            Parameter -> self
            Return type -> None
        """
        self.cursor.execute(QueryConfig.AUTHENTICATION_TABLE_CREATION)
        logger.info(LogPrompts.SUCCESSFUL_AUTHENTICATION_TABLE_CREATION_INFO)
        self.cursor.execute(QueryConfig.EMPLOYEE_TABLE_CREATION)
        logger.info(LogPrompts.SUCCESSFUL_EMPLOYEE_TABLE_CREATION_INFO)
        self.cursor.execute(QueryConfig.CUSTOMER_TABLE_CREATION)
        logger.info(LogPrompts.SUCCESSFUL_CUSTOMER_TABLE_CREATION_INFO)
        self.cursor.execute(QueryConfig.PARKING_SLOT_TABLE_CREATION)
        logger.info(LogPrompts.SUCCESSFUL_PARKING_SLOT_TABLE_CREATION_INFO)
        self.cursor.execute(QueryConfig.VEHICLE_TYPE_TABLE_CREATION)
        logger.info(LogPrompts.SUCCESSFUL_VEHICLE_TYPE_TABLE_CREATION_INFO)
        self.cursor.execute(QueryConfig.SLOT_BOOKING_TABLE_CREATION)
        logger.info(LogPrompts.SUCCESSFUL_SLOT_BOOKING_TABLE_CREATION_INFO)
   
    def save_data_to_database(self, query: str | list, data: tuple | list) -> None:
        """
            Method for saving data to single or multiple tables in database.
            Paramter -> self, query: Union[str, list], data: Union[tuple, list]
            Return type -> None
        """
        if isinstance(query, str):
            self.cursor.execute(query, data)
        else:
            for i in range(len(query)):
                self.cursor.execute(query[i], data[i])
        self.connection.commit()
        logger.info(LogPrompts.DATA_SAVED_TO_DATABASE_SUCCESSFUL_INFO)

    def fetch_data_from_database(self, query: str, data: Optional[tuple] = None) -> list:
        """
            Method for fetching data from single or multiple tables in database.
            Paramter -> self, query: str, data: Union[tuple, None]
            Return type -> list
        """
        if data is None:
            self.cursor.execute(query)
        else:
            self.cursor.execute(query, data)
        logger.info(LogPrompts.DATA_FETCHED_FROM_DATABASE_SUCESSFUL_INFO)
        return self.cursor.fetchall()

db = Database()
