"""Module to invoke business logic for getting default password of a particular employee."""

from src.business.employee_business import EmployeeBusiness
from src.models.database import db
from src.utils.custom_error_handler import custom_error_handler
from src.utils.responses import SuccessResponse


class GetDefaultPasswordController:
    """
        Class for invoking business logic for getting default password.
        ...
        Methods
        -------
        get_default_password(): tuple -> method taking employee id and sending it to business layer.
    """
    @custom_error_handler
    def get_default_password(self, emp_id: str) -> tuple:
        """
            Method taking employee id and sending it to business layer to retrieve default password.
            Parameters -> emp_id: str
            Returns -> tuple
        """
        employee_business = EmployeeBusiness(db)
        response = employee_business.get_employee_default_password(emp_id)
        return SuccessResponse.jsonify_data("Default password fetched successfully.", response), 200
