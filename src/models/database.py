"""Module for performing database operations on data."""
import pymysql
import os
from typing import Optional

from src.config.app_config import AppConfig
from src.config.query import QueryConfig

MYSQL_HOSTNAME = os.getenv("MYSQL_HOSTNAME")
MYSQL_USERNAME = os.getenv("MYSQL_USERNAME")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
MYSQL_PORT = 24164


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
            Method for initializing the mysql connection and cursor object
            Parameters -> None
            Returns -> None
        """
        if Database.connection is None:
            try:
                # Database.connection = connector.connect(
                #     user = MYSQL_USERNAME,
                #     password = MYSQL_PASSWORD,
                #     host = MYSQL_HOSTNAME
                # )
                # Database.cursor = Database.connection.cursor(dictionary=True)
                # Database.cursor.execute(QueryConfig.CREATE_DATABASE.format(AppConfig.PROJECT_DB))
                # Database.cursor.execute(QueryConfig.USE_DATABASE.format(AppConfig.PROJECT_DB))
                timeout = 10
                Database.connection = pymysql.connect(
                    charset="utf8mb4",
                    connect_timeout=timeout,
                    cursorclass=pymysql.cursors.DictCursor,
                    db="parking_management_system",
                    host=MYSQL_HOSTNAME,
                    password=MYSQL_PASSWORD,
                    read_timeout=timeout,
                    port=MYSQL_PORT,
                    user=MYSQL_USERNAME,
                    write_timeout=timeout,
                )
                Database.cursor = Database.connection.cursor()
            except pymysql.Error as err:
                print(err)
                raise pymysql.Error

    def create_all_tables(self) -> None:
        """ 
            Method for creating all tables of database
            Parameter -> None
            Returns -> None
        """
        self.cursor.execute(QueryConfig.AUTHENTICATION_TABLE_CREATION)
        self.cursor.execute(QueryConfig.TOKEN_TABLE_CREATION)
        self.cursor.execute(QueryConfig.EMPLOYEE_TABLE_CREATION)
        self.cursor.execute(QueryConfig.VEHICLE_TYPE_TABLE_CREATION)
        self.cursor.execute(QueryConfig.PARKING_SLOT_TABLE_CREATION)
        self.cursor.execute(QueryConfig.CUSTOMER_TABLE_CREATION)
        self.cursor.execute(QueryConfig.SLOT_BOOKING_TABLE_CREATION)

    def save_data_to_database(self, query: str | list, data: tuple | list) -> None:
        """
            Method for saving data to single or multiple tables in database.
            Parameters -> query: Union[str, list], data: Union[tuple, list]
            Returns -> None
        """
        if isinstance(query, str):
            self.cursor.execute(query, data)
        else:
            for i in range(len(query)):
                self.cursor.execute(query[i], data[i])
        self.connection.commit()

    def fetch_data_from_database(self, query: str, data: Optional[tuple] = None) -> list:
        """
            Method for fetching data from single or multiple tables in database.
            Parameters -> query: str, data: Union[tuple, None]
            Returns -> list
        """
        if data is None:
            self.cursor.execute(query)
        else:
            self.cursor.execute(query, data)
        return self.cursor.fetchall()


db = Database()

