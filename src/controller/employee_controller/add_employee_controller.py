"""Module to invoke business logic for adding or registering employees."""

from src.business.employee_business import EmployeeBusiness
from src.models.database import db
from src.utils.custom_error_handler import custom_error_handler
from src.utils.responses import SuccessResponse


class AddEmployeeController:
    """
        Class for invoking business logic for registering employees.
        ...
        Methods
        -------
        add_employee(): tuple -> method taking employee data and sending it to business layer.
    """
    @custom_error_handler
    def add_employee(self, employee_data: dict) -> tuple:
        """
            Method taking employee data and sending it to business layer to save.
            Parameters -> employee_data: dict
            Returns -> tuple
        """
        name = employee_data["name"]
        age = employee_data["age"]
        gender = employee_data["gender"]
        mobile_no = employee_data["mobile_no"]
        email = employee_data["email_address"]
        username = employee_data["username"]
        role = employee_data["role"]

        auth_table_data = (username, role)
        employee_table_data = (name, age, gender, mobile_no, email)

        employee_business = EmployeeBusiness(db)
        employee_business.register_employee(auth_table_data, employee_table_data)

        return SuccessResponse.jsonify_data("Employee created successfully."), 200
