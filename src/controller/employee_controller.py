"""
    Module for maintaining all the methods or functionalities of Employee.
"""
import shortuuid

from config.statements.config import Config
from config.query.query_config import QueryConfig
from controller.handler.customer_update_handler import customer_details_update_menu
from database.query_executor import QueryExecutor
from parking_manager.parking_slots import ParkingSlot
from parking_manager.slot_booking import SlotBooking
from utils.common import Common
from utils.validator.parking_manager_input_validation import ParkingManagerInputValidation
from utils.validator.user_input_validation import UserInputValidation

class EmployeeController(SlotBooking):
    """
        Class for maintaining all the methods or functionalities of Employee.
    """
    def register_customer(self) -> None:
        """
            Method to register customer.
        """ 
        print(Config.customer_details_input_prompt)
        cust_id = "CUST" + shortuuid.ShortUUID().random(length = 5)
        cust_name = UserInputValidation.input_name()
        cust_mobile_number = UserInputValidation.input_mobile_number()
        cust_vehicle_number = ParkingManagerInputValidation.input_vehicle_number()
        data =  QueryExecutor.fetch_data_from_database(
                    QueryConfig.query_for_fetching_customer_id_and_type_id_from_vehicle_no,
                    (cust_vehicle_number, )
                )
        if any(data):
            print(Config.customer_already_exist_prompt + "\n")
            return
        print(Config.input_type_name_prompt)
        vehicle_type_data = QueryExecutor.fetch_data_from_database(
                                QueryConfig.query_for_fetching_vehicle_type
                            )
        if not any(vehicle_type_data):
            print(Config.zero_record_prompt("vehicle_type"))
            return
        vehicle_type_name = [(vehicle[1],) for vehicle in vehicle_type_data]
        common_obj = Common()
        headers = ["Vehicle Type Name"]
        common_obj.display_table(vehicle_type_name, headers)
        choice = int(input(Config.enter_choice_prompt))
        if choice > len(vehicle_type_name) or choice < 1:
            print(Config.invalid_input_prompt)
        else:
            type_name = vehicle_type_name[choice-1][0]
            type_id =   QueryExecutor.fetch_data_from_database(
                            QueryConfig.query_for_fetching_vehicle_type_type_id_from_type_name,
                            (type_name, )
                        )
            type_id = type_id[0][0]
            QueryExecutor.save_data_in_database(
                QueryConfig.query_for_creating_customer,
                (cust_id, cust_name, cust_mobile_number, cust_vehicle_number, type_id),
                Config.customer_creation_successful_prompt + "\n"
            )

    def update_customer_details(self) -> None:
        self.view_customer_details()
        customer_details_update_menu()
    
    def view_customer_details(self) -> None:
        """
            Method to view customer details.
        """
        data =  QueryExecutor.fetch_data_from_database(
                    QueryConfig.query_for_viewing_customer_detail
                )
        if not any(data):
            print(Config.zero_record_prompt.format("customer"))
        else:
            common_obj = Common()
            headers = QueryConfig.customer_detail_header
            common_obj.display_table(data, headers)
    
    def view_parking_slot_details(self) -> None:
        """
            Method to view parking slot details.
        """
        parking_slot_obj = ParkingSlot()
        parking_slot_obj.view_parking_slot() 