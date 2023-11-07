# third party imports
import yaml

FILE_PATH = 'src\\logs\\logging_prompts.yaml'

class LogConfig:
    @classmethod
    def load(cls):
        with open(FILE_PATH, 'r') as file:
            data = yaml.safe_load(file)
        # main module logs
        cls.project_starting_info_prompt = data["project_starting_info"]
        cls.creating_database_connection_debug_prompt = data["creating_database_connection_debug"]
        cls.closing_database_connection_debug_prompt = data["closing_database_connection_debug"]
        cls.wrong_file_run_debug_prompt = data["wrong_file_run_debug"]

        # authentication module logs
        cls.first_login_info_prompt = data["first_login_info"]
        cls.successful_login_info_prompt = data["successful_login_info"]
        cls.invalid_login_info_prompt = data["invalid_login_info"]
        cls.successful_logout_info_prompt = data["successful_logout_info"]

        # query_executor logs
        cls.successful_authentication_table_creation_info_prompt = data["successful_authentication_table_creation_info"]
        cls.data_fetched_from_database_successful_info_prompt = data["data_fetched_from_database_successful_info"]
        cls.data_saved_to_database_successful_info_prompt = data["data_saved_to_database_successful_info"]
        cls.successful_employee_table_creation_info_prompt = data["successful_employee_table_creation_info"]
        cls.successful_vehicle_type_table_creation_info_prompt = data["successful_vehicle_type_table_creation_info"]
        cls.successful_parking_slot_table_creation_info_prompt = data["successful_parking_slot_table_creation_info"]
        cls.successful_customer_table_creation_info_prompt = data["successful_customer_table_creation_info"]
        cls.successful_slot_booking_table_creation_info_prompt = data["successful_slot_booking_table_creation_info"]

        # validator logs
        cls.invalid_input_exception_prompt = data["invalid_input_exception_info"]