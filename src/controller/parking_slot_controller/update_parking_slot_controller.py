"""Module responsible for invoking business logic to update parking slot status."""

from config.prompts.prompts import Prompts
from business.parking_slot_business import ParkingSlotBusiness
from models.database import db
from utils.custom_error_handler import custom_error_handler
from utils.responses import SuccessResponse


class UpdateParkingSlotController:
    """
        Class responsible for invoking business logic to update parking slot status.
        ...
        Methods
        -------
        update_parking_slot() : tuple -> method to update the status of parking slot if exists.
    """
    @custom_error_handler
    def update_parking_slot(self, parking_slot_no: str, parking_slot_data: dict) -> tuple:
        """
            Method to update existing parking slot status.
            Parameters -> parking_slot_no: str, parking_slot_data: dict
            Returns -> tuple
        """
        new_status = parking_slot_data["new_status"]

        parking_slot_business_obj = ParkingSlotBusiness(db)
        parking_slot_business_obj.update_parking_slot_status(parking_slot_no, new_status)
        return SuccessResponse.jsonify_data("Parking slot updated successfully."), 200
