from config.query import QueryConfig
from models.database import db

class EmployeeController:
    def register_customer(self, cust_data: tuple) -> None:
        """Method to register customer.""" 
        db.save_data_to_database(
            QueryConfig.CREATE_CUSTOMER,
            cust_data
        )
    
    def get_cust_id_from_vehicle_no(self, vehicle_no: str) -> list:
        data =  db.fetch_data_from_database(
                    QueryConfig.FETCH_CUSTOMER_ID_AND_TYPE_ID_FROM_VEHICLE_NO,
                    (vehicle_no, )
                )
        return data

    def get_customer_details(self) -> list:
        """Method to view customer details."""
        data =  db.fetch_data_from_database(QueryConfig.VIEW_CUSTOMER_DETAIL)
        return data
    
    def update_customer_details(self, updated_field: str, new_data: str, cust_id: str) -> None:
        query_for_updating_customer_data = QueryConfig.UPDATE_CUSTOMER_DETAIL.format(updated_field)
        db.save_data_to_database(
            query_for_updating_customer_data,
            (new_data, cust_id)
        )

    def get_booking_details_from_cust_id(self, cust_id: str) -> list:
        data =  db.fetch_data_from_database(
                    QueryConfig.FETCH_BOOKING_DETAIL_FROM_CUSTOMER_ID,
                    (cust_id, )
                )
        return data
    
    def update_out_date(self, updated_field: str, new_data: str, booking_id: str) -> None:
        query_for_updating_out_date = QueryConfig.UPDATE_SLOT_BOOKING_DETAIL.format(updated_field)
        db.save_data_to_database(
            query_for_updating_out_date,
            (new_data, booking_id)
        )