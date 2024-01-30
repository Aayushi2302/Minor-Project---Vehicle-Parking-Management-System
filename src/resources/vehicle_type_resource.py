from flask.views import MethodView
from flask_smorest import Blueprint
from schemas.vehicle_type_schema import VehicleTypeSchema

from controller.vehicle_type_controller.add_vehicle_type_controller import AddVehicleTypeController
from controller.vehicle_type_controller.get_all_vehicle_type_controller import GetAllVehicleTypeController
from controller.vehicle_type_controller.update_vehicle_type_controller import UpdateVehicleTypeController
from utils.decorators import role_based_access
from utils.role_mapping import RoleMapping

blp = Blueprint("vehilce_type", __name__, description = "Vehicle Type related operations")

@blp.route("/vehicle-type")
class VehicleTypeCreate(MethodView):

    @role_based_access((RoleMapping["ADMIN"]))
    @blp.doc(
        parameters = [
        {
            'name': 'Authorization',
            'in': 'header',
            'description': 'Authorization: Bearer <access_token>',
            'required': 'true'
        }
    ])
    @blp.arguments(VehicleTypeSchema)
    @blp.response(201, VehicleTypeSchema)
    def post(self, vehicle_type_data: dict):
        return AddVehicleTypeController().add_vehicle_type(vehicle_type_data)

@blp.route("/vehicle-type/all")
class VehicleTypeGet(MethodView):

    @role_based_access((RoleMapping["ADMIN"], RoleMapping["ATTENDANT"]))
    @blp.doc(
        parameters = [
        {
            'name': 'Authorization',
            'in': 'header',
            'description': 'Authorization: Bearer <access_token>',
            'required': 'true'
        }
    ])
    @blp.response(200, VehicleTypeSchema)
    def get(self):
        return GetAllVehicleTypeController().get_all_vehicle_types()

@blp.route("/vehicle-type/<string:type_id>")
class VehicleTypeUpdate(MethodView):

    @role_based_access((RoleMapping["ADMIN"]))
    @blp.doc(
        parameters = [
        {
            'name': 'Authorization',
            'in': 'header',
            'description': 'Authorization: Bearer <access_token>',
            'required': 'true'
        }
    ])
    @blp.arguments(VehicleTypeSchema)
    @blp.response(200, VehicleTypeSchema)
    def put(self, vehicle_type_data: dict, type_id: str):
        return UpdateVehicleTypeController().update_vehicle_type(type_id, vehicle_type_data)
