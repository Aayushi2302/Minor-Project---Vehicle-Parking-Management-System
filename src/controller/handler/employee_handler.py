"""
    Module for handling employee menu related logic and user interactions.
"""
import logging

from config.statements.config import Config
from config.menu.menu_prompts_config import MenuConfig
from controller.employee_controller import EmployeeController
from parking_manager.parking_charges import ParkingCharges
from utils.common import Common

logger = logging.getLogger('employee_handler')

class EmployeeHandler(ParkingCharges):
    """
        Class for performing employee menu related interactions.
    """
    @staticmethod
    def employee_menu() -> int:
        """
            Method to handle employee menu.
        """
        employee_obj = EmployeeController()
        common_obj = Common()
        while True:
            print("\n" + MenuConfig.employee_menu_prompt)
            try:
                choice = int(input(Config.enter_choice_prompt))
                match choice:
                    case 1:
                        employee_obj.register_customer()
                    case 2:
                        employee_obj.update_customer_details()
                    case 3:
                        employee_obj.view_customer_details()
                    case 4:
                        employee_obj.view_parking_slot_details()
                    case 5:
                        employee_obj.book_parking_slot()
                    case 6:
                        employee_obj.vacate_parking_slot()
                    case 7:
                        employee_obj.view_booking_details()
                    case 8:
                        EmployeeHandler.view_parking_charges_for_vehicle_type()
                    case 9:
                        common_obj.view_emp_details()
                    case 10:
                        print(Config.successful_logout_prompt + "\n")
                        return Config.maximum_login_attempts
                    case _ :
                        print(Config.invalid_input_prompt)
            except ValueError:
                logger.debug(ValueError)
                print(Config.invalid_input_prompt + "\n")