"""Module responsible for invoking business logic for updating a particular vehicle type."""

from config.app_config import AppConfig
from config.prompts.prompts import Prompts
from business.vehicle_type_business import VehicleTypeBusiness
from models.database import db
from utils.custom_error_handler import custom_error_handler
from utils.responses import SuccessResponse

class UpdateVehicleTypeController:
    """
        Class responsible for invoking business logic updating a particular vehicle type.
        ...
        Methods
        -------
        update_vehicle_type(): dict -> method to update a particular vehicle type.
    """
    @custom_error_handler
    def update_vehicle_type_details(self, type_id: str, vehicle_type_data: dict) -> tuple:
        """
            Method to invoke business logic for fetching updating a particular vehicle type.
            Parameter -> type_id: str, vehicle_type_data: dict
            Return type -> dict
        """
        vehicle_type_name = vehicle_type_data["vehicle_type_name"]
        price_per_hour = vehicle_type_data["price_per_hour"]

        vehicle_type_business_obj = VehicleTypeBusiness(db)
        vehicle_type_business_obj.update_vehicle_type(type_id, vehicle_type_name, price_per_hour)

        return SuccessResponse.jsonify_data("Vehicle type updated successfully."), 200
