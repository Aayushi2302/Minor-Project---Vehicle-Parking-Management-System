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
    def update_vehicle_type(self, type_id: str, vehicle_type_data: dict) -> dict:
        """
            Method to invoke business logic for fetching updating a particular vehicle type.
            Parameter -> type_id: str, vehicle_type_data: dict
            Return type -> dict
        """
        type_name = vehicle_type_data[AppConfig.TYPE_NAME_ATTR]
        price_per_hour = vehicle_type_data[AppConfig.PRICE_PER_HOUR_ATTR]

        vehicle_type_business_obj = VehicleTypeBusiness(db)
        vehicle_type_business_obj.update_vehicle_type(type_id, type_name, price_per_hour)

        return SuccessResponse.jsonify_data(Prompts.VEHICLE_TYPE_UPDATE_SUCCESS), 200
