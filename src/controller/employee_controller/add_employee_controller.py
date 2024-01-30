from business.employee_business import EmployeeBusiness
from models.database import db
from utils.custom_error_handler import custom_error_handler
from utils.responses import SuccessResponse

class AddEmployeeController:

    @custom_error_handler
    def add_employee(self, employee_data: dict) -> dict:
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
        employee_id = employee_business_obj.register_employee(auth_table_data, employee_table_data)
        employee_data["employee_id"] = employee_id
        return SuccessResponse.jsonify_data("Employee created successfully.", employee_data), 200
