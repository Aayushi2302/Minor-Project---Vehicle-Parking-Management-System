from config.app_config import AppConfig
from config.prompts.prompts import Prompts
from models.db_helper import DBHelper
from utils.error_handler import error_handler
from utils.input_validator.parking_controller_validator import ParkingControllerInputValidator
from utils.input_validator.user_controller_validator import UserInputValidatior

class CustomerUpdateViews:
    """
        Class containing methods to update customer details.
        ...
        Attributes
        ----------
        db_helper_obj -> DBHelper
        customer_id -> str
        booking_id -> str
        new_data -> str
        updated_field -> str

        Methods
        -------
        customer_update_operations() -> Method to update customer details.
        update_out_date() -> Method to update out date
        update_menu() -> Method to manage customer update menu.
    """
    def __init__(self) -> None:
        self.db_helper_obj = DBHelper()
        self.customer_id = None
        self.booking_id = None
        self.new_data = None
        self.updated_field = None

    def customer_update_operations(self) -> bool:
        """
            Method to update customer details.
            Parameter -> self
            Return type -> bool
        """
        print("\n" + Prompts.INPUT_DETAILS_FOR_UPDATION + "\n")
        cust_vehicle_no = ParkingControllerInputValidator.input_vehicle_number()
        data = self.db_helper_obj.get_customer_id_and_type_id(cust_vehicle_no)
        if not data:
            print(Prompts.CUSTOMER_DOES_NOT_EXIST + "\n")
        else:
            self.customer_id = data[0][0]
            while True:
                if self.update_menu():
                    break
                if self.updated_field in (AppConfig.NAME_ATTR, AppConfig.MOBILE_NO_ATTR):
                    self.db_helper_obj.update_customer_data(
                        self.updated_field,
                        self.new_data,
                        self.customer_id
                    )
                    print(Prompts.CUSTOMER_UPDATION_SUCCESSFUL + "\n")

    def update_out_date(self) -> None:
        """
            Method to update out date.
            Parameter -> self
            Return type -> None
        """
        data =  self.db_helper_obj.get_booking_details(self.customer_id)
        if not data:
            print(Prompts.BOOKING_RECORD_NOT_FOUND + "\n")
        else:
            curr_booking_data = data[len(data)-1]
            self.booking_id = curr_booking_data[0]
            curr_out_time = curr_booking_data[6]
            if curr_out_time != AppConfig.DEFAULT_OUT_TIME:
                print(Prompts.NO_UPDATION_FOR_CHECKOUT_VEHICLE + "\n")
            else:
                print(Prompts.NEW_DETAIL_INPUT.format("Out Date"))
                self.new_data = ParkingControllerInputValidator.input_out_date()
                self.updated_field = AppConfig.OUT_DATE_ATTR
                self.db_helper_obj.update_out_date(
                    self.updated_field,
                    self.new_data,
                    self.booking_id
                )
                print(Prompts.SLOT_BOOKING_UPDATION_SUCCESSFUL + "\n")

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
                self.new_data = UserInputValidatior.input_name()
                self.updated_field = AppConfig.NAME_ATTR
            case '2':
                print(Prompts.NEW_DETAIL_INPUT.format("Mobile No."))
                self.new_data = UserInputValidatior.input_mobile_number()
                self.updated_field = AppConfig.MOBILE_NO_ATTR
            case '3':
                self.update_out_date()
            case '4':
                return True
            case _:
                print(Prompts.INVALID_INPUT)
        return False
