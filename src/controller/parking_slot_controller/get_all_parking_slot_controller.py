"""Module responsible for invoking business logic to get all existing parking slots."""

from src.config.prompts.prompts import Prompts
from src.business.parking_slot_business import ParkingSlotBusiness
from src.models.database import db
from src.utils.custom_error_handler import custom_error_handler
from src.utils.responses import SuccessResponse


class GetAllParkingSlotController:
    """
        Class responsible for invoking business logic to get all existing parking slots.
        ...
        Methods
        -------
        get_all_parking_slots() : tuple -> method to get all existing parking slots.
    """
    @custom_error_handler
    def get_all_parking_slots(self) -> tuple:
        """
            Method to get all existing parking slots.
            Parameters -> None
            Returns -> tuple
        """
        parking_slot_business_obj = ParkingSlotBusiness(db)
        response = parking_slot_business_obj.get_all_parking_slots()
        return SuccessResponse.jsonify_data(Prompts.PARKING_SLOT_GET_SUCCESS, response), 200
