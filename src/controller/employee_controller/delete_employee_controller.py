from business.employee_business import EmployeeBusiness
from models.database import db
from utils.custom_error_handler import custom_error_handler
from utils.responses import SuccessResponse

class DeleteEmployeeController:

    @custom_error_handler
    def delete_employee(self, emp_id: str) -> dict:
        employee_business_obj = EmployeeBusiness(db)
        employee_business_obj.deactivate_employee(emp_id)
        return SuccessResponse.jsonify_data("Employee deleted successfully."), 200