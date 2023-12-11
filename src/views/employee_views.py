import shortuuid

from config.app_config import AppConfig
from config.prompts.prompts import Prompts
from config.query import TableHeader
from controller.employee_controller import EmployeeController
from controller.parking_controller.vehicle_type import VehicleType
from utils.common_helper import CommonHelper
from utils.error_handler import error_handler
from utils.input_validator.parking_controller_validator import ParkingControllerValidator
from utils.input_validator.user_controller_validator import UserControllerValidator
from views.parking_views.parking_slot_views import ParkingSlotViews
from views.parking_views.slot_booking_views import SlotBookingViews
from views.parking_views.vehicle_type_views import VehicleTypeViews

class EmployeeViews(SlotBookingViews):
    def __init__(self, username: str) -> None:
        super().__init__()
        self.employee_controller_obj = EmployeeController()
        self.vehicle_type_obj = VehicleType()
        self.common_helper_obj = CommonHelper()
        self.parking_slot_views_obj = ParkingSlotViews()
        self.vehicle_type_views_obj = VehicleTypeViews()
        self.new_data = None
        self.updated_field = None
        self.username = username

    def employee_menu_operations(self) -> None:
        print("\n" + Prompts.EMPLOYEE_MENU_WELCOME_MESSAGE + "\n")
        while True:
            print("\n" + Prompts.EMPLOYEE_MENU)
            if self.employee_menu():
                break

    def customer_registration_form(self) -> None:
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
        vehicle_type_name = [(vehicle[1],) for vehicle in data]
        self.vehicle_type_views_obj.view_vehicle_type()
        choice = int(input(Prompts.ENTER_CHOICE))
        
        if choice > len(vehicle_type_name) or choice < 1:
            print(Prompts.INVALID_INPUT)
        else:
            type_name = vehicle_type_name[choice-1][0]
            type_id = self.vehicle_type_obj.get_vehicle_type_id_from_type_name(type_name)
            type_id = type_id[0][0]
            cust_data = (cust_id, cust_name, cust_mobile_number, cust_vehicle_number, type_id)
            self.employee_controller_obj.register_customer(cust_data)
            print(Prompts.CUSTOMER_CREATION_SUCCESSFUL + "\n")

    def view_customer_details(self) -> None:
        data = self.employee_controller_obj.get_customer_details()
        if not data:
            print(Prompts.ZERO_RECORD.format("Customer"))
        else:
            header = TableHeader.CUSTOMER_DETAIL_HEADER
            self.common_helper_obj.display_table(data, header)
    
    def customer_details_updation_form(self) -> None:
        if not self.employee_controller_obj.get_customer_details():
            print(Prompts.CANNOT_UPDATE_RECORD + "\n")
            return
        
        self.view_customer_details()
        print("\n" + Prompts.INPUT_DETAILS_FOR_UPDATION + "\n")
        cust_vehicle_no = ParkingControllerValidator.input_vehicle_number()
        data = self.employee_controller_obj.get_cust_id_from_vehicle_no(cust_vehicle_no)

        if not data:
            print(Prompts.CUSTOMER_DOES_NOT_EXIST + "\n")
        else:
            cust_id = data[0][0]
            while True:
                if self.update_menu():
                    break
                if self.updated_field in (AppConfig.NAME_ATTR, AppConfig.MOBILE_NO_ATTR):
                    self.employee_controller_obj.update_customer_details(self.updated_field, self.new_data, cust_id)
                    print(Prompts.CUSTOMER_UPDATION_SUCCESSFUL + "\n")
                else:
                    self.update_out_date(cust_id)

    def update_out_date(self, cust_id) -> None:
        """
            Method to update out date.
            Parameter -> self
            Return type -> None
        """
        data =  self.employee_controller_obj.get_booking_details_from_cust_id(cust_id)
        if not data:
            print(Prompts.BOOKING_RECORD_NOT_FOUND + "\n")
        else:
            curr_booking_data = data[len(data)-1]
            booking_id = curr_booking_data[0]
            curr_out_time = curr_booking_data[6]
            if curr_out_time != AppConfig.DEFAULT_OUT_TIME:
                print(Prompts.NO_UPDATION_FOR_CHECKOUT_VEHICLE + "\n")
            else:
                print(Prompts.NEW_DETAIL_INPUT.format("Out Date"))
                self.new_data = ParkingControllerValidator.input_out_date()
                self.updated_field = AppConfig.OUT_DATE_ATTR
                self.employee_controller_obj.update_out_date(self.updated_field, self.new_data, booking_id)
                print(Prompts.SLOT_BOOKING_UPDATION_SUCCESSFUL + "\n")

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
    def employee_menu(self) -> bool:
        """Method to handle employee menu."""
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
                self.book_parking_slot()
            case '6':
                self.vacate_parking_slot()
            case '7':
                self.view_booking_details()
            case '8':
                self.vehicle_type_views_obj.view_vehicle_type()
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
    def update_menu(self) -> bool:
        """
            Method for managing customer update menu.
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
                pass
            case '4':
                return True
            case _:
                print(Prompts.INVALID_INPUT)
        return False
