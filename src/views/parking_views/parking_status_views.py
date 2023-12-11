from config.prompts.prompts import Prompts
from config.query import TableHeader
from controller.parking_controller.parking_status import ParkingStatus
from utils.common_helper import CommonHelper
from utils.error_handler import error_handler
from views.parking_views.slot_booking_views import SlotBookingViews

class ParkingStatusViews:
    def __init__(self) -> None:
        self.parking_status_obj = ParkingStatus()
        self.common_helper_obj = CommonHelper()
        self.slot_booking_views_obj = SlotBookingViews()

    def view_current_date_status(self) -> None:
        data = self.parking_status_obj.get_current_date_status()
        if not data:
            print(Prompts.ZERO_RECORD.format("Booking") + "\n")
        else:
            header = TableHeader.SLOT_BOOKING_DETAIL_HEADER
            self.common_helper_obj.display_table(data, header)
    
    def view_current_year_status(self) -> None:
        data = self.parking_status_obj.get_current_year_status()
        if not data:
            print(Prompts.ZERO_RECORD.format("Booking") + "\n")
        else:
            header = TableHeader.SLOT_BOOKING_DETAIL_HEADER
            self.common_helper_obj.display_table(data, header)

    @error_handler
    def parking_status_menu(self) -> bool:
        """
            Method for managing parking status menu.
            Parameter -> self
            Return type -> bool
        """
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
    