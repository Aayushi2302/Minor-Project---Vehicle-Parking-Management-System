"""Module responsible for invoking business logic to get individual parking slot."""

from src.config.prompts.prompts import Prompts
from src.business.parking_slot_business import ParkingSlotBusiness
from src.models.database import db
from src.utils.custom_error_handler import custom_error_handler
from src.utils.responses import SuccessResponse


class GetIndividualParkingSlotContainer:
    """
        Class responsible for invoking business logic to get individual parking slot.
        ...
        Methods
        -------
        get_individual_parking_slot() : tuple -> method to get individual parking slot if exists.
    """
    @custom_error_handler
    def get_individual_parking_slot(self, parking_slot_no: str) -> tuple:
        """
            Method to get individual parking slot if exists.
            Parameters -> parking_slot_no: str
            Returns -> tuple
        """
        parking_slot_business_obj = ParkingSlotBusiness(db)
        response = parking_slot_business_obj.get_individual_parking_slot(parking_slot_no)
        return SuccessResponse.jsonify_data("Parking slot fetched successfully", response), 200
