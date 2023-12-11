import shortuuid

from config.app_config import AppConfig
from config.prompts.prompts import Prompts
from config.query import TableHeader
from controller.parking_controller.vehicle_type import VehicleType
from utils.common_helper import CommonHelper
from utils.error_handler import error_handler
from utils.input_validator.parking_controller_validator import ParkingControllerValidator

class VehicleTypeViews:

    def __init__(self):
        self.vehicle_type_obj = VehicleType()
        self.common_helper_obj = CommonHelper()

    def vehicle_type_registration_form(self) -> None:
        type_name = ParkingControllerValidator.input_vehicle_type_name()
        price_per_hour = ParkingControllerValidator.input_price_per_hour()
        type_id = "TYPE" + shortuuid.ShortUUID().random(length = 5)
        self.vehicle_type_obj.register_vehicle_type(type_id, type_name, price_per_hour)
        print(Prompts.VEHICLE_TYPE_REGISTRATION_SUCCESSFUL + "\n")
    
    def view_vehicle_type(self) -> None:
        data = self.vehicle_type_obj.get_all_vehicle_type()
        if not data:
            print(Prompts.ZERO_RECORD.format("Vehicle Type"))
        else:
            header = TableHeader.VEHICLE_TYPE_DETAIL_HEADER
            self.common_helper_obj.display_table(data, header)
    
    def vehicle_type_update_form(self) -> None:
        if not self.vehicle_type_obj.get_all_vehicle_type():
            print(Prompts.CANNOT_UPDATE_RECORD + "\n")
            return

        self.view_vehicle_type()
        print("\n" + Prompts.INPUT_DETAILS_FOR_UPDATION + "\n")
        type_id = ParkingControllerValidator.input_vehicle_type_id()
        data = self.vehicle_type_obj.get_vehicle_type_data_from_type_id(type_id)

        if not data:
            print(Prompts.TYPEID_DOES_NOT_EXIST + "\n")
        else:
            curr_price_per_hour = data[0][0]
            print(Prompts.CURRENT_PRICE_PER_HOUR.format(curr_price_per_hour) + "\n")
            print(Prompts.NEW_DETAIL_INPUT.format("Price Per Hour"))
            new_data = ParkingControllerValidator.input_price_per_hour()
            updated_field = AppConfig.PRICE_PER_HOUR_ATTR
            self.vehicle_type_obj.update_vehicle_type_detail(new_data, updated_field, type_id)
            print(Prompts.VEHICLE_TYPE_DETAILS_UPDATION_SUCCESSFUL + "\n")

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
                self.vehicle_type_registration_form()
            case '2':
                self.vehicle_type_update_form()
            case '3':
                self.view_vehicle_type()
            case '4' :
                return True
            case _ :
                print(Prompts.INVALID_INPUT)
        return False
