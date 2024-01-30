from config.app_config import AppConfig
from config.prompts.prompts import Prompts
from business.vehicle_type_business import VehicleTypeBusiness
from models.database import db
from utils.custom_error_handler import custom_error_handler
from utils.responses import SuccessResponse

class AddVehicleTypeController:

    @custom_error_handler
    def add_vehicle_type(self, vehicle_type_data: dict) -> dict:

        type_name = vehicle_type_data[AppConfig.TYPE_NAME_ATTR].strip().capitalize()
        price_per_hour = vehicle_type_data[AppConfig.PRICE_PER_HOUR_ATTR]

        vehicle_type_business_obj = VehicleTypeBusiness(db)
        response = vehicle_type_business_obj.register_vehicle_type(type_name, price_per_hour)

        return SuccessResponse.jsonify_data(Prompts.VEHICLE_TYPE_REGISTER_SUCCESS,
                                                response), 200
