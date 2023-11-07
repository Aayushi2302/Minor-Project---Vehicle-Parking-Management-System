"""
    Module for validating parking management related inputs.
"""
from datetime import datetime
import logging
import re

from config.statements.config import Config
from logs.logs_config import LogConfig

TYPE_ID_REGEX = r"^TYPE[a-zA-Z0-9]+$"
STRING_REGEX = r"^[a-zA-Z]+\s*"
PARKING_SLOT_NUMBER_REGEX = r"^PSN[0-9]+$"
VEHICLE_NUMBER_REGEX =r"^[A-Z]{2}[-][0-9]{2}[-][A-Z]{2}[-][0-9]{4}$"
BOOKING_ID_REGEX = r"^BOOK[a-zA-Z0-9]+$"

logger = logging.getLogger('validations')

def error_handling_input(func):
    """
        decorator for input validation and error handling during customer registration
    """
    def wrapper(*args, **kwargs):
        try:
            res = func(*args, **kwargs)
            if res == False:
                raise Exception
        except:
            logger.debug(LogConfig.invalid_input_exception_prompt)
            print(Config.invalid_input_prompt + "\n")
        finally:
            return res
    return wrapper
    
@error_handling_input
def input_validation(regular_exp, input_field) -> bool:
    """
        Function to validate input on basis of regex.
    """
    r = re.match(regular_exp, input_field) 
    if r != None:
        return True
    else:
        return False
    
class ParkingManagerInputValidation:
    """
        Class for validating parking related inputs.
    """
    @staticmethod
    def input_vehicle_type_name() -> str:
        """
            validation of vehicle_type name using regular expression
        """
        while True:
            type_name = input(Config.input_type_name_prompt).strip()
            check = input_validation(STRING_REGEX, type_name)
            if check:
                return type_name.title()

    @staticmethod
    def input_price_per_hour() -> float:
        """
            validation of price_per_hour
        """
        while True:
            try:
                price_per_hour = float(input(Config.input_price_prompt))
                return price_per_hour
            except Exception as e:
                logger.debug(e)
                print(Config.number_input_prompt.format("Price per hour") + "\n")

    @staticmethod
    def input_vehicle_type_id() -> str:
        """
            validation of vehicle_type id using regular expression
        """
        while True:
            type_id = input(Config.input_type_id_prompt).strip()
            check = input_validation(TYPE_ID_REGEX, type_id)
            if check:
                return type_id

    @staticmethod
    def input_parking_slot_number() -> str:
        """
            validation of parking_slot no using regular expression
        """
        while True:
            parking_slot_no = input(Config.input_parking_slot_number_prompt).strip()
            check = input_validation(PARKING_SLOT_NUMBER_REGEX, parking_slot_no)
            if check:
                return parking_slot_no.upper()

    @staticmethod
    def input_vehicle_number() -> str:
        """
            validation of vehicle no using regular expression
        """
        while True:
            print(Config.vehicle_number_foramt_prompt + "\n")
            vehicle_number = input(Config.vehicle_number_input_prompt).strip()
            check = input_validation(VEHICLE_NUMBER_REGEX, vehicle_number)
            if check:
                return vehicle_number

    @staticmethod
    def input_out_date() -> str:
        """
            validation of out_date using regular expression
        """
        while True:
            out_date = input(Config.customer_out_date_input_prompt).strip()
            present = datetime.now()
            try:
                out_date = datetime.strptime(out_date, "%d-%m-%Y")
                if out_date.date() < present.date():
                    print(Config.cannot_input_past_date + "\n")
                else:
                    return out_date.date().strftime("%d-%m-%Y")
            except ValueError:
                print(Config.invalid_input_prompt + "\n")
