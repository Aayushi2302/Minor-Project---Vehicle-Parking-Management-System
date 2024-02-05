"""Module to invoke business logic for deleting employees."""

from business.employee_business import EmployeeBusiness
from models.database import db
from utils.custom_error_handler import custom_error_handler
from utils.responses import SuccessResponse

class DeleteEmployeeController:
    """
        Class for invoking business logic for deleting employees.
        ...
        Methods
        -------
        delete_employee(): dict -> method taking employee id and sending it to business layer.
    """
    @custom_error_handler
    def delete_employee(self, emp_id: str) -> dict:
        """
            Method taking employee id and sending it to business layer to delete.
            Parameter -> employee_id: str
            Return type -> dict
        """
        employee_business_obj = EmployeeBusiness(db)
        employee_business_obj.deactivate_employee(emp_id)
        return SuccessResponse.jsonify_data("Employee deleted successfully."), 200