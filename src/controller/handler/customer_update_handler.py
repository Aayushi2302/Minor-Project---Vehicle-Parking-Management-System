"""
    Module for maintaing menu for updating customer details.
"""
import logging

from config.statements.config import Config
from config.menu.menu_prompts_config import MenuConfig
from config.query.query_config import QueryConfig
from database.query_executor import QueryExecutor
from utils.validator.parking_manager_input_validation import ParkingManagerInputValidation
from utils.validator.user_input_validation import UserInputValidation

logger = logging.getLogger('employee_update_handler')

@staticmethod
def customer_details_update_menu() -> None:
    """
        Module to update customer details.
    """
    print("\n" + Config.input_details_for_updation_prompt + "\n")
    cust_vehicle_no = ParkingManagerInputValidation.input_vehicle_number()
    data =  QueryExecutor.fetch_data_from_database(
                QueryConfig.query_for_fetching_customer_id_and_type_id_from_vehicle_no,
                (cust_vehicle_no, )
            )
    if not any(data):
        print(Config.customer_does_not_exist_prompt + "\n")
        return
    customer_id = data[0][0]
    while True:
        print(MenuConfig.customer_detail_update_menu_prompt)
        try:
            choice = int(input(Config.enter_choice_prompt))
            match choice:
                case 1:
                    print(Config.new_detail_input_prompt.format("Name"))
                    new_data = UserInputValidation.input_name()
                    updated_field = "name"
                case 2:
                    print(Config.new_detail_input_prompt.format("Mobile No."))
                    new_data = UserInputValidation.input_mobile_number()
                    updated_field = "mobile_no"
                case 3:
                    data =  QueryExecutor.fetch_data_from_database(
                                QueryConfig.query_for_fetching_booking_detail_from_customer_id,
                                (customer_id, )
                            )
                    if not any(data):
                        print(Config.booking_records_not_found_prompt + "\n")
                        continue
                    curr_booking_data = data[len(data)-1]
                    booking_id = curr_booking_data[0]
                    curr_out_time = curr_booking_data[6]
                    if curr_out_time != "XX:XX":
                        print(Config.no_updation_for_check_out_vehicle_prompt + "\n")
                    else:
                        print(Config.new_detail_input_prompt.format("Out Date"))
                        new_data = UserInputValidation.input_out_date()
                        query_for_updating_out_date = QueryConfig.query_for_updating_slot_booking_detail.format("out_date")
                        QueryExecutor.save_data_in_database(
                            query_for_updating_out_date,
                            (new_data, booking_id)
                        )
                        print(Config.slot_booking_updation_successful_prompt + "\n")
                    continue
                case 4:
                    break
                case _:
                    print(Config.invalid_input_prompt)
            query_for_updating_customer_data = QueryConfig.query_for_updating_customer_detail.format(updated_field)
            QueryExecutor.save_data_in_database(
                query_for_updating_customer_data,
                (new_data, customer_id),
                Config.customer_updation_successful_prompt + "\n"
            )
        except ValueError:
            logger.debug(ValueError)
            print(Config.invalid_input_prompt + "\n")