"""Module to invoke business logic for getting default password of a particular employee."""

from business.employee_business import EmployeeBusiness
from models.database import db
from utils.custom_error_handler import custom_error_handler
from utils.responses import SuccessResponse

class GetDefaultPasswordController:
    """
        Class for invoking business logic for getting default password.
        ...
        Methods
        -------
        get_default_password(): dict -> method taking employee id and sending it to business layer.
    """
    @custom_error_handler
    def get_default_password(self, emp_id: str) -> dict:
        """
            Method taking employee id and sending it to business layer to retrieve default password.
            Parameter -> employee_id: str
            Return type -> dict
        """
        employee_business_obj = EmployeeBusiness(db)
        response = employee_business_obj.get_employee_default_password(emp_id)
        return SuccessResponse.jsonify_data("Default password fetched successfully.", response), 200
