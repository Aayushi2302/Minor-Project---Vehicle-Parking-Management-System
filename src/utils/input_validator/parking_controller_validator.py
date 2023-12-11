"""Module for validating parking management related inputs."""
from datetime import datetime
import logging

from config.prompts.prompts import Prompts
from config.regex_pattern import RegexPattern
from utils.common_helper import CommonHelper

logger = logging.getLogger(__name__)
    
class ParkingControllerValidator:
    """
        This class contains methods for validating parking realted input.
        ...
        Methods
        -------
        input_vehicle_type_name() -> Method to take vehicle_type_name as input.
        input_price_per_hour() -> Method to take price per hour as input.
        input_vehcile_type_id() -> Method to take vehicle_type_id as input.
        input_parking_slot_number() -> Method to take parking_slot_number as input.
        input_vehicle_number() -> Method to take vehicle_number as input.
        input_out_date() -> Method to take out_date as input.
    """
    @staticmethod
    def input_vehicle_type_name() -> str:
        """
            Validation of vehicle_type name using regular expression.
            Parameter -> None
            Return type -> str
        """
        while True:
            type_name = input(Prompts.INPUT_TYPE_NAME).strip()
            is_valid_type_name = CommonHelper.input_validation(RegexPattern.STRING_REGEX, type_name)
            if is_valid_type_name:
                return type_name.title()

    @staticmethod
    def input_price_per_hour() -> float:
        """
            Validation of price_per_hour.
            Parameter -> None
            Return type -> float
        """
        while True:
            price_per_hour = input(Prompts.INPUT_PRICE)
            is_valid_price = CommonHelper.input_validation(RegexPattern.PRICE_REGEX, price_per_hour)
            if is_valid_price:
                return float(price_per_hour)

    @staticmethod
    def input_vehicle_type_id() -> str:
        """
            Validation of vehicle_type id using regular expression.
            Parameter -> None
            Return type -> str
        """
        while True:
            type_id = input(Prompts.INPUT_TYPE_ID).strip()
            is_valid_type_id = CommonHelper.input_validation(RegexPattern.TYPE_ID_REGEX, type_id)
            if is_valid_type_id:
                return type_id

    @staticmethod
    def input_parking_slot_number() -> str:
        """
            Validation of parking_slot no using regular expression.
            Parameter -> None
            Return type -> str
        """
        while True:
            parking_slot_no = input(Prompts.INPUT_PARKING_SLOT_NUMBER).strip()
            is_valid_parking_slot_no = CommonHelper.input_validation(RegexPattern.PARKING_SLOT_NUMBER_REGEX, parking_slot_no)
            if is_valid_parking_slot_no:
                return parking_slot_no.upper()

    @staticmethod
    def input_vehicle_number() -> str:
        """
            Validation of vehicle no using regular expression.
            Parameter -> None
            Return type -> str
        """
        while True:
            print(Prompts.VEHICLE_NUMBER_FORMAT + "\n")
            vehicle_number = input(Prompts.VEHICLE_NUMBER_INPUT).strip()
            is_valid_vehicle_number = CommonHelper.input_validation(RegexPattern.VEHICLE_NUMBER_REGEX, vehicle_number)
            if is_valid_vehicle_number:
                return vehicle_number

    @staticmethod
    def input_out_date() -> str:
        """
            Validation of out_date using regular expression.
            Parameter -> None
            Return type -> str
        """
        while True:
            out_date = input(Prompts.CUSTOMER_OUT_DATE_INPUT).strip()
            present = datetime.now().date()
            try:
                out_date = datetime.strptime(out_date, "%d-%m-%Y").date()
                if out_date < present:
                    print(Prompts.CANNOT_INPUT_PAST_DATE + "\n")
                else:
                    return out_date.strftime("%d-%m-%Y")
            except ValueError:
                print(Prompts.INVALID_INPUT + "\n")
