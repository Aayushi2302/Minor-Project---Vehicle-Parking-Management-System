"""Module for performing database operations on data."""
import logging
from mysql import connector
import os
from typing import Optional

from src.config.app_config import AppConfig
from src.config.log_prompts.log_prompts import LogPrompts
from src.config.query import QueryConfig
from src.helpers.log_helper import get_request_id
from src.utils.decorators import error_handler

logger = logging.getLogger('db_helper')

MYSQL_HOSTNAME = os.getenv("MYSQL_HOSTNAME")
MYSQL_USERNAME = os.getenv("MYSQL_USERNAME")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")


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
    connection = None
    cursor = None

    def __init__(self) -> None:
        """
            Method for initializing the sqlite3 connection and cursor object
            Parameter -> self
            Return type -> None
        """
        if Database.connection is None:
            try:
                Database.connection = connector.connect(
                    user = MYSQL_USERNAME,
                    password = MYSQL_PASSWORD,
                    host = MYSQL_HOSTNAME
                )
                Database.cursor = Database.connection.cursor(dictionary=True)
                Database.cursor.execute(QueryConfig.CREATE_DATABASE.format(AppConfig.PROJECT_DB))
                Database.cursor.execute(QueryConfig.USE_DATABASE.format(AppConfig.PROJECT_DB))

                # logger.info(f"[{get_request_id()}] : Successful database connection established.")
            except Exception:
                raise connector.Error

    def create_all_tables(self) -> None:
        """ 
            Method for creating all tables of database
            Parameter -> self
            Return type -> None
        """
        self.cursor.execute(QueryConfig.AUTHENTICATION_TABLE_CREATION)
        # logger.info(f"[{get_request_id()}] : Authentication table creation successful.")
        self.cursor.execute(QueryConfig.TOKEN_TABLE_CREATION)
        # logger.info(f"[{get_request_id()}] : Token table creation successful.")
        self.cursor.execute(QueryConfig.EMPLOYEE_TABLE_CREATION)
        # logger.info(f"[{get_request_id()}] : Employee table creation successful.")
        self.cursor.execute(QueryConfig.VEHICLE_TYPE_TABLE_CREATION)
        # logger.info(f"[{get_request_id()}] : VehicleType table creation successful.")
        self.cursor.execute(QueryConfig.PARKING_SLOT_TABLE_CREATION)
        # logger.info(f"[{get_request_id()}] : ParkingSlot table creation successful.")
        self.cursor.execute(QueryConfig.CUSTOMER_TABLE_CREATION)
        # logger.info(f"[{get_request_id()}] : Customer table creation successful.")
        self.cursor.execute(QueryConfig.SLOT_BOOKING_TABLE_CREATION)
        # logger.info(f"[{get_request_id()}] : SlotBooking table creation successful.")
   
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
        # logger.info(f"[{get_request_id()}] :  Data saved to database successfully.")

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
        # logger.info(f"[{get_request_id()}] :  Data fetched from database successfully.")
        return self.cursor.fetchall()

db = Database()
