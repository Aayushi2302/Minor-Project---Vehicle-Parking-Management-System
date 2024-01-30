from config.prompts.prompts import Prompts
from business.parking_slot_business import ParkingSlotBusiness
from models.database import db
from utils.custom_error_handler import custom_error_handler
from utils.responses import SuccessResponse

class GetAllParkingSlotController:

    @custom_error_handler
    def get_all_parking_slots(self) -> dict:

        parking_slot_business_obj = ParkingSlotBusiness(db)
        response = parking_slot_business_obj.get_all_parking_slots()
        return SuccessResponse.jsonify_data(Prompts.PARKING_SLOT_GET_SUCCESS, response), 200
