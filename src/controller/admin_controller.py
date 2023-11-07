"""
    Module for maintaining all the methods or functionalities of Admin.
"""
import random
import string
import shortuuid

from config.statements.config import Config
from config.query.query_config import QueryConfig
from controller.handler.employee_update_handler import employee_details_update_menu
from database.query_executor import QueryExecutor
from parking_manager.parking_slots import ParkingSlot
from parking_manager.vehicle_type import VehicleType
from utils.common import Common
from utils.validator.user_input_validation import UserInputValidation

class AdminController(VehicleType, ParkingSlot):
    """
        Class contains all the functionalities that user can perform on Employee.
        Also this class inherits VehicleType and ParkingSlot class to implement further admin functionalities.
    """
    def register_employee(self) -> None:
        """
            Method to register employee and save their data to database.
        """
        print(Config.input_employee_details_prompt + "\n")
        emp_id = "EMP" + shortuuid.ShortUUID().random(length = 5)
        emp_name = UserInputValidation.input_name()
        emp_username = UserInputValidation.input_username()
        data =  QueryExecutor.fetch_data_from_database(
                    QueryConfig.query_for_fetching_emp_id_from_username,
                    (emp_username, )
                )
        if any(data):
            print(Config.user_already_exist_prompt.format(emp_username) + "\n")
        else:
            characters = string.ascii_letters + string.digits + "@#$&%"
            emp_password = ''.join(random.choice(characters) for _ in range(8))
            emp_age = UserInputValidation.input_age()
            emp_gender = UserInputValidation.input_gender()
            emp_role = UserInputValidation.input_role()
            emp_mobile_number = UserInputValidation.input_mobile_number()
            emp_email_address = UserInputValidation.input_email_address()
            data =  QueryExecutor.fetch_data_from_database(
                        QueryConfig.query_for_fetching_emp_id_and_status_from_email,
                        (emp_email_address, )
                    )
            if any(data):
                print(Config.user_already_exist_prompt.format(emp_email_address) + "\n")
            else:
                QueryExecutor.save_data_in_database(
                    QueryConfig.query_for_creating_employee_credentials,
                    (emp_id, emp_username, emp_password, emp_role),
                    ""
                )
                QueryExecutor.save_data_in_database(
                    QueryConfig.query_for_creating_employee_details,
                    (emp_id, emp_name, emp_age, emp_gender, emp_mobile_number, emp_email_address),
                    Config.employee_registration_successful_prompt + "\n"
                )

    def update_employee_details(self) -> None:
        """
            Method to update employee details.
        """
        self.view_employee_details()
        employee_details_update_menu()
                          
    def view_employee_details(self) -> None:
        """
            Method to display employee details.
        """
        data =  QueryExecutor.fetch_data_from_database(
                    QueryConfig.query_for_viewing_employee_detail
                )
        if not any(data):
            print(Config.zero_record_prompt.format("employee"))
        else:
            common_obj = Common()
            headers = QueryConfig.employee_detail_header
            common_obj.display_table(data, headers)

    def view_default_password_for_employee(self) -> None:
        """
            Method to display default password of employee to admin.
        """
        emp_email = UserInputValidation.input_email_address()
        emp_id = QueryExecutor.fetch_data_from_database(
                    QueryConfig.query_for_fetching_emp_id_and_status_from_email,
                    (emp_email, )
                )
        if not emp_id:
            print(Config.details_does_not_exist_prompt.format(emp_email) + "\n")
        else:
            emp_id = emp_id[0][0]
            data =  QueryExecutor.fetch_data_from_database(
                        QueryConfig.query_for_fetching_default_password_from_emp_id,
                        (emp_id, )
                    )
            password_type = data[0][0]
            default_password = data[0][1]
            if password_type == "permanent":
                print(Config.no_default_password_prompt + "\n")
            else:
                print(Config.print_default_password_prompt.format(default_password) + "\n")

    def remove_employee(self) -> None:
        """
            Method to remove or inactivate the employee.
        """
        self.view_employee_details()
        print("\n" + Config.input_details_for_removal_prompt + "\n")
        emp_email = UserInputValidation.input_email_address()
        data =  QueryExecutor.fetch_data_from_database(
                    QueryConfig.query_for_fetching_emp_id_and_status_from_email,
                    (emp_email, )
                )
        if not any(data):
            print(Config.details_does_not_exist_prompt.format(emp_email) + "\n")
            return
        emp_id = data[0][0]
        status = data[0][1]
        if status == "inactive":
            print(Config.updating_details_for_inactive_status_prompt)
        else:
            query = QueryConfig.query_for_updating_employee_detail_from_emp_id.format("status")
            QueryExecutor.save_data_in_database(
                query,
                ("inactive", emp_id ),
                Config.employee_removal_successful_prompt + "\n"
            )