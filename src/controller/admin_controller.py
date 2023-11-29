"""Module for maintaining all the methods or functionalities of Admin."""
import random
import string
import shortuuid

from config.prompts.prompts import Prompts
from config.query import TableHeader
from views.employee_update_views import EmployeeUpdateViews
from models.database import db
from models.db_helper import DBHelper
from controller.parking_controller.parking_slots import ParkingSlot
from controller.parking_controller.vehicle_type import VehicleType
from utils.common_helper import CommonHelper
from utils.input_validator.user_controller_validator import UserControllerValidator

class AdminController(VehicleType, ParkingSlot):
    """
        This class contains all the functionalities that user can perform on Employee.
        Also this class inherits VehicleType and ParkingSlot class to implement further admin functionalities.
    """
    def __init__(self) -> None:
        self.common_helper_obj = CommonHelper()
        self.employee_update_views_obj = EmployeeUpdateViews()
        self.db_helper_obj = DBHelper()

    def register_employee(self, role: str = None) -> None:
        """
            Method to register employee and save their data to database.
            Parameter -> self, role: str = None
            Return type -> None
        """
        emp_id = "EMP" + shortuuid.ShortUUID().random(length = 5)
        emp_name = UserControllerValidator.input_name()
        emp_username = UserControllerValidator.input_username()
        characters = string.ascii_letters + string.digits + "@#$&%"
        emp_password = ''.join(random.choice(characters) for _ in range(8))
        emp_age = UserControllerValidator.input_age()
        emp_gender = UserControllerValidator.input_gender()
        emp_role = UserControllerValidator.input_role(role)
        emp_mobile_number = UserControllerValidator.input_mobile_number()
        emp_email_address = UserControllerValidator.input_email_address()
        data =  [
                    (emp_id, emp_username, emp_password, emp_role),
                    (emp_id, emp_name, emp_age, emp_gender, emp_mobile_number, emp_email_address)
                ]
        self.db_helper_obj.save_employee_details_to_multiple_table(data)
            
    def update_employee_details(self) -> bool:
        """
            Method to update employee details.
            Parameter -> self
            Return type -> bool
        """
        # self.employee_update_views_obj.employee_update_operations()
                          
    def view_employee_details(self) -> bool:
        """
            Method to display employee details.
            Parameter -> self
            Return type -> bool
        """
        data = self.db_helper_obj.get_employee_details()
        if not data:
            return False
        else:
            headers = TableHeader.EMPLOYEE_DETAIL_HEADER
            self.common_helper_obj.display_table(data, headers)
            return True

    def get_default_password_for_employee(self) -> list:
        """
            Method to return default password of employee to admin.
            Parameter -> self
            Return type -> list
        """
        emp_email = UserControllerValidator.input_email_address()
        emp_id = self.db_helper_obj.get_emp_id_from_email(emp_email)
        if not emp_id:
            return None
        else:
            emp_id = emp_id[0][0]
            data = self.db_helper_obj.get_default_password_from_emp_id(emp_id)
            return data

    def get_employee_data(self) -> list:
        """
            Method to get employee data to remove employee the employee.
            Parameter -> self
            Return type -> list
        """
        emp_email = UserControllerValidator.input_email_address()
        data =  self.db_helper_obj.get_emp_id_status_and_role_from_email(emp_email)
        if not data:
            return None
        else:
            return data
                
    def remove_employee(self, updated_field: str, status: str, emp_id: str) -> list:
        """
            Method to remove employee detail.
            Parameter -> self, updated_field: str, status: str, emp_id: str
            Return type -> None
        """
        self.db_helper_obj.update_employee_record(updated_field, status, emp_id)

