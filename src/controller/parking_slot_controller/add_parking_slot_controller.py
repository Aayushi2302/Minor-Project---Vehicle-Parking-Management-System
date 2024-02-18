"""Module responsible for invoking business logic for adding parking slot.."""

from config.prompts.prompts import Prompts
from business.parking_slot_business import ParkingSlotBusiness
from models.database import db
from utils.custom_error_handler import custom_error_handler
from utils.responses import SuccessResponse


class AddParkingSlotController:
    """
        Class containing methods responsible for calling business logic for adding parking slot.
        ...
        Methods
        -------
        add_parking_slot() : tuple -> method to add a new parking slot.
    """

    @custom_error_handler
    def add_parking_slot(self, parking_slot_data: dict) -> tuple:
        """
            Method to add a new parking slot.
            Parameters -> parking_slot_data: dict
            Returns -> dict
        """
        parking_slot_no = parking_slot_data["parking_slot_no"]
        type_name = parking_slot_data["vehicle_type_name"]

        parking_slot_business_obj = ParkingSlotBusiness(db)
        parking_slot_business_obj.register_parking_slot(parking_slot_no, type_name)
        return SuccessResponse.jsonify_data("Parking slot created successfully."), 200
