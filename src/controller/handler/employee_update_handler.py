"""
    Module for maintaing menu for updating employee details.
"""
import logging

from config.statements.config import Config
from config.menu.menu_prompts_config import MenuConfig
from config.query.query_config import QueryConfig
from database.query_executor import QueryExecutor
from utils.validator.user_input_validation import UserInputValidation

logger = logging.getLogger('employee_update_handler')

@staticmethod
def employee_details_update_menu() -> None:
    """
        Method for updating employee details.
    """
    print("\n" + Config.input_details_for_updation_prompt + "\n")
    emp_email = UserInputValidation.input_email_address()
    data =  QueryExecutor.fetch_data_from_database(
                QueryConfig.query_for_fetching_emp_id_and_status_from_email,
                (emp_email, )
            )
    if not any(data):
        print(Config.user_not_exist_prompt.format(emp_email))
        return
    emp_id = data[0][0]
    emp_status = data[0][1]
    if emp_status == "inactive":
        print(Config.updating_details_for_inactive_status_prompt + "\n")
    else:
        while True:
            print(MenuConfig.employee_detail_update_menu_prompt)
            try:
                choice = int(input(Config.enter_choice_prompt))
                match choice :
                    case 1:
                        print(Config.new_detail_input_prompt.format("Name"))
                        new_data = UserInputValidation.input_name()
                        updated_field = "name"
                    case 2:
                        print(Config.new_detail_input_prompt.format("Age"))
                        new_data = UserInputValidation.input_age()
                        updated_field = "age"
                    case 3:
                        print(Config.new_detail_input_prompt.format("Gender"))
                        new_data = UserInputValidation.input_gender()
                        updated_field = "gender"
                    case 4:
                        print(Config.new_detail_input_prompt.format("Mobile No."))
                        new_data = UserInputValidation.input_mobile_number()
                        updated_field = "mobile_no"
                    case 5:
                        print(Config.new_detail_input_prompt.format("Email Address"))
                        new_data = UserInputValidation.input_email_address()
                        updated_field = "email_address"
                    case 6:
                        print(Config.new_detail_input_prompt.format("Username"))
                        new_data = UserInputValidation.input_username()
                        updated_field = "username"
                    case 7:
                        print(Config.new_detail_input_prompt.format("Role"))
                        new_data = UserInputValidation.input_role()
                        updated_field = "role"
                    case 8: 
                        break
                    case _:
                        print(Config.invalid_input_prompt)
                if updated_field in ("role", "username"):
                    query = QueryConfig.query_for_updating_employee_credential_from_emp_id.format(updated_field)
                else:
                    query = QueryConfig.query_for_updating_employee_detail_from_emp_id.format(updated_field)

                QueryExecutor.save_data_in_database(
                    query,
                    (new_data, emp_id),
                    Config.employee_updation_successful_prompt + "\n"
                )
            except ValueError:
                logger.debug(ValueError)
                print(Config.invalid_input_prompt + "\n")