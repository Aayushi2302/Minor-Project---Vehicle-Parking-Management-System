"""
    Module for maintaing functionalities related to parking slot booking.
"""
import random
import shortuuid

from config.statements.config import Config
from config.query.query_config import QueryConfig
from database.query_executor import QueryExecutor
from parking_manager.parking_charges import ParkingCharges
from utils.common import Common
from utils.validator.parking_manager_input_validation import ParkingManagerInputValidation

class SlotBooking(ParkingCharges):
    """
        Class for maintaing functionalities related to parking slot booking.
    """
    def book_parking_slot(self) -> None:
        """
            Method for booking parking slot.
        """
        print(Config.input_details_for_slot_booking_prompt)
        booking_id = "BOOK" + shortuuid.ShortUUID().random(length = 5)
        cust_vehicle_no = ParkingManagerInputValidation.input_vehicle_number()
        data =  QueryExecutor.fetch_data_from_database(
                    QueryConfig.query_for_fetching_customer_id_and_type_id_from_vehicle_no,
                    (cust_vehicle_no, )
                )
        if not any(data):
            print(Config.vehicleno_not_found_prompt + "\n")
        else:
            cust_out_date = ParkingManagerInputValidation.input_out_date()
            customer_id = data[0][0]
            type_id = data[0][1]

            common_obj = Common()
            curr_date_and_time = common_obj.get_current_date_and_time()
            cust_in_date = curr_date_and_time[0]
            cust_in_time = curr_date_and_time[1]
            parking_slot_no = QueryExecutor.fetch_data_from_database(
                                QueryConfig.query_for_fetching_parking_slot_no_for_booking,
                                (type_id, "vacant")
                              )
            random_index = random.randrange(len(parking_slot_no))
            booking_parking_slot_no = parking_slot_no[random_index][0]
            QueryExecutor.save_data_in_database(
                QueryConfig.query_for_creating_slot_booking,
                (booking_id, customer_id, booking_parking_slot_no, cust_in_date, cust_in_time, cust_out_date),
                ""
            )
            query_for_updating_parking_slot_status = QueryConfig.query_for_updating_parking_slot_detail_from_parking_slot_no.format("status")
            QueryExecutor.save_data_in_database(
                query_for_updating_parking_slot_status,
                ("booked", booking_parking_slot_no),
                Config.parking_slot_assigned_prompt.format(booking_parking_slot_no) + "\n"
            )
        
    def view_booking_details(self) -> None:
        """
            Method to view booking details.
        """
        data =  QueryExecutor.fetch_data_from_database(
                    QueryConfig.query_for_viewing_slot_booking_detail
                )
        if not any(data):
            print(Config.zero_record_prompt.format("slot_booking"))
        else:
            common_obj = Common()
            headers = QueryConfig.slot_booking_detail_header
            common_obj.display_table(data, headers)
    
    def vacate_parking_slot(self) -> None:
        """
            Method to vacate parking slot.
        """
        self.view_booking_details()
        print("\n" + Config.input_details_for_updation_prompt + "\n")
        vehicle_number = ParkingManagerInputValidation.input_vehicle_number()
        data =  QueryExecutor.fetch_data_from_database(
                    QueryConfig.query_for_fetching_detail_for_vacating_parking_slot,
                    (vehicle_number, )
                )
        if not any(data):
            print(Config.customer_does_not_exist_prompt + "\n")
            return
        else:
            booking_id = data[0][0]
            parking_slot_no = data[0][1]
            in_date = data[0][2]
            in_time = data[0][3]

            common_obj = Common()
            out_date_time = common_obj.get_current_date_and_time()
            out_date = out_date_time[0]
            out_time = out_date_time[1]

            slot_booking_obj = SlotBooking()
            hours_spent = slot_booking_obj.calculate_hours_spent_in_parking(in_date, in_time, out_date, out_time)
            charges = slot_booking_obj.calculate_charges(hours_spent, booking_id)

            if charges == 0.0:
                return
            query_for_parking_slot_updation = QueryConfig.query_for_updating_parking_slot_detail_from_parking_slot_no.format("status")
            success_message = Config.parking_slot_vacant_prompt + "\n" + Config.print_parking_charges.format(charges, hours_spent) + "\n"
            QueryExecutor.save_data_in_database(
                query_for_parking_slot_updation,
                ("vacant", parking_slot_no),
                ""
            )
            QueryExecutor.save_data_in_database(
                QueryConfig.query_for_updating_detail_for_vacating_parking_slot,
                (out_date, out_time, hours_spent, charges, booking_id),
                success_message
            )