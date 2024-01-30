from business.employee_business import EmployeeBusiness
from models.database import db
from utils.custom_error_handler import custom_error_handler
from utils.responses import SuccessResponse

class GetDefaultPasswordController:

    @custom_error_handler
    def get_default_password(self, emp_id: str):
        employee_business_obj = EmployeeBusiness(db)
        response = employee_business_obj.get_employee_default_password(emp_id)
        return SuccessResponse.jsonify_data("Default password fetched successfully.", response), 200
