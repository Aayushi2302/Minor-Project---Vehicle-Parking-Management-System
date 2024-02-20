"""Module responsible for invoking business logic for fetching all existing vehicle type."""

from src.config.prompts.prompts import Prompts
from src.business.vehicle_type_business import VehicleTypeBusiness
from src.models.database import Database
from src.utils.custom_error_handler import custom_error_handler
from src.utils.responses import SuccessResponse

class GetAllVehicleTypeController:
    """
        Class responsible for invoking business logic for fetching vehicle type.
        ...
        Methods
        -------
        get_all_vehicle_types(): dict -> method to get all existing vehicle types.
    """
    @custom_error_handler
    def get_all_vehicle_types(self) -> tuple:
        """
            Method to invoke business logic for fetching all vehicle type.
            Parameter -> None
            Return type -> dict
        """
        db = Database()
        vehicle_type_business_obj = VehicleTypeBusiness(db)
        vehicle_type_data = vehicle_type_business_obj.get_all_vehicle_type()

        return SuccessResponse.jsonify_data("Vehicle types fetched successfully.", vehicle_type_data), 200
