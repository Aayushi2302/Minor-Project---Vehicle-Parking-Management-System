from mysql import connector

from config.app_config import AppConfig
from config.prompts.prompts import Prompts
from config.query import QueryConfig
from config.regex_pattern import RegexPattern
from models.database import Database
from utils.common_helper import CommonHelper
from utils.custom_exceptions import DataAlreadyExists, DBException, DataNotFound, CustomBaseException, InvalidRegex

class VehicleTypeBusiness:

    def __init__(self, db: Database) -> None:
        self.db = db

    def register_vehicle_type(self, type_name: str, price_per_hour: str) -> dict:
        try:
            type_id = CommonHelper.generate_shortuuid(AppConfig.VEHICLE_TYPE)
            self.db.save_data_to_database(
                QueryConfig.CREATE_VEHICLE_TYPE,
                (type_id, type_name, price_per_hour)
            )
            return  {
                        AppConfig.TYPE_ID_ATTR : type_id,
                        AppConfig.TYPE_NAME_ATTR : type_name,
                        AppConfig.PRICE_PER_HOUR_ATTR : price_per_hour
                    }

        except connector.IntegrityError as error:
            failed_attribute = CommonHelper.get_constraint_failed_attribute(error.msg)
            raise DataAlreadyExists(409, Prompts.ERROR_STATUS_409, 
                                        Prompts.VEHICLE_TYPE_CONFLICT_MSG.format(failed_attribute))

        except connector.Error:
            raise DBException(500, Prompts.ERROR_STATUS_500, Prompts.INTERNAL_SERVER_ERROR_MSG)

    def get_all_vehicle_type(self) -> list:
        try:
            data = self.db.fetch_data_from_database(QueryConfig.FETCH_VEHICLE_TYPE)

            if not data:
                raise DataNotFound(404, Prompts.ERROR_STATUS_404, Prompts.VEHICLE_TYPE_NOT_FOUND)

            return data
        except connector.Error:
            raise DBException(500, Prompts.ERROR_STATUS_500, Prompts.INTERNAL_SERVER_ERROR_MSG)

    def get_vehicle_type_id_from_type_name(self, type_name: str) -> str:
        try:
            data =  self.db.fetch_data_from_database(
                        QueryConfig.FETCH_VEHICLE_TYPE_ID_FROM_TYPE_NAME,
                        (type_name, )
                    )
            return data[0]

        except connector.Error:
            raise DBException(500, Prompts.ERROR_STATUS_500, Prompts.INTERNAL_SERVER_ERROR_MSG)

    def get_vehicle_type_name_from_type_id(self, type_id: str) -> list:
        try:
            data =  self.db.fetch_data_from_database(
                        QueryConfig.FETCH_VEHICLE_TYPE_NAME_FROM_TYPE_ID,
                        (type_id, )
                    )
            return data[0]

        except connector.Error:
            raise DBException(500, Prompts.ERROR_STATUS_500, Prompts.INTERNAL_SERVER_ERROR_MSG)

    def update_vehicle_type(self, type_id: str, type_name: str, new_price_per_hour: str) -> None:
        try:

            result = CommonHelper.input_validation(RegexPattern.TYPE_ID_REGEX, type_id)

            if not result:
                raise InvalidRegex(422, Prompts.ERROR_STATUS_422, 
                                    Prompts.VEHICLE_TYPE_ID_REGEX_INVALID)

            data = self.get_vehicle_type_name_from_type_id(type_id)

            if not data:
                raise DataNotFound(404, Prompts.ERROR_STATUS_404, Prompts.VEHICLE_TYPE_NOT_FOUND)

            if type_name != data[AppConfig.TYPE_NAME_ATTR]:
                raise CustomBaseException(400, Prompts.ERROR_STATUS_400,
                                            Prompts.CANNOT_UPDATE_VEHICLE_TYPE_NAME)

            self.db.save_data_to_database(
                QueryConfig.UPDATE_VEHICLE_TYPE_DETAIL_FROM_TYPE_ID,
                (type_name, new_price_per_hour, type_id)
            )

            return  {
                        AppConfig.TYPE_ID_ATTR : type_id,
                        AppConfig.TYPE_NAME_ATTR : type_name,
                        AppConfig.PRICE_PER_HOUR_ATTR : new_price_per_hour
                    }

        except connector.Error:
            raise DBException(500, Prompts.ERROR_STATUS_500, Prompts.INTERNAL_SERVER_ERROR_MSG)
