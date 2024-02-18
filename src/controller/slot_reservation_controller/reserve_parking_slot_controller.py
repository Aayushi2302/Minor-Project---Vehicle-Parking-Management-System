"""Module responsible for invoking business logic for reserving a parking slot."""

from config.prompts.prompts import Prompts
from business.slot_reservation_business import SlotReservationBusiness
from helpers.customer_helper import CustomerHelper
from helpers.slot_reservation_helper import SlotReservationHelper
from models.database import db
from utils.custom_error_handler import custom_error_handler
from utils.responses import SuccessResponse


class ReserveParkingSlotController:
    """
        Class containing methods responsible for calling business logic for reserving parking slot.
        ...
        Methods
        -------
       reserve_parking_slot() : tuple -> method to reserve a parking slot.
    """

    @custom_error_handler
    def reserve_parking_slot(self, customer_data: dict) -> tuple:
        """
            Method to reserve a parking slot.
            Parameters -> customer_data: dict
            Returns -> tuple
        """
        vehicle_no = customer_data["vehicle_no"]
        out_date = customer_data["out_date"]

        customer_helper = CustomerHelper(db)
        slot_reservation_helper = SlotReservationHelper(db)
        slot_reservation_business = SlotReservationBusiness(db, slot_reservation_helper, customer_helper)

        response = slot_reservation_business.save_reservation_details(vehicle_no, out_date)
        return SuccessResponse.jsonify_data("Parking slot reserved successfully", response), 200
