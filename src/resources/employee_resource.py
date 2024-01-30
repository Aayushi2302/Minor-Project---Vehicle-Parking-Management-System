from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint
from schemas.employee_schema import EmployeeSchema, EmployeeDefaultPasswordSchema, EmployeeDeleteSchema

from controller.employee_controller.add_employee_controller import AddEmployeeController
from controller.employee_controller.get_employees_controller import GetEmployeesController
from controller.employee_controller.get_default_password_controller import GetDefaultPasswordController
from controller.employee_controller.delete_employee_controller import DeleteEmployeeController
from utils.decorators import role_based_access
from utils.role_mapping import RoleMapping

blp = Blueprint("employee", __name__ , description="Employee related operations.")

@blp.route("/employee")
class EmployeeOperations(MethodView):
    @role_based_access((RoleMapping["ADMIN"]))
    @blp.doc(
        parameters = [
        {
            'name': 'Authorization',
            'in': 'header',
            'description': 'Authorization: Bearer <access_token>',
            'required': 'true'
        }
    ])
    @blp.arguments(EmployeeSchema)
    @blp.response(201, EmployeeSchema)
    def post(self, employee_data):
        add_employee_controller_obj = AddEmployeeController()
        return add_employee_controller_obj.add_employee(employee_data)

    @role_based_access((RoleMapping["ADMIN"]))
    @blp.doc(
        parameters = [
        {
            'name': 'Authorization',
            'in': 'header',
            'description': 'Authorization: Bearer <access_token>',
            'required': 'true'
        }
    ])
    @blp.response(200, EmployeeSchema(many=True))
    def get(self):
        query_param = request.args.get("all")
        if query_param == "True":
            get_employees_controller_obj = GetEmployeesController()
            return get_employees_controller_obj.get_all_employees()
        
@blp.route("/employee/<string:emp_id>")
class EmployeeIndividualOperations(MethodView):
    @role_based_access((RoleMapping["ADMIN"]))
    @blp.doc(
        parameters = [
        {
            'name': 'Authorization',
            'in': 'header',
            'description': 'Authorization: Bearer <access_token>',
            'required': 'true'
        }
    ])
    @blp.response(200, EmployeeDeleteSchema)
    def delete(self, emp_id: str):
        delete_employee_controller_obj = DeleteEmployeeController()
        return delete_employee_controller_obj.delete_employee(emp_id)


@blp.route("/employee/default-password/<string:emp_id>")
class EmployeeDefaultPassword(MethodView):
    @role_based_access((RoleMapping["ADMIN"]))
    @blp.doc(
        parameters = [
        {
            'name': 'Authorization',
            'in': 'header',
            'description': 'Authorization: Bearer <access_token>',
            'required': 'true'
        }
    ])
    @blp.response(200, EmployeeDefaultPasswordSchema)
    def get(self, emp_id: str):
        get_default_password_controller_obj = GetDefaultPasswordController()
        return get_default_password_controller_obj.get_default_password(emp_id)


# @blp.route("/employee/<string:employee_id>")
# class IndividualEmployeeOperations(MethodView):
#     @role_based_access((RoleMapping["ADMIN"]))
#     @error_handler
#     @blp.doc(
#         parameters = [
#         {
#             'name': 'Authorization',
#             'in': 'header',
#             'description': 'Authorization: Bearer <access_token>',
#             'required': 'true'
#         }
#     ])
#     @blp.arguments(EmployeeSchema)
#     @blp.response(201, EmployeeSchema)
#     def put(self, employee_id, employee_data):
#         employee_controller_obj = EmployeeController(db)
#         result = employee_controller_obj.update_employee_details(
#                     employee_id,
#                     (
#                         employee_data["username"],
#                         employee_data["role"]
#                     ),
#                     (
#                         employee_data["name"],
#                         employee_data["age"],
#                         employee_data["gender"],
#                         employee_data["mobile_no"],
#                         employee_data["email_address"]
#                     )
#                 )

#         if result == -1:
#             abort(404, "Employee does not exist.")
#         elif result == 0:
#             abort(400, "Employee is already inactive so cannot update details.")
#         else:
#             employee_data["emp_id"] = employee_id
#             return employee_data
        