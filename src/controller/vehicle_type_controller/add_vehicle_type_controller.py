"""Module responsible for invoking business logic for adding vehicle type."""

from config.prompts.prompts import Prompts
from business.vehicle_type_business import VehicleTypeBusiness
from models.database import db
from utils.custom_error_handler import custom_error_handler
from utils.responses import SuccessResponse

class AddVehicleTypeController:
    """
        Class responsible for invoking business logic for adding vehicle type.
        ...
        Methods
        -------
        add_vehicle_type(): dict -> method to add vehicle type.
    """
    @custom_error_handler
    def add_vehicle_type(self, vehicle_type_data: dict) -> tuple:
        """
            Method to invoke business logic for adding vehicle type.
            Parameter -> vehicle_type_data: dict
            Return type -> dict
        """
        vehicle_type_name = vehicle_type_data["vehicle_type_name"]
        price_per_hour = vehicle_type_data["price_per_hour"]

        vehicle_type_business_obj = VehicleTypeBusiness(db)
        vehicle_type_business_obj.register_vehicle_type(vehicle_type_name, price_per_hour)

        return SuccessResponse.jsonify_data("Vehicle type registered successfully."), 200
