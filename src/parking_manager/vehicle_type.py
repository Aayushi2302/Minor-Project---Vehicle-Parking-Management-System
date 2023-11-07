"""
    Module for performing operations related to vehicle_type(like car, truck, etc.) allowed for parking.
"""
import shortuuid

from config.statements.config import Config
from config.query.query_config import QueryConfig
from database.query_executor import QueryExecutor
from utils.common import Common
from utils.validator.parking_manager_input_validation import ParkingManagerInputValidation

class VehicleType:
    """
        Class for performing operations on vehicle_type.
    """
    def register_vehicle_type(self) -> None:
        """
            Method for registering a vehicle_type.
        """
        type_name = ParkingManagerInputValidation.input_vehicle_type_name()
        price_per_hour = ParkingManagerInputValidation.input_price_per_hour()
        data =   QueryExecutor.fetch_data_from_database(
                    QueryConfig.query_for_fetching_vehicle_type_from_type_name,
                    (type_name, )
                )
        if any(data):
            print(Config.vehicle_type_already_exist_prompt + "\n")
        else:
            type_id = "TYPE" + shortuuid.ShortUUID().random(length = 5)
            QueryExecutor.save_data_in_database(
                QueryConfig.query_for_creating_vehicle_type,
                (type_id, type_name, price_per_hour),
                Config.vehicle_type_registration_successful_prompt + "\n"
            )
        
    def update_vehicle_price_per_hour(self) -> None:
        """
            Method for updating vehicle price per hour for parking.
        """
        self.view_vehicle_type()
        print("\n" + Config.input_details_for_updation_prompt + "\n")
        type_id = ParkingManagerInputValidation.input_vehicle_type_id()
        data =  QueryExecutor.fetch_data_from_database(
                    QueryConfig.query_for_fetching_price_per_hour_from_type_id,
                    (type_id, )
                )
        if not any(data):
            print(Config.typeid_does_not_exist_prompt + "\n")
            return
        else:
            curr_price_per_hour = data[0][0]
            print(Config.current_price_per_hour_prompt.format(curr_price_per_hour) + "\n")
            print(Config.new_detail_input_prompt.format("Price Per Hour"))
            new_data = ParkingManagerInputValidation.input_price_per_hour()
            query = QueryConfig.query_for_updating_vehicle_type_detail_from_type_id.format("price_per_hour")
            QueryExecutor.save_data_in_database(
                query,
                (new_data, type_id),
                Config.vehicle_type_details_updation_successful_prompt + "\n"
            )

    def view_vehicle_type(self) -> None:
        """
            Method for viewing details of vehicle_type.
        """
        data = QueryExecutor.fetch_data_from_database(
                    QueryConfig.query_for_fetching_vehicle_type
                )
        if not any(data):
            print(Config.zero_record_prompt("vehicle_type"))
        else:
            common_obj = Common()
            headers = QueryConfig.vehicle_type_detail_header
            common_obj.display_table(data, headers)