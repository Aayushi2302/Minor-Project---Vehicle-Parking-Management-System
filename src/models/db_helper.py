"""Module containing methods for performing operations on database through queries."""
from config.prompts.prompts import Prompts
from config.query import QueryConfig
from models.database import db

class DBHelper:
    """
        Class containting methods for fetching and saving data to database based on queries.
        These methods are helper methods used in various controllers for performing
        CRUD operations.
        ...
        Methods
        -------
        get_employee_credentials() -> Method for getting employee credentails.

    """
    def get_employee_credentails(self, username: str, status: str) -> list:
        """
            Method for getting employee credentails.
            Parameter -> self, username: str, status: str
            Return type -> list
        """
        data =  db.fetch_data_from_database(
                    QueryConfig.FETCH_EMPLOYEE_CREDENTIALS,
                    (username, status)
                )
        return data
    
    def get_employee(self, role: str, status: str) -> list:
        """
            Method for fetching employee from role and status.
            Parameter -> self, role: str, status: str
            Return type -> list
        """
        data =  db.fetch_data_from_database(
                    QueryConfig.FETCH_EMPID_FROM_ROLE_AND_STATUS,
                    (role, status)
                )
        return data
    
    def update_password(self, new_password: str, password_type: str, username: str) -> None:
        """
            Method for saving default password to database.
            Parameter -> self, new_password: str, password_type: str, username: str
            Return type -> None
        """
        db.save_data_in_database(
            QueryConfig.UPDATE_DEFAULT_PASSWORD,
            (new_password, password_type, username),
        )
   
    def get_single_employee_details(self, username: str) -> list:
        """
            Method for fetching single employee details.
            Parameter -> self, username: str
            Return type -> list
        """
        data =  db.fetch_data_from_database(
                    QueryConfig.VIEW_SINGLE_EMPLOYEE_DETAIL,
                    (username, )
                )
        return data

    def get_customer_id_and_type_id(self, cust_vehicle_no: str) -> list:
        """
            Method for fetching customer id and type id.
            Parameter -> self, cust_vehicle_no: str
            Return type -> list
        """
        data =  db.fetch_data_from_database(
                    QueryConfig.FETCH_CUSTOMER_ID_AND_TYPE_ID_FROM_VEHICLE_NO,
                    (cust_vehicle_no, )
                )
        return data
    
    def get_booking_details(self, customer_id: str) -> list:
        """
            Method for fetching booking details.
            Parameter -> self, customer_id: str
            Return type -> list
        """
        data =  db.fetch_data_from_database(
                    QueryConfig.FETCH_BOOKING_DETAIL_FROM_CUSTOMER_ID,
                    (customer_id, )
                )
        return data
    
    def update_out_date(self, updated_field: str, new_data: str, booking_id: str) -> None:
        """
            Method for updating out_date to database.
            Parameter -> self, updated_field: str, new_data: str, booking_id: str
            Return type -> None
        """
        query_for_updating_out_date = QueryConfig.UPDATE_SLOT_BOOKING_DETAIL.format(updated_field)
        db.save_data_in_database(
            query_for_updating_out_date,
            (new_data, booking_id)
        )
    
    def update_customer_data(self, updated_field: str, new_data: str, customer_id: str) -> None:
        """
            Method for updating customer data to database.
            Parameter -> self, updated_field: str, new_data: str, customer_id: str
            Return type -> None
        """
        query_for_updating_customer_data = QueryConfig.UPDATE_CUSTOMER_DETAIL.format(updated_field)
        db.save_data_in_database(
            query_for_updating_customer_data,
            (new_data, customer_id)
        )
    
    def save_employee_details_to_multiple_table(self, data: list) -> None:
        """
            Method for saving employee details to database in multiple tables.
            Parameter -> self, data: list
            Return type -> None
        """
        queries = [QueryConfig.CREATE_EMPLOYEE_CREDENTIALS, QueryConfig.CREATE_EMPLOYEE_DETAILS]
        db.save_data_to_database(
            queries,
            data
        )

    def get_employee_details(self) -> list:
        """
            Method for fetching employee details.
            Parameter -> self
            Return type -> list
        """
        data =  db.fetch_data_from_database(
                    QueryConfig.VIEW_EMPLOYEE_DETAIL
                )
        return data
    
    def get_emp_id_from_email(self, emp_email: str) -> list:
        """
            Method for fetching employee id from email.
            Parameter -> self, emp_email: str
            Return type -> list
        """
        data =  db.fetch_data_from_database(
                    QueryConfig.FETCH_EMP_ID_FROM_EMAIL,
                    (emp_email, )
                )
        return data
    
    def get_emp_id_status_and_role_from_email(self, emp_email: str) -> list:
        """
            Method for fetching employee id, status and role from email.
            Parameter -> self, emp_email: str
            Return type -> list
        """
        data =  db.fetch_data_from_database(
                    QueryConfig.FETCH_EMP_ID_STATUS_AND_ROLE_FROM_EMAIL,
                    (emp_email, )
                )
        return data
    
    def get_default_password_from_emp_id(self, emp_id: str) -> list:
        """
            Method for fetching employee default password from emp_id.
            Parameter -> self, emp_id: str
            Return type -> list
        """
        data =  db.fetch_data_from_database(
                    QueryConfig.FETCH_DEFAULT_PASSWORD_FROM_EMPID,
                    (emp_id, )
                )
        return data
    
    def update_employee_record(self, updated_field: str, status: str, emp_id: str) -> None:
        """
            Method for updating employee record.
            Parameter -> self, status: str, emp_id: str
            Return type -> None
        """
        query = QueryConfig.UPDATE_EMPLOYEE_DETAIL_FROM_EMP_ID.format(updated_field)
        db.save_data_in_database(
            query,
            (status, emp_id)
        )
    
    def update_employee_details(self, query: str, new_data: str, emp_id: str) -> None:
        """
            Method for updating employee details.
            Parameter -> self, query: str, new_data: str, emp_id: str
            Return type -> None
        """
        db.save_data_to_database(
            query,
            (new_data, emp_id)
        )
        