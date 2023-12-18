"""Module containing parking slot controller logic."""

from config.query import QueryConfig
from models.database import db
from controller.parking_controller.vehicle_type import VehicleType

class ParkingSlot:
    """
        Class contaning methods and attributes to manage parking slot information.
        ...
        Attributes:
        ----------
        vehicle_type_obj : VehicleType

        Methods:
        -------
        register_parking_slot() -> method to register parking slot.
        get_parking_slot_status() -> method for fetching parking slot status.
        get_all_parking_slots() -> method to fetch all parking slot details.
        update_parking_slot_status() -> method to update parking slot status.
    """
    def __init__(self) -> None:
        """
            Method for constructing parking slot object.
            Parameter -> self
            Return type -> None
        """
        self.vehicle_type_obj = VehicleType()

    def register_parking_slot(self, parking_slot_number: str, vehicle_type_name: str) -> bool:
        """
            Method to register parking slot.
            Parameter -> self, parking_slot_number: str, vehicle_type_name: str
            Return type -> bool
        """
        data = self.vehicle_type_obj.get_vehicle_type_id_from_type_name(vehicle_type_name)

        if not data:
            return False

        type_id = data[0][0]
        db.save_data_to_database(
            QueryConfig.CREATE_PARKING_SLOT,
            (parking_slot_number, type_id)
        )
        return True

    def get_parking_slot_status(self, parking_slot_number: str) -> list:
        """
            Method to fetch parking slot status.
            Parameter -> self, parking_slot_number: str
            Return type -> list
        """
        data =  db.fetch_data_from_database(
                    QueryConfig.FETCH_STATUS_FROM_PARKING_SLOT_NUMBER,
                    (parking_slot_number, )
                )
        return data

    def get_all_parking_slots(self) -> list:
        """
            Method to fetch all parking slot details.
            Parameter -> self
            Return type -> list
        """
        data =  db.fetch_data_from_database(QueryConfig.VIEW_PARKING_SLOT_DETAIL)
        return data

    def update_parking_slot_status(
            self, parking_slot_number: str,
            updated_field: str,
            new_status: str
    ) -> int:
        """
            Method to update parking slot details.
            Parameter -> self, parking_slot_number: str, updated_field: str, new_status: str
            Return type -> int
        """
        data = self.get_parking_slot_status(parking_slot_number)

        if not data:
            return -1

        status = data[0][0]

        if status == new_status:
            return 0

        query_for_updating_parking_slot = QueryConfig.\
                                          UPDATE_PARKING_SLOT_DETAIL_FROM_PARKING_SLOT_NO.\
                                          format(updated_field)
        db.save_data_to_database(
            query_for_updating_parking_slot,
            (new_status, parking_slot_number)
        )
        return 1
        