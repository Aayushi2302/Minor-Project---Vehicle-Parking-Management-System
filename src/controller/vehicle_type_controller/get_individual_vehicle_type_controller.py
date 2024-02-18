"""Module responsible for invoking business logic for fecthing detail of a particular vehicle type."""

from business.vehicle_type_business import VehicleTypeBusiness
from models.database import db
from utils.custom_error_handler import custom_error_handler
from utils.responses import SuccessResponse

class GetIndividualVehicleTypeController:
    """
        Class responsible for invoking business logic for fetching a particular vehicle type.
        ...
        Methods
        -------
        update_vehicle_type(): dict -> method to update a particular vehicle type.
    """
    @custom_error_handler
    def get_individual_vehicle_details(self, type_id: str) -> tuple:
        """
            Method to invoke business logic for fetching detail of a particular vehicle type.
            Parameter -> type_id: str
            Return type -> dict
        """
        vehicle_type_business_obj = VehicleTypeBusiness(db)
        data = vehicle_type_business_obj.get_individual_vehicle_type(type_id)

        return SuccessResponse.jsonify_data("Vehicle type details fetched successfully.", data), 200
