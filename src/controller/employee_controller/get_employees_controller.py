"""Module to invoke business logic for getting details of all employees."""

from business.employee_business import EmployeeBusiness
from models.database import db
from utils.custom_error_handler import custom_error_handler
from utils.responses import SuccessResponse


class GetEmployeesController:
    """
        Class for invoking business logic for getting all employee details.
        ...
        Methods
        -------
        get_all_employees(): tuple -> method getting employee data from business layer.
    """
    @custom_error_handler
    def get_all_employees(self) -> tuple:
        """
            Method getting employee data for all employee from business layer.
            Parameters -> None
            Returns -> dict
        """
        employee_business = EmployeeBusiness(db)
        response = employee_business.get_all_employees_details()
        return SuccessResponse.jsonify_data("Employees fetched successfully.", response), 200
