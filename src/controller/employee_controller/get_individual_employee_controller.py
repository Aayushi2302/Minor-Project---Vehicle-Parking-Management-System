"""Module to invoke business logic for getting details of individual employee."""

from src.business.employee_business import EmployeeBusiness
from src.models.database import db
from src.utils.custom_error_handler import custom_error_handler
from src.utils.responses import SuccessResponse


class GetIndividualEmployeeController:
    """
        Class for invoking business logic for getting details of individual employee.
        ...
        Methods
        -------
        get_individual_employee(): tuple -> method for  getting details of individual employee.
    """
    @custom_error_handler
    def get_individual_employee(self, emp_id: str) -> tuple:
        """
            Method for  getting details of individual employee.
            Parameters -> emp_id: str
            Returns -> tuple
        """
        employee_business = EmployeeBusiness(db)
        data = employee_business.get_individual_employee_data(emp_id)
        return SuccessResponse.jsonify_data("Employee data fetched successfully.", data), 200
