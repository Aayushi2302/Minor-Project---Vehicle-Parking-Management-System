import pymysql

from src.config.app_config import AppConfig
from src.config.query import QueryConfig
from src.models.database import Database
from src.utils.custom_exceptions import DBException


class CustomerHelper:

    def __init__(self, db: Database) -> None:
        self.db = db

    def get_cust_id_from_vehicle_no(self, vehicle_no: str) -> list:
        """
            Method to get customer id.
            Parameter -> self, vehicle_no: str
            Return type -> list
        """
        try:
            data = self.db.fetch_data_from_database(
                        QueryConfig.FETCH_CUSTOMER_ID_AND_TYPE_ID_FROM_VEHICLE_NO,
                        (vehicle_no, )
                    )
            return data

        except pymysql.Error:
            raise DBException(500, "Internal Server Error", "Something went wrong with the server.")