"""Module for handling admin menu related logic and user interactions."""
import logging

from config.app_config import AppConfig
from config.prompts.prompts import Prompts
from controller.admin_controller import AdminController
from controller.parking_controller.parking_status import ParkingStatus
from utils.common_helper import CommonHelper
from utils.error_handler import error_handler

logger = logging.getLogger(__name__)

#TODO : apply clear screen wherever required

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
    def __init__(self, username: str) -> None:
        print(Prompts.ADMIN_MENU_WELCOME_MESSAGE + "\n")
        self.username = username
        self.admin_controller_obj = AdminController()
        self.common_helper_obj = CommonHelper()
        self.parking_status_obj = ParkingStatus()

    def admin_menu_operations(self) -> None:
        """
            Method to perfrom admin tasks.
            Parameter -> self
            Return type -> None
        """
        while True:
            print("\n" + Prompts.ADMIN_MENU)
            if self.admin_menu():
                break
    
    def __register_employee(self) -> None:
        print(Prompts.INPUT_EMPLOYEE_DETAILS + "\n")
        self.admin_controller_obj.register_employee()
        print(Prompts.EMPLOYEE_REGISTRATION_SUCCESSFUL + "\n")

    def __view_employee_details(self) -> None:
        data_exist = self.admin_controller_obj.view_employee_details()
        if not data_exist:
            print(Prompts.ZERO_RECORD.format("Employee"))

    def __update_employee_details(self) -> None:
        if not self.admin_controller_obj.view_employee_details():
            print(Prompts.CANNOT_UPDATE_RECORD + "\n")
    
    def __view_default_password(self) -> None:
        data = self.admin_controller_obj.get_default_password_for_employee()
        if not data:
            print(Prompts.DETAILS_NOT_EXIST + "\n")
        else:
            password_type = data[0][0]
            default_password = data[0][1]
            if password_type is AppConfig.PERMANENT_PASSWORD:
                print(Prompts.NO_DEFAULT_PASSWORD + "\n")
            else:
                print(Prompts.PRINT_DEFAULT_PASSWORD.format(default_password) + "\n")

    def __remove_employee(self) -> None:
        if not self.admin_controller_obj.view_employee_details():
            print(Prompts.CANNOT_PERFORM_DELETION + "\n")
        print("\n" + Prompts.INPUT_DETAILS_FOR_REMOVAL + "\n")
        data = self.admin_controller_obj.get_employee_data()
        if not data:
            print(Prompts.DETAILS_NOT_EXIST + "\n")
        else:
            emp_id = data[0][0]
            status = data[0][1]
            role = data[0][2]
            if role is AppConfig.ADMIN_ROLE:
                print(Prompts.CANNOT_REMOVE_ADMIN + "\n")
            if status is AppConfig.STATUS_INACTIVE:
                print(Prompts.UPDATE_DETAILS_FOR_INACTIVE_STATUS)
            else:
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
                self.__register_employee()
            case '2':
                self.__update_employee_details()
            case '3':
                self.__view_employee_details()
            case '4':
                self.__view_default_password()
            case '5':
                self.__remove_employee()
            case '6':
                # while True:
                #     print("\n" + Prompts.MANAGE_VEHICLE_TYPE_MENU)
                #     if self.vehicle_type_menu():
                #         break
                pass
            case '7':
                # while True:
                #     print("\n" + Prompts.MANAGE_PARKING_SLOT_MENU)
                #     if self.parking_slot_menu():
                #         break
                pass
            case '8':
                # while True:
                #     print("\n" + Prompts.VIEW_PARKING_STATUS_MENU + "\n")
                #     if self.parking_status_menu():
                #         break
                pass
            case '9':
                # while True:
                #     print("\n" + Prompts.MANAGE_PROFILE_MENU)
                #     if self.manage_profile_menu():
                #         break
                pass
            case '10':
                print(Prompts.SUCCESSFUL_LOGOUT + "\n")
                return True
            case _:
                print(Prompts.INVALID_INPUT)
        return False

    @error_handler
    def vehicle_type_menu(self) -> bool:
        """ 
            Method for managing vehicle type menu.
            Parameter -> self
            Return type -> bool
        """
        vehicle_type_choice = input(Prompts.ENTER_CHOICE)
        match vehicle_type_choice:
            case '1':
                self.admin_controller_obj.register_vehicle_type()
            case '2':
                self.admin_controller_obj.update_vehicle_price_per_hour()
            case '3':
                self.admin_controller_obj.view_vehicle_type()
            case '4' :
                return True
            case _ :
                print(Prompts.INVALID_INPUT)
        return False

    @error_handler
    def parking_slot_menu(self) -> bool:
        """
            Method for managing parking slot menu.
            Parameter -> self
            Return type -> bool
        """
        parking_slot_choice = input(Prompts.ENTER_CHOICE)
        match parking_slot_choice:
            case '1':
                self.admin_controller_obj.register_or_activate_parking_slot()
            case '2':
                self.admin_controller_obj.deactivate_parking_slot()
            case '3':
                self.admin_controller_obj.view_parking_slot()
            case '4':
                self.admin_controller_obj.remove_parking_slot()
            case '5' :
                return True
            case _ :
                print(Prompts.INVALID_INPUT)
        return False

    @error_handler
    def parking_status_menu(self) -> bool:
        """
            Method for managing parking status menu.
            Parameter -> self
            Return type -> bool
        """
        see_status_choice = input(Prompts.ENTER_CHOICE)
        match see_status_choice:
            case '1':
                self.parking_status_obj.view_current_date_status()
            case '2':
                self.parking_status_obj.view_current_year_status()
            case '3':
                self.parking_status_obj.view_total_vehicle_entries()
            case '4':
                return True
            case _ :
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
