"""Module containing controller logic for vehicle type module."""

from config.query import QueryConfig
from models.database import db

class VehicleType:
    """
        Class containing methods for performing operations on vehicle_type.
        ...
        Methods:
        -------
        register_vehicle_type() -> method to register vehicle type.
        get_vehicle_type_data_from_type_id() -> method to fetch vehcile type data.
        get_vehicle_type_id_from_type_name() -> method to fetch vehicle type id.
        update_vehicle_type_details() -> method to update vehicle type details.
        get_all_vehicle_type() -> method to get all vehicle type.
    """
    def register_vehicle_type(self, type_id: str, type_name: str, price_per_hour: float) -> None:
        """
            Method for registering a vehicle_type.
            Parameter -> self, type_id: str, type_name: str, price_per_hour: float
            Return type -> None
        """
        db.save_data_to_database(
            QueryConfig.CREATE_VEHICLE_TYPE,
            (type_id, type_name, price_per_hour)
        )

    def get_vehicle_type_data_from_type_id(self, type_id: str) -> list:
        """
            Method to fetch vehicle type data.
            Parameter -> self, type_id: str
            Return type -> list
        """
        data =  db.fetch_data_from_database(
                    QueryConfig.FETCH_PRICE_PER_HOUR_FROM_TYPE_ID,
                    (type_id, )
                )
        return data

    def get_vehicle_type_id_from_type_name(self, type_name: str) -> list:
        """
            Method to fetch vehicle type id.
            Parameter -> self, type_name: str
            Return type -> list
        """
        data =  db.fetch_data_from_database(
                    QueryConfig.FETCH_VEHICLE_TYPE_ID_FROM_TYPE_NAME,
                    (type_name, )
                )
        return data

    def update_vehicle_type_detail(self, type_id: str, updated_field: str, new_data: str) -> bool:
        """
            Method for updating vehicle price per hour for parking.
            Parameter -> self, type_id: str, updated_field: str, new_data: str
            Return type -> bool
        """
        data = self.get_vehicle_type_data_from_type_id(type_id)

        if not data:
            return False

        query_for_updating_vehicle_type_detail = QueryConfig.\
                                                 UPDATE_VEHICLE_TYPE_DETAIL_FROM_TYPE_ID.\
                                                 format(updated_field)
        db.save_data_to_database(
            query_for_updating_vehicle_type_detail,
            (new_data, type_id)
        )
        return True

    def get_all_vehicle_type(self) -> list:
        """
            Method for viewing details of vehicle_type.
            Parameter -> self
            Return type -> list
        """
        data = db.fetch_data_from_database(QueryConfig.FETCH_VEHICLE_TYPE)
        return data
        