"""Module contaning views logic for parking controller parking slot module."""

from config.app_config import AppConfig
from config.prompts.prompts import Prompts
from config.query import TableHeader
from controller.parking_controller.parking_slot import ParkingSlot
from controller.parking_controller.vehicle_type import VehicleType
from utils.common_helper import CommonHelper
from utils.decorators import error_handler, looper
from utils.input_validator.parking_controller_validator import ParkingControllerValidator

class ParkingSlotViews:
    """ 
        Class containing views logic for parking slot module.
        ...
        Attributes:
        ----------
        parking_slot_obj : ParkingSlot
        common_helper_obj : CommonHelper

        Methods:
        -------
        parking_slot_registration_form() -> method to take inputs for registering parking slot.
        view_parking_slots() -> method to view parking slot details.
        parking_slot_status_updation_form() -> method to update parking slot status.
        parking_slot_menu() -> menu to handle parking slot operations.
    """
    def __init__(self) -> None:
        """
            Method for constructing parking slot views object.
            Parameter -> self
            Return type -> None
        """
        self.parking_slot_obj = ParkingSlot()
        self.common_helper_obj = CommonHelper()

    def parking_slot_registration_form(self) -> None:
        """
            Method to take inputs for registering parking slots.
            Parameter -> self
            Return type -> None
        """
        parking_slot_number = ParkingControllerValidator.input_parking_slot_number()
        vehicle_type_name = ParkingControllerValidator.input_vehicle_type_name()
        result = self.parking_slot_obj.register_parking_slot(parking_slot_number, vehicle_type_name)

        if not result:
            print(Prompts.VEHICLE_TYPE_DOES_NOT_EXIST + "\n")
        else:
            print(Prompts.PARKING_SLOT_REGISTRATION_SUCCESSFUL + "\n")

    def view_parking_slots(self) -> None:
        """
            Method to view parking slot details.
            Parameter -> self
            Return type -> None
        """
        data = self.parking_slot_obj.get_all_parking_slots()
        if not data:
            print("\n" + Prompts.ZERO_RECORD.format("Parking Slot"))
        else:
            header = TableHeader.PARKING_SLOT_DETAIL_HEADER
            self.common_helper_obj.display_table(data, header)

    def parking_slot_status_updation_form(self, new_status: str) -> None:
        """
            Method to update parking slot status.
            Parameter -> self, new_status: str
            Return type -> None
        """
        if not self.parking_slot_obj.get_all_parking_slots():
            print("\n" + Prompts.CANNOT_UPDATE_RECORD + "\n")
            return

        self.view_parking_slots()
        print("\n" + Prompts.INPUT_DETAILS_FOR_UPDATION + "\n")
        parking_slot_number = ParkingControllerValidator.input_parking_slot_number()
        result = self.parking_slot_obj.update_parking_slot_status(
                    parking_slot_number,
                    AppConfig.STATUS_ATTR, new_status
                )

        if result == -1:
            print("\n" + Prompts.PARKING_SLOT_NUMBER_DOES_NOT_EXIST + "\n")
        elif result == 0:
            print("\n" + Prompts.PARKING_SLOT_ALREADY_VACANT + "\n")
        else:
            if new_status == AppConfig.PARKING_SLOT_STATUS_VACANT:
                print("\n" + Prompts.PARKING_SLOT_ACTIVATION_SUCCESSFUL + "\n")
            elif new_status == AppConfig.PARKING_SLOT_STATUS_INACTIVE:
                print("\n" + Prompts.PARKING_SLOT_DEACTIVATION_SUCCESSFUL + "\n")
            else:
                print("\n" + Prompts.PARKING_SLOT_REMOVAL_SUCCESSFUL + "\n")

    @looper
    @error_handler
    def parking_slot_menu(self) -> bool:
        """
            Method for managing parking slot menu operations.
            Parameter -> self
            Return type -> bool
        """
        print("\n" + Prompts.MANAGE_PARKING_SLOT_MENU)
        parking_slot_choice = input(Prompts.ENTER_CHOICE)
        match parking_slot_choice:
            case '1':
                self.parking_slot_registration_form()
            case '2':
                self.parking_slot_status_updation_form(AppConfig.PARKING_SLOT_STATUS_VACANT)
            case '3':
                self.parking_slot_status_updation_form(AppConfig.PARKING_SLOT_STATUS_INACTIVE)
            case '4':
                self.view_parking_slots()
            case '5' :
                self.parking_slot_status_updation_form(AppConfig.PARKING_SLOT_STATUS_DELETED)
            case '6':
                return True
            case _ :
                print(Prompts.INVALID_INPUT)
        return False
