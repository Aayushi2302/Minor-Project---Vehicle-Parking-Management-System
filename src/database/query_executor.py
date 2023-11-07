"""
    Module for performing all the CRUD operations on the tables in the database.
"""
import logging
from sqlite3 import IntegrityError
from sqlite3 import OperationalError
from sqlite3 import ProgrammingError

from config.statements.config import Config
from config.query.query_config import QueryConfig
from database.db_connector import DatabaseConnection
from logs.logs_config import LogConfig

logger = logging.getLogger('query_executor')

class QueryExecutor:
    """
        Class containing methods for executing database queries fetched from QueryConfig.
    """
    @staticmethod
    def create_all_tables() -> None:
        """
            Method for creating all tables of database.
        """
        try:
            with DatabaseConnection(Config.database_path) as connection:
                cursor = connection.cursor()
                cursor.execute(QueryConfig.query_for_authentication_table_creation)
                logger.info(LogConfig.successful_authentication_table_creation_info_prompt)
                cursor.execute(QueryConfig.query_for_employee_table_creation)
                logger.info(LogConfig.successful_employee_table_creation_info_prompt)
                cursor.execute(QueryConfig.query_for_customer_table_creation)
                logger.info(LogConfig.successful_vehicle_type_table_creation_info_prompt)
                cursor.execute(QueryConfig.query_for_parking_slot_table_creation)
                logger.info(LogConfig.successful_parking_slot_table_creation_info_prompt)
                cursor.execute(QueryConfig.query_for_vehicle_type_table_creation)
                logger.info(LogConfig.successful_customer_table_creation_info_prompt)
                cursor.execute(QueryConfig.query_for_slot_booking_table_creation)
                logger.info(LogConfig.successful_slot_booking_table_creation_info_prompt)
        except OperationalError as e:
            logger.debug(e)
            print(Config.operational_error_message_prompt + "\n")
        except ProgrammingError as e:
            logger.debug(e)
            print(Config.programming_error_message_prompt + "\n")
        except Exception as e:
            logger.debug(e)
            print(Config.general_exception_message_prompt + "\n")

    @staticmethod
    def fetch_data_from_database(query: str, data: tuple = None) -> list:
        """
            Method to fetch all the data from the database with the query and data passed as parameter.
        """
        try:
            with DatabaseConnection(Config.database_path) as connection:
                cursor = connection.cursor()
                if not data:
                    cursor.execute(query)
                else:
                    cursor.execute(query, data)
                data = cursor.fetchall()
                logger.info(LogConfig.data_fetched_from_database_successful_info_prompt)
                return data
        except IntegrityError as e:
            logger.debug(e)
            print(Config.integrity_error_message_prompt + "\n")
        except OperationalError as e:
            logger.debug(e)
            print(Config.operational_error_message_prompt + "\n")
        except ProgrammingError as e:
            logger.debug(e)
            print(Config.programming_error_message_prompt + "\n")
        except Exception as e:
            logger.debug(e)
            print(Config.general_exception_message_prompt + "\n")
     
    @staticmethod
    def save_data_in_database(query: str, data: tuple, success_message: str) -> None:
        """
            Method to save data to database with query and data passed as parameter.
        """
        try:
            with DatabaseConnection(Config.database_path) as connection:
                cursor = connection.cursor()
                cursor.execute(query, data)
                connection.commit()
                print(success_message)
                logger.info(LogConfig.data_saved_to_database_successful_info_prompt)
        except IntegrityError as e:
            logger.debug(e)
            print(Config.integrity_error_message_prompt + "\n")
        except OperationalError as e:
            logger.debug(e)
            print(Config.operational_error_message_prompt + "\n")
        except ProgrammingError as e:
            logger.debug(e)
            print(Config.programming_error_message_prompt + "\n")
        except Exception as e:
            logger.debug(e)
            print(Config.general_exception_message_prompt + "\n")