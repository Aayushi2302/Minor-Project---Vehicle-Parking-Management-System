from config.app_config import AppConfig
from config.prompts.prompts import Prompts
from business.parking_slot_business import ParkingSlotBusiness
from models.database import db
from utils.custom_error_handler import custom_error_handler
from utils.responses import SuccessResponse

class AddParkingSlotController:

    @custom_error_handler
    def add_parking_slot(self, parking_slot_data: dict) -> dict:

        parking_slot_no = parking_slot_data["parking_slot_no"].strip()
        type_name = parking_slot_data["type_name"].strip().capitalize()

        parking_slot_business_obj = ParkingSlotBusiness(db)
        response = parking_slot_business_obj.register_parking_slot(parking_slot_no, type_name)
        return SuccessResponse.jsonify_data(Prompts.PARKING_SLOT_REGISTER_SUCCESS, response), 200
