"""
    Module for loading queries from yaml.
"""
import yaml

FILE_PATH = 'src\\config\\query\\query_collector.yaml'

class QueryConfig:
    """
        Class for loading queries from yaml.
    """
    @classmethod
    def load(cls):
        with open(FILE_PATH, 'r') as file:
            data = yaml.safe_load(file)
            
            # table headers
            cls.employee_detail_header = data["employee_detail_header"]
            cls.customer_detail_header = data["customer_detail_header"]
            cls.parking_slot_detail_header = data["parking_slot_detail_header"]
            cls.slot_booking_detail_header = data["slot_booking_detail_header"]
            cls.vehicle_type_detail_header = data["vehicle_type_detail_header"]

            # queries for authentication table
            cls.query_for_authentication_table_creation = data["authentication_table_creation"]
            cls.query_for_creating_employee_credentials = data["create_employee_credentials"]
            cls.query_for_fetching_employee_credentials = data["fetch_employee_credentials"]
            cls.query_for_fetching_authentication_table = data["fetch_authentication_table"]
            cls.query_for_fetching_default_password_from_emp_id = data["fetch_default_password_from_emp_id"]
            cls.query_for_fetching_emp_id_from_username = data["fetch_emp_id_from_username"]
            cls.query_for_fetching_emp_id_from_role_and_status = data["fetch_emp_id_from_role_and_status"]
            cls.query_for_updating_default_password = data["update_default_password"]
            cls.query_for_updating_employee_credential_from_emp_id = data["update_employee_credential_from_emp_id"]

            # queries for employee table
            cls.query_for_employee_table_creation = data["employee_table_creation"]
            cls.query_for_creating_employee_details = data["create_employee_details"]
            cls.query_for_fetching_emp_id_and_status_from_email = data["fetch_emp_id_and_status_from_email"]
            cls.query_for_updating_employee_detail_from_emp_id = data["update_employee_detail_from_empid"]
            cls.query_for_viewing_employee_detail = data["view_employee_detail"]
            cls.query_for_viewing_single_employee_detail = data["view_single_employee_detail"]

            # queries for vehicle_type table
            cls.query_for_vehicle_type_table_creation = data["vehicle_type_table_creation"]
            cls.query_for_creating_vehicle_type = data["create_vehicle_type"]
            cls.query_for_fetching_vehicle_type = data["fetch_vehicle_type"]
            cls.query_for_fetching_price_per_hour_from_type_id = data["fetch_price_per_hour_from_type_id"]
            cls.query_for_fetching_vehicle_type_type_id_from_type_name = data["fetch_vehicle_type_id_from_type_name"]
            cls.query_for_fetching_vehicle_type_from_type_name = data["fetch_vehicle_type_from_type_name"]
            cls.query_for_updating_vehicle_type_detail_from_type_id = data["update_vehicle_type_detail_from_type_id"]

            # queries for parking_slot table
            cls.query_for_parking_slot_table_creation = data["parking_slot_table_creation"]
            cls.query_for_creating_parking_slot = data["create_parking_slot"]
            cls.query_for_fetching_parking_slot_detail_from_parking_slot_no = data["fetch_parking_slot_detail_from_parking_slot_no"]
            cls.query_for_fetching_parking_slot_no_for_booking = data["fetch_parking_slot_no_for_booking"]
            cls.query_for_updating_parking_slot_detail_from_parking_slot_no = data["update_parking_slot_detail_from_parking_slot_no"]
            cls.query_for_viewing_parking_slot_detail = data["view_parking_slot_detail"]
            cls.query_for_deleting_parking_slot_from_parking_slot_no = data["delete_parking_slot_from_parking_slot_no"]

            # queries for customer table
            cls.query_for_customer_table_creation = data["customer_table_creation"]
            cls.query_for_creating_customer = data["create_customer"]
            cls.query_for_fetching_customer_id_and_type_id_from_vehicle_no = data["fetch_customer_id_and_type_id_from_vehicle_no"]
            cls.query_for_viewing_customer_detail = data["view_customer_detail"]
            cls.query_for_updating_customer_detail = data["update_customer_detail"]
            
            # queries for slot_booking table
            cls.query_for_slot_booking_table_creation = data["slot_booking_table_creation"]
            cls.query_for_creating_slot_booking = data["create_slot_booking"]
            cls.query_for_fetching_booking_detail_from_customer_id = data["fetch_booking_detail_from_customer_id"]
            cls.query_for_fetching_booking_detail_from_booking_id = data["fetch_booking_detail_from_booking_id"]
            cls.query_for_fetching_detail_for_vacating_parking_slot = data["fetch_detail_for_vacating_parking_slot"]
            cls.query_for_fetching_type_id_from_booking_id = data["fetch_type_id_from_booking_id"]
            cls.query_for_fetching_current_date_record = data["fetch_current_date_record"]
            cls.query_for_fetching_past_year_record = data["fetch_past_year_record"]
            cls.query_for_fetching_out_time_from_customer_id = data["fetch_out_time_from_customer_id"]
            cls.query_for_updating_slot_booking_detail = data["update_slot_booking_detail"]
            cls.query_for_updating_detail_for_vacating_parking_slot = data["update_detail_for_vacating_parking_slot"]
            cls.query_for_viewing_slot_booking_detail = data["view_slot_booking_detail"]