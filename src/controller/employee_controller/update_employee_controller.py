"""Module to invoke business logic for updating details of employees."""

from business.employee_business import EmployeeBusiness
from models.database import db
from utils.custom_error_handler import custom_error_handler
from utils.responses import SuccessResponse

class UpdateEmployeeController:
    """
        Class for invoking business logic for updating employee details.
        ...
        Methods
        -------
        update_employee(): dict -> method for updating employee data for a particular employee.
    """
    @custom_error_handler
    def update_employee(self, emp_id: str, employee_data: dict) -> dict:
        """
            Method for updating employee data for a particular employee.
            Parameter -> emp_id: str, employee_data: dict
            Return type -> dict
        """
        name = employee_data["name"]
        age = employee_data["age"]
        gender = employee_data["gender"]
        mobile_no = employee_data["mobile_no"]
        email = employee_data["email"]
        username = employee_data["username"]
        role = employee_data["role"]

        auth_table_data = (username, role)
        employee_table_data = (name, age, gender, mobile_no, email)

        employee_business_obj = EmployeeBusiness(db)
        employee_business_obj.update_employee_details(emp_id, auth_table_data, employee_table_data)
        return SuccessResponse.jsonify_data("Employee updated successfully."), 200
