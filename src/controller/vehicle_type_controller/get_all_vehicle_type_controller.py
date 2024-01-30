from config.prompts.prompts import Prompts
from business.vehicle_type_business import VehicleTypeBusiness
from models.database import db
from utils.custom_error_handler import custom_error_handler
from utils.responses import SuccessResponse

class GetAllVehicleTypeController:

    @custom_error_handler
    def get_all_vehicle_types(self) -> dict:

        vehicle_type_business_obj = VehicleTypeBusiness(db)
        vehicle_type_data = vehicle_type_business_obj.get_all_vehicle_type()

        return SuccessResponse.jsonify_data(Prompts.VEHICLE_TYPE_GET_SUCCESS,
                                                vehicle_type_data), 200
