"""Module containing end points related to parking slot resource."""

from flask.views import MethodView
from flask_smorest import Blueprint

from config.app_config import AppConfig
from controller.parking_slot_controller.add_parking_slot_controller import AddParkingSlotController
from controller.parking_slot_controller.get_all_parking_slot_controller import GetAllParkingSlotController
from controller.parking_slot_controller.get_individual_parking_slot_controller import \
    GetIndividualParkingSlotContainer
from controller.parking_slot_controller.update_parking_slot_controller import UpdateParkingSlotController
from controller.parking_slot_controller.delete_parking_slot_controller import  DeleteParkingSlotController
from schemas.parking_slot_schemas import ParkingSlotSchema, ParkingSlotWriteResponseSchema, ParkingSlotUpdateSchema
from utils.route_access import route_access
from utils.role_mapping import RoleMapping

blp = Blueprint("parking-slot", __name__, description="Parking Slot related operations")


@blp.route("/v1/parking-slots")
class ParkingSlots(MethodView):
    """
        Class containing various methods applicable to /v1/parking-slots route.
        ...
        Methods
        -------
        POST
        GET
    """

    @blp.doc(parameters=[AppConfig.BLP_DOC_PARAMETERS])
    @blp.arguments(ParkingSlotSchema)
    @blp.response(201, ParkingSlotWriteResponseSchema)
    @route_access((RoleMapping["admin"], ))
    def post(self, parking_slot_data: dict) -> dict:
        """
            Method for creating parking slot.
            ...
            On Success -> Follows ParkingSlotWriteResponseSchema and returns success message.
            On Failure -> Returns success = False and error message.
        """
        return AddParkingSlotController().add_parking_slot(parking_slot_data)

    @blp.doc(parameters=[AppConfig.BLP_DOC_PARAMETERS])
    @blp.response(200, ParkingSlotSchema(many=True))
    @route_access((RoleMapping["admin"], RoleMapping["attendant"]))
    def get(self) -> dict:
        """
            Method for getting all existing parking slots.
            ...
            On Success -> Follows ParkingSlotSchema and returns parking slot details.
            On Failure -> Returns success = False and error message.
        """
        return GetAllParkingSlotController().get_all_parking_slots()


@blp.route("/v1/parking-slots/<string:parking_slot_no>")
class VehicleTypeUpdate(MethodView):
    """
        Class containing various methods applicable to /v1/parking-slot/{parking_slot_no} route.
        ...
        Methods
        -------
        PUT
        GET
        DELETE
    """

    @blp.doc(parameters=[AppConfig.BLP_DOC_PARAMETERS])
    @blp.arguments(ParkingSlotUpdateSchema)
    @blp.response(200, ParkingSlotWriteResponseSchema)
    @route_access((RoleMapping["admin"], ))
    def put(self, parking_slot_data: dict, parking_slot_no: str) -> dict:
        """
            Method for updating parking slot status.
            ...
            On Success -> Follows ParkingSlotWriteResponseSchema and returns success message.
            On Failure -> Returns success = False and error message.
        """
        return UpdateParkingSlotController().update_parking_slot(parking_slot_no, parking_slot_data)

    @blp.doc(parameters=[AppConfig.BLP_DOC_PARAMETERS])
    @blp.response(200, ParkingSlotSchema)
    @route_access((RoleMapping["admin"], ))
    def get(self, parking_slot_no: str) -> dict:
        """
            Method for fetching a particular parking slot.
            ...
            On Success -> Follows ParkingSlotSchema and returns parking slot details.
            On Failure -> Returns success = False and error message.
        """
        return GetIndividualParkingSlotContainer().get_individual_parking_slot(parking_slot_no)

    @blp.doc(parameters=[AppConfig.BLP_DOC_PARAMETERS])
    @blp.response(200, ParkingSlotWriteResponseSchema)
    @route_access((RoleMapping["admin"], ))
    def delete(self, parking_slot_no: str) -> dict:
        """
            Method for deleting a particular parking slot.
            ...
            On Success -> Follows ParkingSlotWriteResponseSchema and returns a success message.
            On Failure -> Returns success = False and error message.
        """
        return DeleteParkingSlotController().delete_parking_slot(parking_slot_no)