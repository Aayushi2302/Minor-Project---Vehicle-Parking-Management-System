from mysql import connector

from config.app_config import AppConfig
from config.prompts.prompts import Prompts
from config.query import QueryConfig
from business.vehicle_type_business import VehicleTypeBusiness
from models.database import Database
from utils.custom_exceptions import DataNotFound, DataAlreadyExists, DBException, CustomBaseException

class ParkingSlotBusiness:

    def __init__(self, db: Database) -> None:
        self.db = db
        self.vehicle_type_business_obj = VehicleTypeBusiness(db)
    
    def register_parking_slot(self, parking_slot_no: str, type_name: str) -> dict:
        try:
            data = self.vehicle_type_business_obj.get_vehicle_type_id_from_type_name(type_name)

            if not data:
                raise DataNotFound(404, Prompts.ERROR_STATUS_404, Prompts.VEHICLE_TYPE_NOT_FOUND)

            type_id = data["type_id"]

            self.db.save_data_to_database(
                QueryConfig.CREATE_PARKING_SLOT,
                (parking_slot_no, type_id)
            )
            return  {
                        "parking_slot_no" : parking_slot_no,
                        "type_name" : type_name,
                        "status" : AppConfig.PARKING_SLOT_STATUS_VACANT
                    }
       
        except connector.IntegrityError as error:
            raise DataAlreadyExists(409, Prompts.ERROR_STATUS_409, Prompts.PARKING_SLOT_CONFLICT_MSG)

        except connector.Error:
            raise DBException(500, Prompts.ERROR_STATUS_500, Prompts.INTERNAL_SERVER_ERROR_MSG)

    def get_all_parking_slots(self) -> list:
        try:
            data =  self.db.fetch_data_from_database(QueryConfig.VIEW_PARKING_SLOT_DETAIL)
             
            if not data:
                raise DataNotFound(404, Prompts.ERROR_STATUS_404, Prompts.PARKING_SLOT_NOT_FOUND)

            return data

        except connector.Error:
            raise DBException(500, Prompts.ERROR_STATUS_500, Prompts.INTERNAL_SERVER_ERROR_MSG)

    def get_parking_slot_detail(self, parking_slot_number: str) -> dict:
        try:
            data =  self.db.fetch_data_from_database(
                        QueryConfig.FETCH_PARKING_SLOT_DETAIL_FROM_PARKING_SLOT_NUMBER,
                        (parking_slot_number, )
                    )
            return data[0]

        except connector.Error:
            raise DBException(500, Prompts.ERROR_STATUS_500, Prompts.INTERNAL_SERVER_ERROR_MSG)

    def update_parking_slot_status(self, parking_slot_no: str, type_name: str, new_status: str) -> dict:
        try:
            data = self.get_parking_slot_detail(parking_slot_no)

            if not data:
                raise DataNotFound(404, Prompts.ERROR_STATUS_404, Prompts.PARKING_SLOT_NOT_FOUND)

            if type_name != data["type_name"]:
                raise CustomBaseException(400, Prompts.ERROR_STATUS_400, Prompts.CANNOT_UPDATE_VEHICLE_TYPE_NAME)

            self.db.save_data_to_database(
                QueryConfig.UPDATE_PARKING_SLOT_STATUS_FROM_PARKING_SLOT_NO,
                (new_status, parking_slot_no)
            )

            return  {
                        "parking_slot_no" : parking_slot_no,
                        "type_name" : type_name,
                        "status" : new_status
                    }

        except connector.Error:
            raise DBException(500, Prompts.ERROR_STATUS_500, Prompts.INTERNAL_SERVER_ERROR_MSG)
