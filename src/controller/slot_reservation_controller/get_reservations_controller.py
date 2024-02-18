"""Module responsible for invoking business logic for getting reservation details."""

from typing import Optional

from config.prompts.prompts import Prompts
from business.reservation_record import ReservationRecord
from business.slot_reservation_business import SlotReservationBusiness
from helpers.customer_helper import CustomerHelper
from helpers.slot_reservation_helper import SlotReservationHelper
from models.database import db
from utils.custom_error_handler import custom_error_handler
from utils.responses import SuccessResponse


class GetReservationsController:
    """
        Class containing methods responsible for calling business logic for getting reservation details.
        ...
        Methods
        -------
       get_reservation_details() : tuple -> method to get reservation details.
    """

    @custom_error_handler
    def get_reservation_details(self, date_or_year: Optional[str] = None) -> tuple:
        """
            Method to get reservation details based on date_or_year field.
            Parameters -> date_or_year : str | None
            Returns -> tuple
        """
        if date_or_year is None:
            customer_helper = CustomerHelper(db)
            slot_reservation_helper = SlotReservationHelper(db)
            slot_reservation_business = SlotReservationBusiness(db, slot_reservation_helper, customer_helper)

            response = slot_reservation_business.get_reservation_details()

        else:
            reservation_record = ReservationRecord(db)
            if "-" in date_or_year:
                response = reservation_record.get_date_record(date_or_year)

            else:
                response = reservation_record.get_date_record(date_or_year)

        return SuccessResponse.jsonify_data("Reservations fetched successfully", response), 200
