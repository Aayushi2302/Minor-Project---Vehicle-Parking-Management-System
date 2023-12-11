"""Module for handling admin menu related logic and user interactions."""
import logging
import random
import string
import shortuuid

from config.app_config import AppConfig
from config.prompts.prompts import Prompts
from config.query import TableHeader
from controller.admin_controller import AdminController
from utils.common_helper import CommonHelper
from utils.error_handler import error_handler
from utils.input_validator.user_controller_validator import UserControllerValidator
from views.parking_views.parking_slot_views import ParkingSlotViews
from views.parking_views.parking_status_views import ParkingStatusViews
from views.parking_views.vehicle_type_views import VehicleTypeViews

logger = logging.getLogger(__name__)

class AdminViews:
    """
        Class for performing admin menu related interactions.
        ...
        Attributes
        ----------
        username : str
        admin_controller_obj : AdminController
        common_helper_obj : CommonHelper
        parking_status_obj = ParkingStatus

        Methods
        -------
        admin_menu_operations() -> Method to perform admin tasks.
        admin_menu() -> Method for managing admin menu.
        vehicle_type_menu() -> Method for managing vehcile type menu.
        parking_slot_menu() -> Method for managing parking slot menu.
        parking_status_menu() -> Method for managing parking status menu.
        manage_profile_menu() -> Method for managing profile menu.
    """
    def __init__(self, username: str = None) -> None:
        self.updated_field = None
        self.username = username
        self.new_data = None
        self.admin_controller_obj = AdminController()
        self.common_helper_obj = CommonHelper()
        self.parking_slot_views_obj = ParkingSlotViews()
        self.vehicle_type_views_obj = VehicleTypeViews()
        self.parking_status_views_obj = ParkingStatusViews()

    def admin_menu_operations(self) -> None:
        """
            Method to perfrom admin tasks.
            Parameter -> self
            Return type -> None
        """
        print("\n" + Prompts.ADMIN_MENU_WELCOME_MESSAGE + "\n")
        while True:
            print("\n" + Prompts.ADMIN_MENU)
            if self.admin_menu():
                break
    
    def employee_registration_form(self, role: str = None) -> None:
        print(Prompts.INPUT_EMPLOYEE_DETAILS + "\n")

        emp_id = "EMP" + shortuuid.ShortUUID().random(length = 5)
        print(emp_id)
        emp_name = UserControllerValidator.input_name()
        emp_username = UserControllerValidator.input_username()
        characters = string.ascii_letters + string.digits + "@#$&%"
        emp_password = ''.join(random.choice(characters) for _ in range(8))
        print(emp_password)
        emp_age = UserControllerValidator.input_age()
        emp_gender = UserControllerValidator.input_gender()
        emp_role = UserControllerValidator.input_role(role)
        emp_mobile_number = UserControllerValidator.input_mobile_number()
        emp_email_address = UserControllerValidator.input_email_address()
        
        auth_data = (emp_id, emp_username, emp_password, emp_role)
        employee_data = (emp_id, emp_name, emp_age, emp_gender, emp_mobile_number, emp_email_address)
        self.admin_controller_obj.register_employee(auth_data, employee_data)
        print(Prompts.EMPLOYEE_REGISTRATION_SUCCESSFUL + "\n")

    def view_employee_details(self) -> None:
        data = self.admin_controller_obj.get_all_employees()
        if not data:
            print(Prompts.ZERO_RECORD.format("Employee"))
        else:
            header = TableHeader.EMPLOYEE_DETAIL_HEADER
            self.common_helper_obj.display_table(data, header)

    def employee_updation_form(self) -> None:
        if not self.admin_controller_obj.get_all_employees():
            print(Prompts.CANNOT_UPDATE_RECORD + "\n")
            return
            
        self.view_employee_details()
        print("\n" + Prompts.INPUT_DETAILS_FOR_UPDATION + "\n")
        emp_email = UserControllerValidator.input_email_address()
        data = self.admin_controller_obj.get_employee_data(emp_email)

        if not data:
            print(Prompts.DETAILS_NOT_EXIST + "\n")
        else:
            emp_id = data[0][0]
            status = data[0][1]
            role = data[0][2]
    
            if role == AppConfig.ADMIN_ROLE:
                print(Prompts.CANNOT_UPDATE_ADMIN + "\n")
                return
            if status == AppConfig.STATUS_INACTIVE:
                print(Prompts.UPDATE_DETAILS_FOR_INACTIVE_STATUS + "\n")
            else:
                while True:
                    if self.employee_update_menu():
                        break
                    self.admin_controller_obj.update_employee_details(self.updated_field, self.new_data, emp_id)
                    print(Prompts.EMPLOYEE_UPDATION_SUCCESSFUL + "\n")

    
    def view_default_password(self) -> None:
        if not self.admin_controller_obj.get_all_employees():
            print(Prompts.CANNOT_UPDATE_RECORD + "\n")
            return
            
        self.view_employee_details()
        emp_email = UserControllerValidator.input_email_address()
        data = self.admin_controller_obj.get_default_password_for_employee(emp_email)

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
        if not self.admin_controller_obj.get_all_employees():
            print(Prompts.CANNOT_PERFORM_DELETION + "\n")
            return

        self.view_employee_details()
        print("\n" + Prompts.INPUT_DETAILS_FOR_REMOVAL + "\n")
        emp_email = UserControllerValidator.input_email_address()
        data = self.admin_controller_obj.get_employee_data(emp_email)

        if not data:
            print(Prompts.DETAILS_NOT_EXIST + "\n")
        else:
            emp_id = data[0][0]
            status = data[0][1]
            role = data[0][2]
            
            if role == AppConfig.ADMIN_ROLE:
                print(Prompts.CANNOT_REMOVE_ADMIN + "\n")
                return
            if status == AppConfig.STATUS_INACTIVE:
                print(Prompts.UPDATE_DETAILS_FOR_INACTIVE_STATUS)
            else:
                status = AppConfig.STATUS_INACTIVE
                self.admin_controller_obj.remove_employee(AppConfig.STATUS_ATTR, status, emp_id)
                print(Prompts.EMPLOYEE_REMOVAL_SUCCESSFUL + "\n")

    @error_handler
    def admin_menu(self) -> bool:
        """
            Method for managing admin menu.
            Parameter -> self
            Return type -> bool
        """
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
                while True:
                    print("\n" + Prompts.MANAGE_VEHICLE_TYPE_MENU)
                    if self.vehicle_type_views_obj.vehicle_type_menu():
                        break
            case '7':
                while True:
                    print("\n" + Prompts.MANAGE_PARKING_SLOT_MENU)
                    if self.parking_slot_views_obj.parking_slot_menu():
                        break
            case '8':
                while True:
                    print("\n" + Prompts.VIEW_PARKING_STATUS_MENU + "\n")
                    if self.parking_status_views_obj.parking_status_menu():
                        break
            case '9':
                while True:
                    print("\n" + Prompts.MANAGE_PROFILE_MENU)
                    if self.manage_profile_menu():
                        break
            case '10':
                print(Prompts.SUCCESSFUL_LOGOUT + "\n")
                return True
            case _:
                print(Prompts.INVALID_INPUT)
        return False

    @error_handler
    def manage_profile_menu(self) -> bool:
        """
            Method for managing profile menu.
            Parameter -> self
            Return type -> bool
        """
        menu_profile_choice = input(Prompts.ENTER_CHOICE)
        match menu_profile_choice:
            case '1':
                self.common_helper_obj.view_individual_employee_details(self.username)
            case '2':
                self.common_helper_obj.create_new_password(self.username)
            case '3':
                return True
            case _:
                print(Prompts.INVALID_INPUT)
        return False

    @error_handler
    def employee_update_menu(self) -> bool:
        """
            Method to manage employee update menu.
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
