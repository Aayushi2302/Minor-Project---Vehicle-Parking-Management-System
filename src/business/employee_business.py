"""Module containing business logic related to employees."""

from mysql import connector

from config.app_config import AppConfig
from config.query import QueryConfig
from config.regex_pattern import RegexPattern
from models.database import Database
from utils.common_helper import (generate_shortuuid,
                                 generate_random_password,
                                 get_constraint_failed_attribute,
                                 regex_validation)
from utils.custom_exceptions import (CustomBaseException,
                                     DataAlreadyExists,
                                     DBException,
                                     DataNotFound,
                                     InvalidRegex)

class EmployeeBusiness:
    """
        Class containing business logic related to employees.
        ...
        Methods
        -------
        register_employee(): None -> method used to register employees.
        get_all_employee_details(): list -> method to get a list of all existing employees.
        get_employee_default_password(): dict -> method to get the default password of an employee.
        get_employee_data(): dict -> method to get the data of a particular employee if exists.
        update_employee_details(): int -> method to update the details of a particular employee.
        deactivate_employee(): None -> method to deactivate a particular employee.
    """
    def __init__(self, db: Database) -> None:
        """Constructor of employee business."""
        self.db = db

    def __check_for_invalid_employee_id(self, emp_id) -> None:
        result = regex_validation(RegexPattern.EMPLOYEE_ID_REGEX, emp_id)

        if not result:
            raise InvalidRegex(422, "Unprocessable Entity", "Employee ID is not as per required standard.")

    def register_employee(self, auth_data: tuple, employee_data: tuple) -> str:
        """
            Method to register employee.
            Parameter -> auth_data: tuple, employee_data: tuple
            Return type -> str
        """
        try:
            emp_id = generate_shortuuid("EMP")
            emp_password = generate_random_password()

            employee_data = (emp_id, ) + employee_data
            auth_data = (emp_id, emp_password) + auth_data

            query = [QueryConfig.CREATE_EMPLOYEE_CREDENTIALS, QueryConfig.CREATE_EMPLOYEE_DETAILS]
            data =  [auth_data, employee_data]
            self.db.save_data_to_database(
                query,
                data
            )

        except connector.IntegrityError as error:
            constraint_failed_attribute = get_constraint_failed_attribute(error.msg)
            self.db.cursor.execute(QueryConfig.ROLLBACK_QUERY)
            raise DataAlreadyExists(409, "Conflict", f"Entered {constraint_failed_attribute} already exist.")

        except connector.Error:
            raise DBException(500, "Internal Server Error", "Something went wrong with the server.")

    def get_all_employees_details(self) -> list:
        """
            Method to get a list of all existing employees.
            Parameter -> None
            Return type -> list
        """
        try:
            data = self.db.fetch_data_from_database(QueryConfig.VIEW_EMPLOYEE_DETAIL)
            return data
        except connector.Error:
            raise DBException(500, "Internal Server Error", "Something went wrong with the server.")

    def get_employee_default_password(self, emp_id: str) -> str:
        """
            Method to get default password for a particular employee.
            Parameter -> emp_id: str
            Return type -> str
        """
        try:
            self.__check_for_invalid_employee_id(emp_id)
            data =  self.db.fetch_data_from_database(
                        QueryConfig.FETCH_DEFAULT_PASSWORD_FROM_EMPID,
                        (emp_id, )
                    )

            if not data:
                raise DataNotFound(404, "Not Found", "Given employee does not exist.")

            if data[0]["password_type"] != AppConfig.DEFAULT_PASSWORD:
                raise CustomBaseException(403, "Forbidden", "Password for given employee has been already changed.")
            return data[0]
        except connector.Error:
            raise DBException(500, "Internal Server Error", "Something went wrong with the server.")

    def get_employee_data(self, emp_id: str) -> dict:
        """
            Method to get employee data.
            Parameter -> emp_id: str
            Return type -> list
        """
        try:
            self.__check_for_invalid_employee_id(emp_id)
            data =  self.db.fetch_data_from_database(
                        QueryConfig.FETCH_EMP_FROM_EMP_ID,
                        (emp_id, )
                    )
            if not data:
                return data
            return data[0]
        except connector.Error:
            raise DBException(500, "Internal Server Error", "Something went wrong with the server.") 

    def update_employee_details(self,
                                emp_id: str,
                                auth_table: tuple,
                                employee_table: tuple
    ) -> int:
        """
            Method to update employee details.
            Parameter -> emp_id: str, auth_data: tuple, employee_data: tuple
            Return type -> int
        """
        try:
            self.__check_for_invalid_employee_id(emp_id)
            data = self.get_employee_data(emp_id)

            if not data or data["status"] == AppConfig.STATUS_INACTIVE:
                raise DataNotFound(404, "Not Found", "Given employee does not exist.")

            role = data["role"]

            if role == AppConfig.ADMIN_ROLE:
                raise CustomBaseException(403, "Forbidden", "Cannot update employee.")

            query = [ QueryConfig.UPDATE_EMPLOYEE_CREDENTIAL_FROM_EMP_ID,
                        QueryConfig.UPDATE_EMPLOYEE_DETAIL_FROM_EMP_ID]
            data = [auth_table, employee_table]
            self.db.save_data_to_database(
                query,
                data
            )

        except connector.IntegrityError as error:
            constraint_failed_attribute = get_constraint_failed_attribute(error.msg)
            self.db.cursor.execute(QueryConfig.ROLLBACK_QUERY)
            raise DataAlreadyExists(409, "Conflict", f"Entered {constraint_failed_attribute} already exist.")

        except connector.Error:
            raise DBException(500, "Internal Server Error", "Something went wrong with the server.") 

    def deactivate_employee(self, emp_id: str) -> None:
        """
            Method to deactivate employee.
            Parameter -> emp_id: str
            Return type -> None
        """
        try:
            self.__check_for_invalid_employee_id(emp_id)
            data =  self.get_employee_data(emp_id)

            if not data or data["status"] == AppConfig.STATUS_INACTIVE:
                raise DataNotFound(404, "Not Found", "Given employee does not exist.")

            role = data[0]["role"]

            if role == AppConfig.ADMIN_ROLE:
                raise CustomBaseException(403, "Forbidden", "Cannot delete employee.")

            self.db.save_data_to_database(
                QueryConfig.DELETE_EMPLOYEE_FROM_EMP_ID,
                (AppConfig.STATUS_INACTIVE, emp_id)
            )

        except connector.Error as error:
            raise DBException(500, "Internal Server Error", "Something went wrong with the server.")