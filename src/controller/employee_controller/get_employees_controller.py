from business.employee_business import EmployeeBusiness
from models.database import db
from utils.custom_error_handler import custom_error_handler
from utils.responses import SuccessResponse

class GetEmployeesController:

    @custom_error_handler
    def get_all_employees(self) -> dict:
        employee_business_obj = EmployeeBusiness(db)
        response = employee_business_obj.get_all_employees_details()
        return SuccessResponse.jsonify_data("Employee Data fetched successfully.", response), 200
