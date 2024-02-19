"""Module responsible for invoking business logic to delete existing parking slot."""

from src.config.app_config import  AppConfig
from src.config.prompts.prompts import Prompts
from src.business.parking_slot_business import ParkingSlotBusiness
from src.models.database import db
from src.utils.custom_error_handler import custom_error_handler
from src.utils.responses import SuccessResponse


class DeleteParkingSlotController:
    """
        Class responsible for invoking business logic to delete existing parking slot.
        ...
        Methods
        -------
        delete_parking_slots() : tuple -> method to delete existing parking slot.
    """
    @custom_error_handler
    def delete_parking_slot(self, parking_slot_no: str) -> tuple:
        """
            Method to delete existing parking slot.
            Parameters -> None
            Returns -> tuple
        """
        new_status = AppConfig.PARKING_SLOT_STATUS_DELETED

        parking_slot_business_obj = ParkingSlotBusiness(db)
        parking_slot_business_obj.update_parking_slot_status(parking_slot_no, new_status)
        return SuccessResponse.jsonify_data("Parking slot deleted successfully."), 200
