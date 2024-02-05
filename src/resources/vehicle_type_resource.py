"""Module containg end points related to vehicle type resource."""

from flask.views import MethodView
from flask_smorest import Blueprint
from schemas.vehicle_type_schema import VehicleTypeSchema, VehicleTypeResponseSchema

from config.app_config import AppConfig
from controller.vehicle_type_controller.add_vehicle_type_controller import AddVehicleTypeController
from controller.vehicle_type_controller.get_all_vehicle_type_controller import GetAllVehicleTypeController
from controller.vehicle_type_controller.update_vehicle_type_controller import UpdateVehicleTypeController
from controller.vehicle_type_controller.get_individual_vehicle_type_controller import GetIndividualVehicleTypeController
from utils.decorators import role_based_access
from utils.role_mapping import RoleMapping

blp = Blueprint("vehilce_type", __name__, description = "Vehicle Type related operations")

@blp.route("/v1/vehicle-types")
class VehicleTypeCreate(MethodView):
    """
        Class containing various methods applicable to /v1/vehicle_types route.
        ...
        Methods
        -------
        POST
        GET
    """
    @blp.doc(parameters = [AppConfig.BLP_DOC_PARAMETERS])
    @blp.arguments(VehicleTypeSchema)
    @blp.response(201, VehicleTypeResponseSchema)
    @role_based_access((RoleMapping["ADMIN"]))
    def post(self, vehicle_type_data: dict) -> dict:
        """
            Method for creating vehicle type.
            ...
            On Success -> Follows VehicleTypeResponseSchema and returns success message.
            On Failure -> Returns success = False and error message.
        """
        return AddVehicleTypeController().add_vehicle_type(vehicle_type_data)

    @blp.doc(parameters = [AppConfig.BLP_DOC_PARAMETERS])
    @blp.response(200, VehicleTypeSchema(many=True))
    @role_based_access((RoleMapping["ADMIN"]))
    def get(self) -> dict:
        """
            Method for creating vehicle type.
            ...
            On Success -> Follows VehicleTypeSchema and returns vehicle type details.
            On Failure -> Returns success = False and error message.
        """
        return GetAllVehicleTypeController().get_all_vehicle_types()

@blp.route("/vehicle-type/<string:type_id>")
class VehicleTypeUpdate(MethodView):
    """
        Class containing various methods applicable to /v1/vehicle_type/{vehicle_type_id} route.
        ...
        Methods
        -------
        PUT
        GET
    """
    @blp.doc(parameters = [AppConfig.BLP_DOC_PARAMETERS])
    @blp.arguments(VehicleTypeSchema)
    @blp.response(200, VehicleTypeResponseSchema)
    @role_based_access((RoleMapping["ADMIN"]))
    def put(self, vehicle_type_data: dict, type_id: str) -> dict:
        """
            Method for updating vehicle type.
            ...
            On Success -> Follows VehicleTypeResponseSchema and returns success message.
            On Failure -> Returns success = False and error message.
        """
        return UpdateVehicleTypeController().update_vehicle_type(type_id, vehicle_type_data)

    @blp.doc(parameters = [AppConfig.BLP_DOC_PARAMETERS])
    @blp.response(200, VehicleTypeSchema)
    @role_based_access((RoleMapping["ADMIN"]))
    def get(self, type_id: str) -> dict:
        """
            Method for fetching a particular vehicle type.
            ...
            On Success -> Follows VehicleTypeSchema and returns vehicle type details.
            On Failure -> Returns success = False and error message.
        """
        return GetIndividualVehicleTypeController().get_individual_vehicle_type(type_id)
