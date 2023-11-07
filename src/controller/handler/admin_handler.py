"""
    Module for handling admin menu related logic and user interactions.
"""
import logging

from config.statements.config import Config
from config.menu.menu_prompts_config import MenuConfig
from controller.admin_controller import AdminController
from parking_manager.parking_status import ParkingStatus
from utils.common import Common

logger = logging.getLogger('admin_handler')

class AdminHandler(ParkingStatus):
    """
        Class for performing admin menu related interactions.
    """
    @staticmethod
    def admin_menu() -> int:
        """
            Method to handle admin menu.
        """
        admin_obj = AdminController()
        common_obj = Common()
        while True:
            print("\n" + MenuConfig.admin_menu_prompt)
            try:
                choice = int(input(Config.enter_choice_prompt))           
                match choice:
                    case 1:
                        admin_obj.register_employee()
                    case 2:
                        admin_obj.update_employee_details()
                    case 3:
                        admin_obj.view_employee_details()
                    case 4:
                        admin_obj.view_default_password_for_employee()
                    case 5:
                        admin_obj.remove_employee()
                    case 6 :
                        while True:
                            print("\n" + MenuConfig.vehicle_type_manage_menu_prompt)
                            try:
                                vehicle_type_choice = int(input(Config.enter_choice_prompt))
                                match vehicle_type_choice:
                                    case 1:
                                        admin_obj.register_vehicle_type()
                                    case 2:
                                        admin_obj.update_vehicle_price_per_hour()
                                    case 3:
                                        admin_obj.view_vehicle_type()
                                    case 4 :
                                        break
                                    case _ :
                                        print(Config.invalid_input_prompt)
                            except ValueError:
                                logger.debug(ValueError)
                                print(Config.invalid_input_prompt + "\n")
                    case 7 :
                        while True:
                            print("\n" + MenuConfig.parking_slot_manage_menu_prompt)
                            try:
                                parking_slot_choice = int(input(Config.enter_choice_prompt))
                                match parking_slot_choice:
                                    case 1:
                                        admin_obj.register_or_activate_parking_slot()
                                    case 2:
                                        admin_obj.deactivate_parking_slot()
                                    case 3:
                                        admin_obj.view_parking_slot()
                                    case 4:
                                        admin_obj.remove_parking_slot()
                                    case 5 :
                                        break
                                    case _ :
                                        print(Config.invalid_input_prompt)
                            except ValueError:
                                logger.debug(ValueError)
                                print(Config.invalid_input_prompt + "\n")
                    case 8 :
                        while True:
                            print("\n" + MenuConfig.view_parking_status_menu_prompt + "\n")
                            try:
                                see_status_choice = int(input(Config.enter_choice_prompt))
                                match see_status_choice:
                                    case 1:
                                        AdminHandler.view_current_date_status()
                                    case 2:
                                        AdminHandler.view_current_year_status()
                                    case 3:
                                        AdminHandler.view_total_vehicle_entries()
                                    case 4:
                                        break
                                    case _ :
                                        print(Config.invalid_input_prompt)
                            except ValueError:
                                logger.debug(ValueError)
                                print(Config.invalid_input_prompt + "\n")
                    case 9 : 
                        common_obj.view_emp_details()
                    case 10 : 
                        print(Config.successful_logout_prompt + "\n")
                        return Config.maximum_login_attempts
                    case _ :
                        print(Config.invalid_input_prompt)
            except ValueError:
                logger.debug(ValueError)
                print(Config.invalid_input_prompt + "\n")