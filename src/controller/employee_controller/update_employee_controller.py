"""Module to invoke business logic for updating details of employees."""

from src.business.employee_business import EmployeeBusiness
from src.models.database import db
from src.utils.custom_error_handler import custom_error_handler
from src.utils.responses import SuccessResponse


class UpdateEmployeeController:
    """
        Class for invoking business logic for updating employee details.
        ...
        Methods
        -------
        update_employee(): tuple -> method for updating employee data for a particular employee.
    """
    @custom_error_handler
    def update_employee(self, emp_id: str, employee_data: dict) -> tuple:
        """
            Method for updating employee data for a particular employee.
            Parameters -> emp_id: str, employee_data: dict
            Returns -> tuple
        """
        name = employee_data["name"]
        age = employee_data["age"]
        gender = employee_data["gender"]
        mobile_no = employee_data["mobile_no"]
        email = employee_data["email_address"]
        username = employee_data["username"]
        role = employee_data["role"]

        auth_table_data = (username, role, emp_id)
        employee_table_data = (name, age, gender, mobile_no, email, emp_id)

        employee_business = EmployeeBusiness(db)
        employee_business.update_employee_details(emp_id, auth_table_data, employee_table_data)
        return SuccessResponse.jsonify_data("Employee updated successfully."), 200
