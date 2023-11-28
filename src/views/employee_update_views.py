from config.app_config import AppConfig
from config.prompts.prompts import Prompts
from config.query import QueryConfig
from models.db_helper import DBHelper
from utils.error_handler import error_handler
from utils.input_validator.user_controller_validator import UserControllerValidator

# TODO : remove db_helper() method invokes from this module.

class EmployeeUpdateViews:
    """
        Class containing methods to update employee details.
        ...
        Attributes
        ----------
        db_helper_obj -> DBHelper
        emp_id -> str
        new_data -> str
        updated_field -> str

        Methods
        -------
        employee_update_operations() -> Method to update employee details.
        employee_update_menu() -> Method to manage employee update menu.
    """
    def __init__(self) -> None:
        self.db_helper_obj = DBHelper()
        self.updated_field = None
        self.new_data = None
        self.emp_id = None

    def employee_update_operations(self) -> None:
        """
            Method to perform employee update operations.
            Parameter -> self
            Return type -> None
        """
        print("\n" + Prompts.INPUT_DETAILS_FOR_UPDATION + "\n")
        emp_email = UserControllerValidator.input_email_address()
        data =  self.db_helper_obj.get_emp_id_status_and_role_from_email(emp_email)
        # data = admin_controller.AdminController.get_employee_data()
        if not data:
            print(Prompts.DETAILS_NOT_EXIST)
        else:
            self.emp_id = data[0][0]
            emp_status = data[0][1]
            role = data[0][2]
            if role is AppConfig.ADMIN_ROLE:
                print(Prompts.CANNOT_UPDATE_ADMIN + "\n")
            if emp_status is AppConfig.STATUS_INACTIVE:
                print(Prompts.UPDATE_DETAILS_FOR_INACTIVE_STATUS + "\n")
            else:
                while True:
                    if self.employee_update_menu():
                        break
                    if self.updated_field in (AppConfig.ROLE_ATTR, AppConfig.USERNAME_ATTR):
                        query = QueryConfig.UPDATE_EMPLOYEE_CREDENTIAL_FROM_EMP_ID.format(self.updated_field)
                    else:
                        query = QueryConfig.UPDATE_EMPLOYEE_DETAIL_FROM_EMP_ID.format(self.updated_field)
                    self.db_helper_obj.update_employee_details(query, self.new_data, self.emp_id)
                    print(Prompts.EMPLOYEE_UPDATION_SUCCESSFUL + "\n")

    @error_handler
    def employee_update_menu(self) -> bool:
        """
            Method to manage employee update menu.
            Parameter -> self
            Return type -> bool
        """
        print(Prompts.EMPLOYEE_DETAIL_UPDATE_MENU)
        choice = input(Prompts.ENTER_CHOICE)
        match choice :
            case '1':
                print(Prompts.NEW_DETAIL_INPUT.format("Name"))
                self.new_data = UserControllerValidator.input_name()
                self.updated_field = AppConfig.NAME_ATTR
            case '2':
                print(Prompts.NEW_DETAIL_INPUT.format("Age"))
                self.new_data = UserControllerValidator.input_age()
                self.updated_field = AppConfig.AGE_ATTR
            case '3':
                print(Prompts.NEW_DETAIL_INPUT.format("Gender"))
                self.new_data = UserControllerValidator.input_gender()
                self.updated_field = AppConfig.GENDER_ATTR
            case '4':
                print(Prompts.NEW_DETAIL_INPUT.format("Mobile No."))
                self.new_data = UserControllerValidator.input_mobile_number()
                self.updated_field = AppConfig.MOBILE_NO_ATTR
            case '5':
                print(Prompts.NEW_DETAIL_INPUT.format("Email Address"))
                self.new_data = UserControllerValidator.input_email_address()
                self.updated_field = AppConfig.EMAIL_ADDRESS_ATTR
            case '6':
                print(Prompts.NEW_DETAIL_INPUT.format("Username"))
                self.new_data = UserControllerValidator.input_username()
                self.updated_field = AppConfig.USERNAME_ATTR
            case '7':
                print(Prompts.NEW_DETAIL_INPUT.format("Role"))
                self.new_data = UserControllerValidator.input_role()
                self.updated_field = AppConfig.ROLE_ATTR
            case '8':
                return True
            case _:
                print(Prompts.INVALID_INPUT)
        return False
