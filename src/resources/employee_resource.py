"""Module having end points related to employee."""

from flask.views import MethodView
from flask_smorest import Blueprint
from schemas.employee_schema import EmployeeSchema, EmployeeResponseSchema, EmployeeDefaultPasswordSchema

from config.app_config import AppConfig
from controller.employee_controller.add_employee_controller import AddEmployeeController
from controller.employee_controller.get_employees_controller import GetEmployeesController
from controller.employee_controller.get_default_password_controller import GetDefaultPasswordController
from controller.employee_controller.get_individual_employee_controller import GetIndividualEmployeeController
from controller.employee_controller.update_employee_controller import UpdateEmployeeController
from controller.employee_controller.delete_employee_controller import DeleteEmployeeController
from utils.decorators import role_based_access
from utils.role_mapping import RoleMapping

blp = Blueprint("employee", __name__ , description="Employee related operations.")

@blp.route("/v1/employees")
class EmployeeOperations(MethodView):
    """
        Class containing various methods applicable to /v1/employees route.
        ...
        Methods
        -------
        POST
        GET
    """
    @blp.doc(parameters = [AppConfig.BLP_DOC_PARAMETERS])
    @blp.arguments(EmployeeSchema)
    @blp.response(201, EmployeeResponseSchema)
    @role_based_access((RoleMapping["admin"]))
    def post(self, employee_data: dict) -> dict:
        """
            Method for performing post operation on employees.
            ...
            On Success -> Follows EmployeeResponseSchema and returns success message.
            On Failure -> Returns success = False and error message.
        """
        return AddEmployeeController().add_employee(employee_data)

    @blp.doc(parameters = [AppConfig.BLP_DOC_PARAMETERS])
    @blp.response(200, EmployeeSchema(many=True))
    @role_based_access((RoleMapping["admin"]))
    def get(self) -> dict:
        """
            Method for performing get operation on employees.
            ...
            On Success -> Follows EmployeeSchema and employee related details.
            On Failure -> Returns success = False and error message.
        """
        return GetEmployeesController().get_all_employees()

@blp.route("/v1/employee/<string:emp_id>")
class EmployeeIndividualOperations(MethodView):
    """
        Class containing various methods applicable to /v1/employee/{employee_id} route.
        ...
        Methods
        -------
        PUT
        GET
        DELETE  
    """
    @blp.doc(parameters = [AppConfig.BLP_DOC_PARAMETERS])
    @blp.response(200, EmployeeResponseSchema)
    @role_based_access((RoleMapping["admin"]))
    def put(self, employee_data: dict, emp_id: str) -> dict:
        """
            Method for performing update operation on a particular employee.
            ...
            On Success -> Follows EmployeeResponseSchema and returns success message.
            On Failure -> Returns success = False and error message.
        """
        return UpdateEmployeeController().update_employee(emp_id, employee_data)

    @blp.doc(parameters = [AppConfig.BLP_DOC_PARAMETERS])
    @blp.response(200, EmployeeSchema)
    @role_based_access((RoleMapping["admin"]))
    def get(self, emp_id: str) -> dict:
        """
            Method for feteching details of a particular employee.
            ...
            On Success -> Follows EmployeeSchema and returns a particular employee detail.
            On Failure -> Returns success = False and error message.
        """
        return GetIndividualEmployeeController().get_individual_employee(emp_id)

    @blp.doc(parameters = [AppConfig.BLP_DOC_PARAMETERS])
    @blp.response(200, EmployeeResponseSchema)
    @role_based_access((RoleMapping["admin"]))
    def delete(self, emp_id: str) -> dict:
        """
            Method for performing delete operation on a particular employee.
            ...
            On Success -> Follows EmployeeResponseSchema and returns success message.
            On Failure -> Returns success = False and error message.
        """
        return DeleteEmployeeController().delete_employee(emp_id)

@blp.route("/v1/employee/default-password/<string:emp_id>")
class EmployeeDefaultPassword(MethodView):
    """
        Class containing various methods applicable to /v1/employee/default-password/{employee_id} route.
        ...
        Methods
        -------
        GET
    """
    @role_based_access((RoleMapping["admin"]))
    @blp.doc(parameters = [AppConfig.BLP_DOC_PARAMETERS])
    @blp.response(200, EmployeeDefaultPasswordSchema)
    def get(self, emp_id: str) -> dict:
        """
            Method for fetching default password of a particular employee.
            ...
            On Success -> Follows EmployeeDefaultPasswordSchema and returns default password.
            On Failure -> Returns success = False and error message.
        """
        return GetDefaultPasswordController().get_default_password(emp_id)
