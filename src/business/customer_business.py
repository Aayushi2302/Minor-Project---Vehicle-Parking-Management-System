from mysql import connector

from config.app_config import AppConfig
from config.query import QueryConfig
from config.regex_pattern import RegexPattern
from models.database import Database
from utils.common_helper import CommonHelper
from utils.custom_exceptions import DataAlreadyExists, DataNotFound, DBException, CustomBaseException, InvalidRegex

class CustomerBusiness:

    def __init__(self, db: Database) -> None:
        self.db = db

    def register_customer(self, customer_data: tuple) -> str:
        try:
            customer_id = CommonHelper.generate_shortuuid("CUST")

            customer_data = (customer_id, ) + customer_data

            self.db.save_data_to_database(
                QueryConfig.CREATE_CUSTOMER,
                customer_data
            )

            return customer_id
        
        except connector.IntegrityError as error:
            failed_attribute = CommonHelper.get_constraint_failed_attribute(error.msg)
            raise DataAlreadyExists(409, "Conflict", f"Customer {failed_attribute} already exist.")
        
        except connector.Error:
            raise DBException(500, "Internal Server Error", "Something went wrong with the server.")

    
    def get_all_customers(self) -> list:
        try:
            data =  self.db.fetch_data_from_database(QueryConfig.VIEW_CUSTOMER_DETAIL)

            if not data:
                raise DataNotFound(404, "Not Found", "Customer data not found.")

            return data

        except connector.Error:
            raise DBException(500, "Internal Server Error", "Something went wrong with the server.")

    def get_customer_details_from_customer_id(self, customer_id: str) -> dict:
        try:
            data =  self.db.fetch_data_from_database(
                        QueryConfig.FETCH_CUSTOMER_DATA_FROM_CUSTOMER_ID,
                        (customer_id, )
                    )
            return data[0]

        except connector.Error:
            raise DBException(500, "Internal Server Error", "Something went wrong with the server.")


    def update_customer_details(self, customer_id: str, customer_data: tuple, vehicle_type_name: str) -> dict:
        try:
            
            valid_id = CommonHelper.regex_validation(RegexPattern.CUSTOMER_ID_REGEX, customer_id)

            if not valid_id:
                raise InvalidRegex(422, "Unprocessable Entity", "Customer ID is not as per required standard.")

            data = self.get_customer_details_from_customer_id(customer_id)

            if not data:
                raise DataNotFound(404, "Not Found", "Customer data not found.")

            if data["status"] == "inactive":
                raise  CustomBaseException(400, "Bad Request", "Cannot update deleted customer record.")

            if data["type_name"] != vehicle_type_name:
                raise CustomBaseException(400, "Bad Request", "Cannot update type name.")

            self.db.save_data_to_database(
                QueryConfig.UPDATE_CUSTOMER_DETAIL,
                customer_data
            )

        except connector.IntegrityError as error:
            failed_attribute = CommonHelper.get_constraint_failed_attribute(error.msg)
            raise DataAlreadyExists(409, "Conflict", f"Customer {failed_attribute} already exist.")
  
        except connector.Error:
            raise DBException(500, "Internal Server Error", "Something went wrong with the server.")
    
    def deactivate_customer(self, customer_id: str) -> None:
        try:

            valid_id = CommonHelper.regex_validation(RegexPattern.CUSTOMER_ID_REGEX, customer_id)

            if not valid_id:
                raise InvalidRegex(422, "Unprocessable Entity", "Customer ID is not as per required standard.")
        
            data = self.get_customer_details_from_customer_id(customer_id)

            if not data:
                raise DataNotFound(404, "Not Found", "Customer data not found.")

            if data["status"] == "inactive":
                raise  CustomBaseException(400, "Bad Request", "Customer does not exist.")
        
            self.db.save_data_to_database(
                QueryConfig.DELETE_CUSTOMER_FROM_CUSTOMER_ID,
                (AppConfig.STATUS_INACTIVE, customer_id)
            )

        except connector.Error:
            raise DBException(500, "Internal Server Error", "Something went wrong with the server.")
        