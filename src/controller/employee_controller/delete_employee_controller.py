"""Module to invoke business logic for deleting employees."""

from src.business.employee_business import EmployeeBusiness
from src.models.database import Database
from src.utils.custom_error_handler import custom_error_handler
from src.utils.responses import SuccessResponse


class DeleteEmployeeController:
    """
        Class for invoking business logic for deleting employees.
        ...
        Methods
        -------
        delete_employee(): tuple -> method taking employee id and sending it to business layer.
    """
    @custom_error_handler
    def delete_employee(self, emp_id: str) -> tuple:
        """
            Method taking employee id and sending it to business layer to delete.
            Parameters -> employee_id: str
            Returns -> tuple
        """
        db = Database()
        employee_business = EmployeeBusiness(db)
        employee_business.deactivate_employee(emp_id)
        return SuccessResponse.jsonify_data("Employee deleted successfully."), 200
