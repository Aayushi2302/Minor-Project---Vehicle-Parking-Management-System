"""Module contaning views logic for parking controller parking status module."""

from config.prompts.prompts import Prompts
from config.query import TableHeader
from controller.parking_controller.parking_status import ParkingStatus
from utils.common_helper import CommonHelper
from utils.decorators import error_handler, looper
from views.parking_views.slot_booking_views import SlotBookingViews

class ParkingStatusViews:
    """
        Class contaning views logic for parking status module.
        ...
        Attributes:
        ----------
        parking_status_obj : ParkingStatus
        common_helper_obj : CommonHelper
        slot_booking_obj : SlotBooking

        Methods:
        -------
        view_current_date_status() -> method to view booking details according to current date.
        view_cuurent_year_status() -> method to view booking details according to current year.
        parking_status_menu() -> menu to handle view parking status operations.
    """
    def __init__(self) -> None:
        """
            Method for constructing parking status views object.
            Parameter -> self
            Return type -> None
        """
        self.parking_status_obj = ParkingStatus()
        self.common_helper_obj = CommonHelper()
        self.slot_booking_views_obj = SlotBookingViews()

    def view_current_date_status(self) -> None:
        """ 
            Method to view booking details according to current date.
            Parameter -> self
            Return type -> None
        """
        data = self.parking_status_obj.get_current_date_status()
        if not data:
            print(Prompts.ZERO_RECORD.format("Booking") + "\n")
        else:
            header = TableHeader.SLOT_BOOKING_DETAIL_HEADER
            self.common_helper_obj.display_table(data, header)

    def view_current_year_status(self) -> None:
        """
            Method to view booking details according to current year.
            Parameter -> self
            Return type -> None
        """
        data = self.parking_status_obj.get_current_year_status()
        if not data:
            print(Prompts.ZERO_RECORD.format("Booking") + "\n")
        else:
            header = TableHeader.SLOT_BOOKING_DETAIL_HEADER
            self.common_helper_obj.display_table(data, header)

    @looper
    @error_handler
    def parking_status_menu(self) -> bool:
        """
            Method for managing parking status menu operations
            Parameter -> self
            Return type -> bool
        """
        print("\n" + Prompts.VIEW_PARKING_STATUS_MENU + "\n")
        see_status_choice = input(Prompts.ENTER_CHOICE)
        match see_status_choice:
            case '1':
                self.view_current_date_status()
            case '2':
                self.view_current_year_status()
            case '3':
                self.slot_booking_views_obj.view_booking_details()
            case '4':
                return True
            case _ :
                print(Prompts.INVALID_INPUT)
        return False
    