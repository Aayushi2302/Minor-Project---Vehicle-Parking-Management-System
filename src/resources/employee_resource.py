import shortuuid
import string
import random
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from schemas.employee_schema import EmployeeSchema

from controller.employee_controller import EmployeeController
from models.database import db
from utils.decorators import error_handler, role_based_access
from utils.role_mapping import RoleMapping

blp = Blueprint("employee", __name__ , description="Employee related operations.")

@blp.route("/employee")
class EmployeeOperations(MethodView):
    @role_based_access((RoleMapping["ADMIN"]))
    @error_handler
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
        emp_id = "EMP" + shortuuid.ShortUUID().random(length = 5)
        characters = string.ascii_letters + string.digits + "@#$&%"
        emp_password = ''.join(random.choice(characters) for _ in range(8))
        employee_controller_obj = EmployeeController(db)
        employee_controller_obj.register_employee(
            (
                emp_id,
                employee_data["username"],
                emp_password,
                employee_data["role"]
            ),
            (
                emp_id,
                employee_data["name"],
                employee_data["age"],
                employee_data["gender"],
                employee_data["mobile_no"],
                employee_data["email_address"]  
            )
        )
        employee_data["emp_id"] = emp_id
        employee_data["status"] = "active"
        return employee_data

    @role_based_access((RoleMapping["ADMIN"]))
    @error_handler
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
        employee_controller_obj = EmployeeController(db)
        emp_data = employee_controller_obj.get_all_employees()
        if not emp_data:
            abort(404, "Resource not found.")
        return emp_data

@blp.route("/employee/<string:employee_id>")
class IndividualEmployeeOperations(MethodView):
    @role_based_access((RoleMapping["ADMIN"]))
    @error_handler
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
    def put(self, employee_id, employee_data):
        employee_controller_obj = EmployeeController(db)
        result = employee_controller_obj.update_employee_details(
                    employee_id,
                    (
                        employee_data["username"],
                        employee_data["role"]
                    ),
                    (
                        employee_data["name"],
                        employee_data["age"],
                        employee_data["gender"],
                        employee_data["mobile_no"],
                        employee_data["email_address"]
                    )
                )

        if result == -1:
            abort(404, "Employee does not exist.")
        elif result == 0:
            abort(400, "Employee is already inactive so cannot update details.")
        else:
            employee_data["emp_id"] = employee_id
            return employee_data
        