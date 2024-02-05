"""Module contaning controller logic for managing customer details."""

from config.app_config import AppConfig
from config.query import QueryConfig
from models.database import db

class CustomerController:
    """ 
        Class containing method for managing employee related operations.
        ...

        Methods:
        -------
        register_customer() -> method to regsiter customer.
        get_cust_id_from_vehicle_no() -> method to get customer id.
        get_customer_details() -> method to get customer details.
        update_customer_details() -> method to update customer details.
        get_booking_details_from_cust_id() -> method to get booking details from customer id.
    """

    def get_cust_id_from_vehicle_no(self, vehicle_no: str) -> list:
        """
            Method to get customer id.
            Parameter -> self, vehicle_no: str
            Return type -> list
        """
        data =  db.fetch_data_from_database(
                    QueryConfig.FETCH_CUSTOMER_ID_AND_TYPE_ID_FROM_VEHICLE_NO,
                    (vehicle_no, )
                )
        return data

    def update_customer_details(self, cust_vehicle_no: str,
                                updated_field: str, new_data: str) -> int:
        """
            Method to update customer details.
            Parameter -> self, cust_vehicle_no: str, updated_field: str, new_data: str
            Return type -> int
        """
        data = self.get_cust_id_from_vehicle_no(cust_vehicle_no)
        if not data:
            return -1

        cust_id = data[0][0]

        if updated_field in (AppConfig.NAME_ATTR, AppConfig.MOBILE_NO_ATTR):
            query_for_updation = QueryConfig.UPDATE_CUSTOMER_DETAIL.format(updated_field)
            db.save_data_to_database(
                    query_for_updation,
                    (new_data, cust_id)
                )
            return 2

        else:
            data = self.get_booking_details_from_cust_id(cust_id)
            if not data:
                return 0

            booking_id = data[len(data)-1][0]
            out_time = data[len(data)-1][1]

            if out_time != AppConfig.DEFAULT_OUT_TIME:
                return 1
            else:
                query_for_updation = QueryConfig.UPDATE_SLOT_BOOKING_DETAIL.format(updated_field)

                db.save_data_to_database(
                        query_for_updation,
                        (new_data, booking_id)
                    )
                return 2

    def get_booking_details_from_cust_id(self, cust_id: str) -> list:
        """
            Method to get booking details from customer id.
            Parameter -> self, cust_id: str
            Return type -> list
        """
        data =  db.fetch_data_from_database(
                    QueryConfig.FETCH_BOOKING_DETAIL_FROM_CUSTOMER_ID,
                    (cust_id, )
                )
        return data
