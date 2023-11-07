"""
    Module for loading menu_promts from yaml.
"""
import yaml

FILE_PATH = "src\\config\\menu\\menu_prompts.yaml"

class MenuConfig:
    """
        Class for loading menu_promts from yaml.
    """
    @classmethod
    def load(cls):
        with open(FILE_PATH, 'r') as file:
            data = yaml.safe_load(file)
            
        cls.admin_menu_prompt = data["admin_menu"]
        cls.employee_detail_update_menu_prompt = data["employee_detail_update_menu"]
        cls.vehicle_type_manage_menu_prompt = data["vehicle_type_manage_menu"]
        cls.parking_slot_manage_menu_prompt = data["parking_slot_manage_menu"]
        cls.employee_menu_prompt = data["employee_menu"]
        cls.view_parking_status_menu_prompt = data["view_parking_status_menu"]
        cls.customer_detail_update_menu_prompt = data["customer_detail_update_menu"]