from mysql import connector

from config.query import QueryConfig
from models.database import Database
from utils.custom_exceptions import DataAlreadyExists

class EmployeeBusiness:

    def __init__(self, db: Database) -> None:
        self.db = db

    def register_employee(self, auth_data: tuple, employee_data: tuple) -> None:
        try:
            query = [QueryConfig.CREATE_EMPLOYEE_CREDENTIALS, QueryConfig.CREATE_EMPLOYEE_DETAILS]
            data =  [auth_data, employee_data]
            self.db.save_data_to_database(
                query,
                data
            )
        except connector.IntegrityError:
            raise DataAlreadyExists(409, "Conflict", "User data already exist.")