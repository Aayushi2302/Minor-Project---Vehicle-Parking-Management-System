from config.app_config import AppConfig
from config.prompts.prompts import Prompts
from business.parking_slot_business import ParkingSlotBusiness
from models.database import db
from utils.custom_error_handler import custom_error_handler
from utils.responses import SuccessResponse

class UpdateParkingSlotContainer:

    @custom_error_handler
    def update_parking_slot(self, parking_slot_no: str, parking_slot_data: dict) -> dict:

        type_name = parking_slot_data[AppConfig.TYPE_NAME_ATTR].strip().capitalize()
        new_status = parking_slot_data[AppConfig.STATUS_ATTR].strip().lower()

        parking_slot_business_obj = ParkingSlotBusiness(db)
        response = parking_slot_business_obj.update_parking_slot_status(parking_slot_no, type_name, new_status)
        return SuccessResponse.jsonify_data(Prompts.PARKING_SLOT_UPDATE_SUCCESS, response), 200
