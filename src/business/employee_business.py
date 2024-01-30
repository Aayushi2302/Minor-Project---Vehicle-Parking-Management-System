from mysql import connector

from config.app_config import AppConfig
from config.query import QueryConfig
from config.regex_pattern import RegexPattern
from models.database import Database
from utils.common_helper import CommonHelper
from utils.custom_exceptions import CustomBaseException, DataAlreadyExists, DBException, DataNotFound, InvalidRegex

class EmployeeBusiness:

    def __init__(self, db: Database) -> None:
        self.db = db

    def register_employee(self, auth_data: tuple, employee_data: tuple) -> str:
        try:
            emp_id = CommonHelper.generate_shortuuid("EMP")
            emp_password = CommonHelper.generate_random_password()

            employee_data = (emp_id, ) + employee_data
            auth_data = (emp_id, emp_password) + auth_data

            query = [QueryConfig.CREATE_EMPLOYEE_CREDENTIALS, QueryConfig.CREATE_EMPLOYEE_DETAILS]
            data =  [auth_data, employee_data]
            self.db.save_data_to_database(
                query,
                data
            )
            return emp_id

        except connector.IntegrityError as error:
            constraint_failed_attribute = CommonHelper.get_constraint_failed_attribute(error.msg)
            self.db.cursor.execute("ROLLBACK")
            raise DataAlreadyExists(409, "Conflict", f"Entered {constraint_failed_attribute} already exist.")

        except connector.Error:
            raise DBException(500, "Internal Server Error", "Something went wrong with the server.")

    def get_all_employees_details(self) -> list:
        try:
            data = self.db.fetch_data_from_database(QueryConfig.VIEW_EMPLOYEE_DETAIL)

            if not data:
                raise DataNotFound(404, "Not Found", "Employee data not found.")

            return data
        except connector.Error:
            raise DBException(500, "Internal Server Error", "Something went wrong with the server.")

    def get_employee_default_password(self, emp_id: str) -> str:
        try:
            result = CommonHelper.input_validation(RegexPattern.EMPLOYEE_ID_REGEX, emp_id)
            
            if not result:
                raise InvalidRegex(422, "Unprocessable Entity", "Employee ID is not as per required standard.")

            data =  self.db.fetch_data_from_database(
                        QueryConfig.FETCH_DEFAULT_PASSWORD_FROM_EMPID,
                        (emp_id, )
                    )

            if not data:
                raise DataNotFound(404, "Not Found", "Given employee does not exist.")

            return data[0]
        except connector.Error:
            raise DBException(500, "Internal Server Error", "Something went wrong with the server.")

    def deactivate_employee(self, emp_id: str) -> None:
        try:
            result = CommonHelper.input_validation(RegexPattern.EMPLOYEE_ID_REGEX, emp_id)
            
            if not result:
                raise InvalidRegex(422, "Unprocessable Entity", "Employee ID is not as per required standard.")

            data =  self.db.fetch_data_from_database(
                        QueryConfig.FETCH_EMP_FROM_EMP_ID,
                        (emp_id, )
                    )
    
            if not data or data[0]["status"] == AppConfig.STATUS_INACTIVE:
                raise DataNotFound(404, "Not Found", "Given employee does not exist.")

            role = data[0]["role"]

            if role == AppConfig.ADMIN_ROLE:
                raise CustomBaseException(400, "Bad Request", "Cannot delete employee.")
            
            self.db.save_data_to_database(
                QueryConfig.DELETE_EMPLOYEE_FROM_EMP_ID,
                (AppConfig.STATUS_INACTIVE, emp_id)
            )

        except connector.Error as error:
            raise DBException(500, "Internal Server Error", "Something went wrong with the server.")