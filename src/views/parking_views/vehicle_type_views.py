"""Module containing views for parking controller vehicle type module."""

import shortuuid

from config.app_config import AppConfig
from config.prompts.prompts import Prompts
from config.query import TableHeader
from controller.parking_controller.vehicle_type import VehicleType
from utils.common_helper import CommonHelper
from utils.decorators import error_handler, looper
from utils.input_validator.parking_controller_validator import ParkingControllerValidator

class VehicleTypeViews:
    """
        Class contaning views logic for vehicle type module in parking controller.
        ...
        Attributes:
        ----------
        vehicle_type_obj : VehicleType
        common_helper_obj : CommonHelper

        Methods:
        -------
        vehicle_type_registration_form() -> method for taking input for registering vehicle type.
        view_vehicle_type() -> method for view vehicle type details.
        vehicle_type_update_form() -> method for taking input to update vehicle type details.
        vehicle_type_menu() -> menu to handle vehicle type operations.
    """
    def __init__(self) -> None:
        """
            Method for constructing vehicle type views object.
            Parameter -> self
            Return type -> None
        """
        self.vehicle_type_obj = VehicleType()
        self.common_helper_obj = CommonHelper()

    def vehicle_type_registration_form(self) -> None:
        """
            Method for taking input for registering vehicle type.
            Parameter -> self
            Return type -> None
        """
        type_name = ParkingControllerValidator.input_vehicle_type_name()
        price_per_hour = ParkingControllerValidator.input_price_per_hour()
        type_id = "TYPE" + shortuuid.ShortUUID().random(length = 5)
        self.vehicle_type_obj.register_vehicle_type(type_id, type_name, price_per_hour)
        print(Prompts.VEHICLE_TYPE_REGISTRATION_SUCCESSFUL + "\n")

    def view_vehicle_type(self) -> None:
        """
            Method to view vehicle type details.
            Parameter -> self
            Return type -> None
        """
        data = self.vehicle_type_obj.get_all_vehicle_type()
        if not data:
            print(Prompts.ZERO_RECORD.format("Vehicle Type"))
        else:
            header = TableHeader.VEHICLE_TYPE_DETAIL_HEADER
            self.common_helper_obj.display_table(data, header)

    def vehicle_type_update_form(self) -> None:
        """
            Method to take input to update vehicle type details.
            Parameter -> self
            Return type -> None

        """
        if not self.vehicle_type_obj.get_all_vehicle_type():
            print(Prompts.CANNOT_UPDATE_RECORD + "\n")
            return

        self.view_vehicle_type()
        print("\n" + Prompts.INPUT_DETAILS_FOR_UPDATION + "\n")
        type_id = ParkingControllerValidator.input_vehicle_type_id()
        print(Prompts.NEW_DETAIL_INPUT.format("Price Per Hour"))
        new_data = ParkingControllerValidator.input_price_per_hour()
        updated_field = AppConfig.PRICE_PER_HOUR_ATTR
        result = self.vehicle_type_obj.update_vehicle_type_detail(type_id, updated_field, new_data)

        if not result:
            print(Prompts.TYPEID_DOES_NOT_EXIST + "\n")
        else:
            print(Prompts.VEHICLE_TYPE_DETAILS_UPDATION_SUCCESSFUL + "\n")

    @looper
    @error_handler
    def vehicle_type_menu(self) -> bool:
        """ 
            Method for managing vehicle type menu operations.
            Parameter -> self
            Return type -> bool
        """
        print("\n" + Prompts.MANAGE_VEHICLE_TYPE_MENU)
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
