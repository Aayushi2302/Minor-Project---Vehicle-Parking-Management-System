"""
    Module for maintaining parking slot details.
"""
from config.statements.config import Config
from config.query.query_config import QueryConfig
from database.query_executor import QueryExecutor
from utils.common import Common
from utils.validator.parking_manager_input_validation import ParkingManagerInputValidation

class ParkingSlot:
    """
        Class for maintaining parking slot information.
    """
    def register_or_activate_parking_slot(self) -> None:
        """
            Method to register or activate parking slot.
        """
        parking_slot_number = ParkingManagerInputValidation.input_parking_slot_number()
        parking_slot_data = QueryExecutor.fetch_data_from_database(
                                QueryConfig.query_for_fetching_parking_slot_detail_from_parking_slot_no,
                                (parking_slot_number, )
                            )
        if not any(parking_slot_data):
            vehicle_type_name = ParkingManagerInputValidation.input_vehicle_type_name()
            vehicle_type_data =  QueryExecutor.fetch_data_from_database(
                                    QueryConfig.query_for_fetching_vehicle_type_type_id_from_type_name,
                                    (vehicle_type_name, )
                                )
            if not any(vehicle_type_data):
                print(Config.vehicle_type_does_not_exist_prompt + "\n")
                return
            else:
                type_id = vehicle_type_data[0][0]
                QueryExecutor.save_data_in_database(
                    QueryConfig.query_for_creating_parking_slot,
                    (parking_slot_number, type_id),
                    Config.parking_slot_registration_successful_prompt + "\n"
                )
        else:
            status = parking_slot_data[0][2]
            if status == "vacant":
                print(Config.parking_slot_number_already_exist_prompt + "\n")
                return
            else:
                query_for_updating_parking_slot_status = QueryConfig.query_for_updating_parking_slot_detail_from_parking_slot_no.format("status")
                QueryExecutor.save_data_in_database(
                    query_for_updating_parking_slot_status,
                    ("vacant", parking_slot_number),
                    Config.parking_slot_activation_successful_prompt + "\n"
                )
        
    def deactivate_parking_slot(self) -> None:
        """
            Method to deactivate aprking slot.
        """
        self.view_parking_slot()
        print("\n" + Config.input_details_for_updation_prompt + "\n")
        parking_slot_number = ParkingManagerInputValidation.input_parking_slot_number()
        data =  QueryExecutor.fetch_data_from_database(
                    QueryConfig.query_for_fetching_parking_slot_detail_from_parking_slot_no,
                    (parking_slot_number, )
                )
        if not any(data):
            print(Config.parking_slot_number_does_not_exist_prompt + "\n")
            return
        status = data[0][2]
        if status == "inactive":
            print(Config.updating_details_for_inactive_status_prompt + "\n")
        else:
            query_for_updating_parking_slot_status = QueryConfig.query_for_updating_parking_slot_detail_from_parking_slot_no.format("status")
            QueryExecutor.save_data_in_database(
                query_for_updating_parking_slot_status,
                ("inactive", parking_slot_number),
                Config.parking_slot_deactivation_successful_prompt + "\n"
            )

    def view_parking_slot(self) -> None:
        """
            Method to view parking slot details.
        """
        data =  QueryExecutor.fetch_data_from_database(
                    QueryConfig.query_for_viewing_parking_slot_detail
                )
        if not any(data):
            print(Config.zero_record_prompt.format("parking_slot"))
        else:
            common_obj = Common()
            headers = QueryConfig.parking_slot_detail_header
            common_obj.display_table(data, headers)

    def remove_parking_slot(self) -> None:
        """
            Method to remove parking slot.
        """
        self.view_parking_slot()
        print("\n" + Config.input_details_for_updation_prompt + "\n")
        parking_slot_number = ParkingManagerInputValidation.input_parking_slot_number()
        data =  QueryExecutor.fetch_data_from_database(
                    QueryConfig.query_for_fetching_parking_slot_detail_from_parking_slot_no,
                    (parking_slot_number, )
                )
        if not any(data):
            print(Config.parking_slot_number_does_not_exist_prompt + "\n")
            return
        query_for_deleting_parking_slot = QueryConfig.query_for_updating_parking_slot_detail_from_parking_slot_no.format("status")
        QueryExecutor.save_data_in_database(
            query_for_deleting_parking_slot,
            ("deleted", parking_slot_number, ),
            Config.parking_slot_deletion_successful_prompt + "\n"
        )