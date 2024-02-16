"""Module containing end points related to parking slot reservation."""

from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint

from src.config.app_config import AppConfig
from src.controller.slot_reservation_controller.reserve_parking_slot_controller import ReserveParkingSlotController
from src.controller.slot_reservation_controller.get_reservations_controller import GetReservationsController
from src.controller.slot_reservation_controller.vacate_parking_slot_controller import VacateParkingSlotController
from src.schemas.slot_reservation_schema import SlotReservationSchema, SlotReservationGetSchema, SlotVacateSchema
from src.utils.route_access import route_access
from src.utils.role_mapping import RoleMapping

blp = Blueprint("slot-reservation", __name__, description="Parking Slot Reservation related operations")


@blp.route("/v1/reserve/parking-slot")
class ParkingSlotReservation(MethodView):
    """
        Class containing various methods applicable to /v1/reserve/parking-slot route.
        ...
        Methods
        -------
        POST
    """

    @blp.doc(parameters=[AppConfig.BLP_DOC_PARAMETERS])
    @blp.arguments(SlotReservationSchema)
    @blp.response(201, SlotReservationSchema)
    @route_access((RoleMapping["attendant"], ))
    def post(self, cust_data: dict) -> dict:
        """
            Method for reserving parking slot.
            ...
            On Success -> Follows SlotReservationSchema and returns success message.
            On Failure -> Returns success = False and error message.
        """
        return ReserveParkingSlotController().reserve_parking_slot(cust_data)


@blp.route("/v1/reservations")
class GetReservations(MethodView):
    """
        Class containing various methods applicable to /v1/reservations route.
        ...
        Methods
        -------
        GET
    """

    @blp.doc(parameters=[AppConfig.BLP_DOC_PARAMETERS])
    @blp.response(200, SlotReservationGetSchema(many=True))
    @route_access((RoleMapping["admin"], RoleMapping["attendant"]))
    def get(self) -> dict:
        """
            Method for getting reservation details either all, date-wise or year-wise.
            ...
            On Success -> Follows SlotReservationGetSchema and returns booking details.
            On Failure -> Returns success = False and error message.
        """
        date_parm = request.args.get("date")
        year_parm = request.args.get("year")

        if not date_parm or not year_parm:
            return GetReservationsController().get_reservation_details()
        elif not date_parm:
            return GetReservationsController().get_reservation_details(year_parm)
        else:
            return GetReservationsController().get_reservation_details(date_parm)


@blp.route("/v1/vacate/parking-slot")
class VehicleTypeUpdate(MethodView):
    """
        Class containing various methods applicable to /v1/vacate/parking-slot route.
        ...
        Methods
        -------
        PUT
    """

    @blp.doc(parameters=[AppConfig.BLP_DOC_PARAMETERS])
    @blp.arguments(SlotVacateSchema)
    @blp.response(200, SlotVacateSchema)
    @route_access((RoleMapping["attendant"], ))
    def put(self, cust_data: dict) -> dict:
        """
            Method for vacating parking slot.
            ...
            On Success -> Follows SlotVacateSchema and returns hours spent along with charges.
            On Failure -> Returns success = False and error message.
        """
        return VacateParkingSlotController().vacate_parking_slot(cust_data)
