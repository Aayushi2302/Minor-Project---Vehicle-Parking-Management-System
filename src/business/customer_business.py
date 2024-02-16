"""Module containing business logic for operations on customer."""

from mysql import connector

from src.business.vehicle_type_business import VehicleTypeBusiness
from src.config.app_config import AppConfig
from src.config.query import QueryConfig
from src.config.regex_pattern import RegexPattern
from src.models.database import Database
from src.helpers.common_helper import generate_shortuuid, get_constraint_failed_attribute, regex_validation
from src.utils.custom_exceptions import AppException, DBException


class CustomerBusiness:
    """
        Class containing business logic for operations on customer.
        ...
        Attributes
        ----------
        db: Database Object

        Methods
        -------
        __check_for_valid_customer_id(): None -> method to validate customer id.
        register_customer(): None -> method to register a new customer.
        get_all_customers(): list -> method to get a list of all existing customers.
        get_individual_customer(): list -> method to get the details of a particular customer.
        update_customer_details(): None -> method to update the details of existing customer.
        deactivate_customer(): None -> method to deactivate existing customer.
    """
    def __init__(self, db: Database) -> None:
        """Constructor for customer business."""
        self.db = db
        self.vehicle_type_business = VehicleTypeBusiness(db)

    def __check_for_valid_customer_id(self, customer_id: str) -> None:
        """
            Method to validate customer id.
            Parameters -> customer_id: str
            Returns -> None
        """
        result = regex_validation(RegexPattern.CUSTOMER_ID_REGEX, customer_id)

        if not result:
            raise AppException(422, "Unprocessable Entity", "Customer ID is not as per required standard.")

    def register_customer(self, customer_data: tuple, type_name: str) -> None:
        """
            Method to register a new customer.
            Parameters -> customer_data: tuple
            Returns -> str
        """
        try:

            data = self.vehicle_type_business.get_vehicle_type_id_from_type_name(type_name)

            if not data:
                raise AppException(403, "Forbidden", "Vehicle type does not exist")

            type_id = data[0]["type_id"]
            customer_id = generate_shortuuid("CUST")
            customer_data = (customer_id,) + customer_data + (type_id, )

            self.db.save_data_to_database(
                QueryConfig.CREATE_CUSTOMER,
                customer_data
            )

        except connector.IntegrityError as error:
            failed_attribute = get_constraint_failed_attribute(error.msg)
            raise AppException(409, "Conflict", f"Customer {failed_attribute} already exist.")

        except connector.Error as error:
            print(error)
            raise DBException(500, "Internal Server Error", "Something went wrong with the server.")

    def get_all_customers(self) -> list:
        """
            Method to get the list of all existing customers.
            Parameters -> None
            Returns -> list
        """
        try:
            data = self.db.fetch_data_from_database(QueryConfig.VIEW_CUSTOMER_DETAIL)
            return data

        except connector.Error:
            raise DBException(500, "Internal Server Error", "Something went wrong with the server.")

    def get_individual_customer(self, customer_id: str) -> list:
        """
            Method to get details of customer from customer id.
            Parameters -> customer_id: str
            Returns -> list
        """
        try:
            data = self.db.fetch_data_from_database(
                QueryConfig.FETCH_CUSTOMER_DATA_FROM_CUSTOMER_ID,
                (customer_id,)
            )
            return data

        except connector.Error:
            raise DBException(500, "Internal Server Error", "Something went wrong with the server.")

    def get_individual_customer_details(self, customer_id: str) -> list:
        """
            Method to get details of customer from customer id.
            Parameters -> customer_id: str
            Returns -> list
        """
        try:
            data = self.db.fetch_data_from_database(
                QueryConfig.FETCH_CUSTOMER_DETAILS_FROM_CUSTOMER_ID,
                (customer_id,)
            )
            return data

        except connector.Error as error:
            print(error)
            raise DBException(500, "Internal Server Error", "Something went wrong with the server.")

    def update_customer_details(self, customer_id: str, customer_data: tuple) -> None:
        """
            Method to update customer details.
            Parameters -> customer_id: str, customer_data: tuple
            Returns -> None
        """
        try:

            self.__check_for_valid_customer_id(customer_id)
            data = self.get_individual_customer(customer_id)

            if not data:
                raise AppException(404, "Not Found", "Customer data not found.")

            if data[0]["status"] == "inactive":
                raise AppException(403, "Forbidden", "Cannot update deleted customer record.")

            self.db.save_data_to_database(
                QueryConfig.UPDATE_CUSTOMER_DETAIL,
                customer_data
            )

        except connector.IntegrityError as error:
            failed_attribute = get_constraint_failed_attribute(error.msg)
            raise AppException(409, "Conflict", f"Customer {failed_attribute} already exist.")

        except connector.Error:
            raise DBException(500, "Internal Server Error", "Something went wrong with the server.")

    def deactivate_customer(self, customer_id: str) -> None:
        """
            Method to deactivate customer.
            Parameters -> customer_id: str
            Returns -> None
        """
        try:

            self.__check_for_valid_customer_id(customer_id)
            data = self.get_individual_customer(customer_id)

            if not data:
                raise AppException(404, "Not Found", "Customer data not found.")

            if data[0]["status"] == "inactive":
                raise AppException(403, "Forbidden", "Customer does not exist.")

            self.db.save_data_to_database(
                QueryConfig.DELETE_CUSTOMER_FROM_CUSTOMER_ID,
                (AppConfig.STATUS_INACTIVE, customer_id)
            )

        except connector.Error:
            raise DBException(500, "Internal Server Error", "Something went wrong with the server.")
