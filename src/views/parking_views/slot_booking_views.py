import shortuuid

from config.app_config import AppConfig
from config.prompts.prompts import Prompts
from config.query import TableHeader
from controller.employee_controller import EmployeeController
from controller.parking_controller.slot_booking import SlotBooking
from utils.common_helper import CommonHelper
from utils.input_validator.parking_controller_validator import ParkingControllerValidator

class SlotBookingViews:
    def __init__(self) -> None:
        self.slot_booking_obj = SlotBooking()
        self.common_helper_obj = CommonHelper()

    def book_parking_slot(self) -> None:
        print(Prompts.INPUT_DETAILS_FOR_SLOT_BOOKING)
        booking_id = "BOOK" + shortuuid.ShortUUID().random(length = 5)
        cust_vehicle_no = ParkingControllerValidator.input_vehicle_number()
        cust_out_date = ParkingControllerValidator.input_out_date()
        curr_date_and_time = self.common_helper_obj.get_current_date_and_time()
        cust_in_date = curr_date_and_time[0]
        cust_in_time = curr_date_and_time[1]
        parking_slot_no = self.slot_booking_obj.save_booking_details(booking_id, cust_vehicle_no,
                                                        cust_in_date, cust_in_time, cust_out_date)
        if not parking_slot_no:
            print(Prompts.VEHCILE_NO_NOT_FOUND + "\n")
        else:
            print(Prompts.PARKING_SLOT_ASSIGNED.format(parking_slot_no) + "\n")

    def view_booking_details(self) -> None:
        data = self.slot_booking_obj.get_booking_details()
        if not data:
            print(Prompts.ZERO_RECORD.format("Slot Booking"))
        else:
            header = TableHeader.SLOT_BOOKING_DETAIL_HEADER
            self.common_helper_obj.display_table(data, header)

    def vacate_parking_slot(self) -> None:
        if not self.slot_booking_obj.get_booking_details():
            print(Prompts.CANNOT_VACATE_PARKING_SLOT + "\n")
            return

        self.view_booking_details()
        print("\n" + Prompts.INPUT_DETAIL_TO_VACATE_PARKING_SLOT + "\n")
        vehicle_no = ParkingControllerValidator.input_vehicle_number()
        out_date_time = self.common_helper_obj.get_current_date_and_time()
        out_date = out_date_time[0]
        out_time = out_date_time[1]
        result = self.slot_booking_obj.save_vacating_details(vehicle_no, out_date, out_time)
        if result[0] == -1:
            print(Prompts.CUSTOMER_DOES_NOT_EXIST + "\n")
        elif result[0] == 0:
            print(Prompts.VEHICLE_ALREADY_VACATE_PARKING_SLOT + "\n")
        else:
            print(Prompts.PARKING_SLOT_VACANT + "\n" \
                + Prompts.PRINT_PARKING_CHARGES.format(result[0], result[1]) + "\n")
