"""Module to invoke business logic for getting details of individual employee."""

from business.employee_business import EmployeeBusiness
from models.database import db
from utils.custom_error_handler import custom_error_handler
from utils.responses import SuccessResponse

class GetIndividualEmployeeController:
    """
        Class for invoking business logic for getting details of individula employee.
        ...
        Methods
        -------
        get_individual_employee(): dict -> method for  getting details of individual employee.
    """
    @custom_error_handler
    def get_individual_employee(self, emp_id: str) -> dict:
        """
            Method for  getting details of individual employee.
            Parameter -> emp_id: str, employee_data: dict
            Return type -> dict
        """
        employee_business_obj = EmployeeBusiness(db)
        employee_business_obj.get_employee_data(emp_id)
        return SuccessResponse.jsonify_data("Employee data fetched successfully."), 200
