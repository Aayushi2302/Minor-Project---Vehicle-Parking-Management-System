from config.query import QueryConfig
from models.database import db

class ParkingSlot:
    """This class contains all methods for maintaining parking slot information."""
    def register_parking_slot(self, parking_slot_number: str, type_id: str) -> None:
        db.save_data_to_database(
            QueryConfig.CREATE_PARKING_SLOT,
            (parking_slot_number, type_id)
        )

    def get_parking_slot_status(self, parking_slot_number: str) -> list:
        data =  db.fetch_data_from_database(
                    QueryConfig.FETCH_STATUS_FROM_PARKING_SLOT_NUMBER,
                    (parking_slot_number, )
                )
        return data

    def get_all_parking_slots(self) -> list:
        data =  db.fetch_data_from_database(QueryConfig.VIEW_PARKING_SLOT_DETAIL)
        return data

    def update_parking_slot(self, parking_slot_number: str, updated_field: str, new_data: str) -> None:
        query_for_updating_parking_slot = QueryConfig.UPDATE_PARKING_SLOT_DETAIL_FROM_PARKING_SLOT_NO.format(updated_field)
        db.save_data_to_database(
            query_for_updating_parking_slot,
            (new_data, parking_slot_number)
        )
        