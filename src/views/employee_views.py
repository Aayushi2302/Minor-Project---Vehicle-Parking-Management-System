"""Module contaning views logic of employee controller."""

import shortuuid

from config.app_config import AppConfig
from config.prompts.prompts import Prompts
from config.query import TableHeader
from controller.employee_controller import EmployeeController
from controller.parking_controller.vehicle_type import VehicleType
from utils.common_helper import CommonHelper
from utils.decorators import error_handler, looper
from utils.input_validator.parking_controller_validator import ParkingControllerValidator
from utils.input_validator.user_controller_validator import UserControllerValidator
from views.parking_views.parking_slot_views import ParkingSlotViews
from views.parking_views.slot_booking_views import SlotBookingViews
from views.parking_views.vehicle_type_views import VehicleTypeViews

class EmployeeViews:
    """
        Class containing views related to employee controller.
        ...
        Attributes:
        ----------
        employee_controller_obj : EmployeeController
        vehicle_type_obj : VehicleType
        common_helper_obj : CommonHelper
        parking_slot_views_obj : ParkingSlotViews
        vehicle_type_views_obj : VehicleTypeViews
        slot_booking_obj : SlotBooking
        new_data : str
        updated_field : str
        username : str, None

        Methods:
        -------
        customer_registration_form() -> for taking inputs for registering customer.
        view_customer_details() -> to view customer details.
        customer_details_updation_form() -> to take inputs for updating customer details.
        manage_profile_menu() -> menu to manage personal profile of employees.
        employee_menu -> for showing menu operations.
        update_menu() -> menu shown for updating customer details.
    """
    def __init__(self, username: str) -> None:
        """
            Method for constructing employee views obj.
            Paramter -> self, username: str
            Return type -> None
        """
        super().__init__()
        self.employee_controller_obj = EmployeeController()
        self.vehicle_type_obj = VehicleType()
        self.common_helper_obj = CommonHelper()
        self.parking_slot_views_obj = ParkingSlotViews()
        self.vehicle_type_views_obj = VehicleTypeViews()
        self.slot_booking_views_obj = SlotBookingViews()
        self.new_data = None
        self.updated_field = None
        self.username = username

    def customer_registration_form(self) -> None:
        """
            Method to take input for customer registration.
            Parameter -> self
            Return type -> None
        """
        print(Prompts.CUSTOMER_DETAILS_INPUT)
        cust_id = "CUST" + shortuuid.ShortUUID().random(length = 5)
        cust_name = UserControllerValidator.input_name()
        cust_mobile_number = UserControllerValidator.input_mobile_number()
        cust_vehicle_number = ParkingControllerValidator.input_vehicle_number()

        print(Prompts.INPUT_TYPE_NAME)
        data = self.vehicle_type_obj.get_all_vehicle_type()
        if not data:
            print(Prompts.ZERO_RECORD.format("Vehicle Type"))
            return

        self.vehicle_type_views_obj.view_vehicle_type()

        choice = int(input(Prompts.ENTER_CHOICE))

        if choice > len(data) or choice < 1:
            print(Prompts.INVALID_INPUT)
        else:
            type_id = data[choice-1][0]
            cust_data = (cust_id, cust_name, cust_mobile_number, cust_vehicle_number, type_id)
            self.employee_controller_obj.register_customer(cust_data)
            print(Prompts.CUSTOMER_CREATION_SUCCESSFUL + "\n")

    def view_customer_details(self) -> None:
        """
            Method to view customer details.
            Parameter -> self
            Return type -> None
        """
        data = self.employee_controller_obj.get_customer_details()
        if not data:
            print(Prompts.ZERO_RECORD.format("Customer"))
        else:
            header = TableHeader.CUSTOMER_DETAIL_HEADER
            self.common_helper_obj.display_table(data, header)

    @error_handler
    def customer_details_updation_form(self) -> None:
        """
            Method to take input and show output for customer details updation.
            Parameter -> self
            Return type -> None
        """
        if not self.employee_controller_obj.get_customer_details():
            print(Prompts.CANNOT_UPDATE_RECORD + "\n")
            return

        self.view_customer_details()
        print("\n" + Prompts.INPUT_DETAILS_FOR_UPDATION + "\n")
        cust_vehicle_no = ParkingControllerValidator.input_vehicle_number()

        while True:
            if self.update_menu():
                break

            result = self.employee_controller_obj.\
                        update_customer_details(cust_vehicle_no, self.updated_field, self.new_data)

            if result == -1:
                print(Prompts.CUSTOMER_DOES_NOT_EXIST + "\n")
            elif result == 0:
                print(Prompts.BOOKING_RECORD_NOT_FOUND + "\n")
            elif result == 1:
                print(Prompts.NO_UPDATION_FOR_CHECKOUT_VEHICLE + "\n")
            else:
                print(Prompts.CUSTOMER_UPDATION_SUCCESSFUL + "\n")

    @looper
    @error_handler
    def manage_profile_menu(self) -> bool:
        """
            Method for managing profile menu.
            Parameter -> self
            Return type -> bool
        """
        print("\n" + Prompts.MANAGE_PROFILE_MENU)
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

    @looper
    @error_handler
    def employee_menu(self) -> bool:
        """
            Method to handle employee menu operations.
            Parameter -> self
            Return type -> bool
        
        """
        print("\n" + Prompts.EMPLOYEE_MENU)
        choice = input(Prompts.ENTER_CHOICE)
        match choice:
            case '1':
                self.customer_registration_form()
            case '2':
                self.customer_details_updation_form()
            case '3':
                self.view_customer_details()
            case '4':
                self.parking_slot_views_obj.view_parking_slots()
            case '5':
                self.slot_booking_views_obj.book_parking_slot()
            case '6':
                self.slot_booking_views_obj.vacate_parking_slot()
            case '7':
                self.slot_booking_views_obj.view_booking_details()
            case '8':
                self.vehicle_type_views_obj.view_vehicle_type()
            case '9':
                self.manage_profile_menu()
            case '10':
                print(Prompts.SUCCESSFUL_LOGOUT + "\n")
                return True
            case _:
                print(Prompts.INVALID_INPUT)
        return False

    def update_menu(self) -> bool:
        """
            Method for managing customer update menu operations.
            Parameter -> self
            Return type -> bool
        """
        print(Prompts.CUSTOMER_DETAIL_UPDATE_MENU)
        choice = input(Prompts.ENTER_CHOICE)
        match choice:
            case '1':
                print(Prompts.NEW_DETAIL_INPUT.format("Name"))
                self.new_data = UserControllerValidator.input_name()
                self.updated_field = AppConfig.NAME_ATTR
            case '2':
                print(Prompts.NEW_DETAIL_INPUT.format("Mobile No."))
                self.new_data = UserControllerValidator.input_mobile_number()
                self.updated_field = AppConfig.MOBILE_NO_ATTR
            case '3':
                print(Prompts.NEW_DETAIL_INPUT.format("Out Date"))
                self.new_data = ParkingControllerValidator.input_out_date()
                self.updated_field = AppConfig.OUT_DATE_ATTR
            case '4':
                return True
            case _:
                print(Prompts.INVALID_INPUT)
        return False
