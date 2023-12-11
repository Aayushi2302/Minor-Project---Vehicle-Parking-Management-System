from config.query import QueryConfig
from models.database import db

class VehicleType:
    """This class contains methods for performing operations on vehicle_type."""
    def register_vehicle_type(self, type_id: str, type_name: str, price_per_hour: float) -> None:
        """Method for registering a vehicle_type."""
        db.save_data_to_database(
            QueryConfig.CREATE_VEHICLE_TYPE,
            (type_id, type_name, price_per_hour)
        )

    def get_vehicle_type_data_from_type_id(self, type_id: str) -> list:
        data =  db.fetch_data_from_database(
                    QueryConfig.FETCH_PRICE_PER_HOUR_FROM_TYPE_ID,
                    (type_id, )
                )
        return data

    def get_vehicle_type_id_from_type_name(self, type_name: str) -> list:
        data =  db.fetch_data_from_database(
                    QueryConfig.FETCH_VEHICLE_TYPE_ID_FROM_TYPE_NAME,
                    (type_name, )
                )
        return data

    def update_vehicle_type_detail(self, new_data: float, updated_field: str, type_id: str) -> None:
        """Method for updating vehicle price per hour for parking."""
        query_for_updating_vehicle_type_detail = QueryConfig.UPDATE_VEHICLE_TYPE_DETAIL_FROM_TYPE_ID.format(updated_field)
        db.save_data_to_database(
            query_for_updating_vehicle_type_detail,
            (new_data, type_id)
        )
       
    def get_all_vehicle_type(self) -> list:
        """Method for viewing details of vehicle_type."""
        data = db.fetch_data_from_database(QueryConfig.FETCH_VEHICLE_TYPE)
        return data