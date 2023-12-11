"""Module for maintaining all the methods or functionalities of Admin."""

from config.app_config import AppConfig
from config.query import QueryConfig
from models.database import db

class AdminController:
    """
        This class contains all the functionalities that user can perform on Employee.
        Also this class inherits VehicleType and ParkingSlot class to implement further admin functionalities.
    """
    def register_employee(self, auth_data: tuple, employee_data: tuple) -> None:
        """
            Method to register employee and save their data to database.
            Parameter -> self, role: str = None
            Return type -> None
        """
        query = [QueryConfig.CREATE_EMPLOYEE_CREDENTIALS, QueryConfig.CREATE_EMPLOYEE_DETAILS]
        data =  [auth_data, employee_data]
        db.save_data_to_database(
            query,
            data
        )
            
    def update_employee_details(self, updated_field: str, new_data: str, emp_id: str) -> None:
        """
            Method to update employee details.
            Parameter -> self
            Return type -> bool
        """
        if updated_field in (AppConfig.ROLE_ATTR, AppConfig.USERNAME_ATTR):
            query = QueryConfig.UPDATE_EMPLOYEE_CREDENTIAL_FROM_EMP_ID.format(updated_field)
        else:
            query = QueryConfig.UPDATE_EMPLOYEE_DETAIL_FROM_EMP_ID.format(updated_field)
        db.save_data_to_database(
            query,
            (new_data, emp_id)
        )

    def get_all_employees(self) -> list:
        """
            Method to display employee details.
            Parameter -> self
            Return type -> bool
        """
        data = db.fetch_data_from_database(QueryConfig.VIEW_EMPLOYEE_DETAIL)
        return data

    def get_default_password_for_employee(self, emp_email: str) -> list:
        """
            Method to return default password of employee to admin.
            Parameter -> self
            Return type -> list
        """
        emp_id = db.fetch_data_from_database(
                    QueryConfig.FETCH_EMP_ID_FROM_EMAIL,
                    (emp_email, )
                )
        if not emp_id:
            return []
        else:
            emp_id = emp_id[0][0]
            data =  db.fetch_data_from_database(
                        QueryConfig.FETCH_DEFAULT_PASSWORD_FROM_EMPID,
                        (emp_id, )
                    )
            return data

    def get_employee_data(self, emp_email: str) -> list:
        """
            Method to get employee data to remove employee the employee.
            Parameter -> self
            Return type -> list
        """
        data =  db.fetch_data_from_database(
                    QueryConfig.FETCH_EMP_ID_STATUS_AND_ROLE_FROM_EMAIL,
                    (emp_email, )
                )
        return data
                
    def remove_employee(self, updated_field: str, status: str, emp_id: str) -> None:
        """
            Method to remove employee detail.
            Parameter -> self, updated_field: str, status: str, emp_id: str
            Return type -> None
        """
        query = QueryConfig.UPDATE_EMPLOYEE_DETAIL_FROM_EMP_ID.format(updated_field)
        db.save_data_to_database(
            query,
            (status, emp_id)
        )
