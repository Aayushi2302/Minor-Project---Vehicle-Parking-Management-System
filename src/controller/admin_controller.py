"""Module for maintaining all the methods or functionalities of Admin."""

from config.app_config import AppConfig
from config.query import QueryConfig
from models.database import db

class AdminController:
    """
        This class contains all the functionalities that user can perform on Employee.
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

    def update_employee_details(self, emp_email: str, updated_field: str, new_data: str) -> int:
        data = self.get_employee_data(emp_email)
        if not data:
            return -1

        emp_id = data[0][0]
        status = data[0][1]
        role = data[0][2]

        if role == AppConfig.ADMIN_ROLE:
            return -2
        elif status == AppConfig.STATUS_INACTIVE:
            return -3
        else:
            if updated_field in (AppConfig.ROLE_ATTR, AppConfig.USERNAME_ATTR):
                query = QueryConfig.UPDATE_EMPLOYEE_CREDENTIAL_FROM_EMP_ID.format(updated_field)
            else:
                query = QueryConfig.UPDATE_EMPLOYEE_DETAIL_FROM_EMP_ID.format(updated_field)
            db.save_data_to_database(
                query,
                (new_data, emp_id)
            )
            return 1

    def get_all_employees(self) -> list:
        """
            Method to display employee details.
            Parameter -> self
            Return type -> bool
        """
        data = db.fetch_data_from_database(QueryConfig.VIEW_EMPLOYEE_DETAIL)
        return data

    def get_default_password_for_employee(self, emp_email: str) -> int:
        data = db.fetch_data_from_database(
                    QueryConfig.FETCH_EMP_ID_FROM_EMAIL,
                    (emp_email, )
                )
        if not data:
            return []
        else:
            emp_id = data[0][0]
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

    def remove_employee(self, emp_email: str, updated_field: str, new_data: str) -> int:
        data = self.get_employee_data(emp_email)
        if not data:
            return -1

        emp_id = data[0][0]
        status = data[0][1]
        role = data[0][2]

        if role == AppConfig.ADMIN_ROLE:
            return 0
        elif status == new_data:
            return 1
        else:
            query = QueryConfig.UPDATE_EMPLOYEE_DETAIL_FROM_EMP_ID.format(updated_field)
            db.save_data_to_database(
                query,
                (new_data, emp_id)
            )
            return 2
