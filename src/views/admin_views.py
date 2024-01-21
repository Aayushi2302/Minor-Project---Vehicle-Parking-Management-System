"""Module containing views logic of admin controller."""

import logging
import random
import string
from typing import Optional
import shortuuid

from config.app_config import AppConfig
from config.prompts.prompts import Prompts
from config.query import TableHeader
from controller.employee_controller import EmployeeController
from utils.common_helper import CommonHelper
from utils.decorators import error_handler, looper
from utils.input_validator.user_controller_validator import UserControllerValidator
from views.employee_views import EmployeeViews
from views.parking_views.parking_slot_views import ParkingSlotViews
from views.parking_views.parking_status_views import ParkingStatusViews
from views.parking_views.vehicle_type_views import VehicleTypeViews

logger = logging.getLogger(__name__)

class AdminViews:
    """
        Class contaning views for admin controller.
        ...
        Attributes
        ----------
        updated_field : str
        username : str
        new_data : str
        employee_controller_obj : EmployeeController
        common_helper_obj : CommonHelper
        employee_views_obj : EmployeeViews
        parking_slot_views_obj : ParkingSlotViews
        vehicle_type_views_obj : VehicleTypeViews
        parking_status_views_obj : ParkingStatusViews

        Methods
        -------
        employee_registration_form() -> method for taking input for regestering employee.
        view_employee_details() -> method for viewing employee details.
        employee_updation_form() -> method to take inputs to update employee details.
        view_default_password() -> method to view default password of employee.
        employee_removal_form() -> method to remove employee.
        admin_menu() -> menu to handle admin operations.
        employee_update_menu() -> menu to handle employee update operations.
    """
    def __init__(self, username: Optional[str] = None) -> None:
        """
            Method to construct admin views object.
            Parameter -> self, username: str, None
            Return type -> None
        """
        self.updated_field = None
        self.username = username
        self.new_data = None
        self.employee_controller_obj = EmployeeController()
        self.common_helper_obj = CommonHelper()
        self.employee_views_obj = EmployeeViews(self.username)
        self.parking_slot_views_obj = ParkingSlotViews()
        self.vehicle_type_views_obj = VehicleTypeViews()
        self.parking_status_views_obj = ParkingStatusViews()

    def employee_registration_form(self, emp_role: Optional[str] = None) -> None:
        """
            Method to take input for regestering employee.
            Parameter -> self, emp_role: str, None
            Return type -> None
        """
        print(Prompts.INPUT_EMPLOYEE_DETAILS + "\n")

        emp_id = "EMP" + shortuuid.ShortUUID().random(length = 5)
        emp_name = UserControllerValidator.input_name()
        emp_username = UserControllerValidator.input_username()
        characters = string.ascii_letters + string.digits + "@#$&%"
        emp_password = ''.join(random.choice(characters) for _ in range(8))
        emp_age = UserControllerValidator.input_age()
        emp_gender = UserControllerValidator.input_gender()
        if not emp_role:
            emp_role = UserControllerValidator.input_role()
        emp_mobile_number = UserControllerValidator.input_mobile_number()
        emp_email_address = UserControllerValidator.input_email_address()

        auth_data = (emp_id, emp_username, emp_password, emp_role)
        employee_data = (emp_id, emp_name, emp_age, emp_gender,
                            emp_mobile_number, emp_email_address)
        self.employee_controller_obj.register_employee(auth_data, employee_data)
        print(Prompts.EMPLOYEE_REGISTRATION_SUCCESSFUL + "\n")

    def view_employee_details(self) -> None:
        """
            Method to view employee details.
            Parameter -> self
            Return type -> None
        """
        data = self.employee_controller_obj.get_all_employees()
        if not data:
            print(Prompts.ZERO_RECORD.format("Employee"))
        else:
            header = TableHeader.EMPLOYEE_DETAIL_HEADER
            self.common_helper_obj.display_table(data, header)

    @error_handler
    def employee_updation_form(self) -> bool:
        """
            Method to take inputs to update employee details.
            Parameter -> self
            Return type -> None
        """
        if not self.employee_controller_obj.get_all_employees():
            print(Prompts.CANNOT_UPDATE_RECORD + "\n")
            return

        self.view_employee_details()
        print("\n" + Prompts.INPUT_DETAILS_FOR_UPDATION + "\n")
        emp_email = UserControllerValidator.input_email_address()

        while True:
            if self.employee_update_menu():
                break

            result = self.employee_controller_obj.\
                        update_employee_details(emp_email, self.updated_field, self.new_data)

            if result == -1:
                print(Prompts.DETAILS_NOT_EXIST + "\n")
            elif result == -2:
                print(Prompts.CANNOT_UPDATE_ADMIN + "\n")
            elif result == -3:
                print(Prompts.UPDATE_DETAILS_FOR_INACTIVE_STATUS + "\n")
            else:
                print(Prompts.EMPLOYEE_UPDATION_SUCCESSFUL + "\n")

    def view_default_password(self) -> None:
        """
            Method to view default password of employee.
            Parameter -> self
            Return type -> None
        """
        if not self.employee_controller_obj.get_all_employees():
            print(Prompts.CANNOT_UPDATE_RECORD + "\n")
            return

        self.view_employee_details()
        emp_email = UserControllerValidator.input_email_address()
        data = self.employee_controller_obj.get_default_password_for_employee(emp_email)

        if not data:
            print(Prompts.DETAILS_NOT_EXIST + "\n")
        else:
            password_type = data[0][0]
            default_password = data[0][1]
            if password_type == AppConfig.PERMANENT_PASSWORD:
                print(Prompts.NO_DEFAULT_PASSWORD + "\n")
            else:
                print(Prompts.PRINT_DEFAULT_PASSWORD.format(default_password) + "\n")

    def employee_removal_form(self) -> None:
        """
            Method to update status for employee removal.
            Parameter -> self
            Return type -> None
        """
        if not self.employee_controller_obj.get_all_employees():
            print(Prompts.CANNOT_PERFORM_DELETION + "\n")
            return

        self.view_employee_details()
        print("\n" + Prompts.INPUT_DETAILS_FOR_REMOVAL + "\n")
        emp_email = UserControllerValidator.input_email_address()
        updated_field = AppConfig.STATUS_ATTR
        new_data = AppConfig.STATUS_INACTIVE
        result = self.employee_controller_obj.remove_employee(emp_email, updated_field, new_data)

        if result == -1:
            print(Prompts.DETAILS_NOT_EXIST + "\n")
        elif result == 0:
            print(Prompts.CANNOT_REMOVE_ADMIN + "\n")
        elif result == 1:
            print(Prompts.UPDATE_DETAILS_FOR_INACTIVE_STATUS + "\n")
        else:
            print(Prompts.EMPLOYEE_REMOVAL_SUCCESSFUL + "\n")

    @looper
    @error_handler
    def admin_menu(self) -> bool:
        """
            Method for managing admin menu operations.
            Parameter -> self
            Return type -> bool
        """
        print("\n" + Prompts.ADMIN_MENU_WELCOME_MESSAGE + "\n")
        print("\n" + Prompts.ADMIN_MENU)
        choice = input(Prompts.ENTER_CHOICE)
        match choice:
            case '1':
                self.employee_registration_form()
            case '2':
                self.employee_updation_form()
            case '3':
                self.view_employee_details()
            case '4':
                self.view_default_password()
            case '5':
                self.employee_removal_form()
            case '6':
                self.vehicle_type_views_obj.vehicle_type_menu()
            case '7':
                self.parking_slot_views_obj.parking_slot_menu()
            case '8':
                self.parking_status_views_obj.parking_status_menu()
            case '9':
                self.employee_views_obj.manage_profile_menu()
            case '10':
                print(Prompts.SUCCESSFUL_LOGOUT + "\n")
                return True
            case _:
                print(Prompts.INVALID_INPUT)
        return False


    def employee_update_menu(self) -> bool:
        """
            Method to manage employee update menu operations.
            Parameter -> self
            Return type -> bool
        """
        print("\n" + Prompts.EMPLOYEE_DETAIL_UPDATE_MENU)
        choice = input(Prompts.ENTER_CHOICE)
        match choice :
            case '1':
                print(Prompts.NEW_DETAIL_INPUT.format("Name"))
                self.new_data = UserControllerValidator.input_name()
                self.updated_field = AppConfig.NAME_ATTR
            case '2':
                print(Prompts.NEW_DETAIL_INPUT.format("Age"))
                self.new_data = UserControllerValidator.input_age()
                self.updated_field = AppConfig.AGE_ATTR
            case '3':
                print(Prompts.NEW_DETAIL_INPUT.format("Gender"))
                self.new_data = UserControllerValidator.input_gender()
                self.updated_field = AppConfig.GENDER_ATTR
            case '4':
                print(Prompts.NEW_DETAIL_INPUT.format("Mobile No."))
                self.new_data = UserControllerValidator.input_mobile_number()
                self.updated_field = AppConfig.MOBILE_NO_ATTR
            case '5':
                print(Prompts.NEW_DETAIL_INPUT.format("Email Address"))
                self.new_data = UserControllerValidator.input_email_address()
                self.updated_field = AppConfig.EMAIL_ADDRESS_ATTR
            case '6':
                print(Prompts.NEW_DETAIL_INPUT.format("Username"))
                self.new_data = UserControllerValidator.input_username()
                self.updated_field = AppConfig.USERNAME_ATTR
            case '7':
                print(Prompts.NEW_DETAIL_INPUT.format("Role"))
                self.new_data = UserControllerValidator.input_role()
                self.updated_field = AppConfig.ROLE_ATTR
            case '8':
                return True
            case _:
                print(Prompts.INVALID_INPUT)
        return False
