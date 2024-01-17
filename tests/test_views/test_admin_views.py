from unittest import TestCase
from unittest.mock import Mock, patch

from src.views.admin_views import AdminViews

class TestAdminViews(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.admin_views_obj = AdminViews()

    @patch('src.views.admin_views.random.choice')
    @patch('src.views.admin_views.AdminController.register_employee')
    @patch('src.views.admin_views.shortuuid.ShortUUID.random')
    @patch('src.views.admin_views.UserControllerValidator')
    def test_employee_registration_form(self, mock_user_validator: Mock, mock_shortuuid: Mock, mock_register_employee: Mock, mock_password: Mock) -> bool:
        mock_shortuuid.return_value = "1234"
        mock_password.return_value = "a"
        mock_user_validator.input_name.return_value = "Aayushi"
        mock_user_validator.input_username.return_value = "user@aayushi"
        mock_user_validator.input_age.return_value = 25
        mock_user_validator.input_gender.return_value = "Female"
        mock_user_validator.input_role.return_value = "admin"
        mock_user_validator.input_mobile_number.return_value = "9687456325"
        mock_user_validator.input_email_address.return_value = "sharmaaayushi2302@gmail.com"

        auth_data = ("EMP1234", "user@aayushi", "aaaaaaaa", "admin")
        employee_data = ("EMP1234", "Aayushi", 25, "Female", "9687456325", "sharmaaayushi2302@gmail.com")

        self.assertIsNone(self.admin_views_obj.employee_registration_form())
        mock_register_employee.assert_called_once_with(auth_data, employee_data)


    @patch('src.views.admin_views.AdminController.get_all_employees')
    def test_view_employee_details_positive(self, mock_get_all_employees: Mock) -> bool:
        mock_get_all_employees.return_value = [("data", )]
        self.admin_views_obj.view_employee_details()

    @patch('src.views.admin_views.AdminController.get_all_employees')
    def test_view_employee_details_negative(self, mock_get_all_employees: Mock) -> bool:
        mock_get_all_employees.return_value = []
        self.admin_views_obj.view_employee_details()

    # @patch('src.views.admin_views.AdminController.update_employee_details')
    # @patch('src.views.admin_views.AdminViews.employee_update_menu')
    # @patch('src.views.admin_views.AdminController.get_employee_data')
    # @patch('src.views.admin_views.UserControllerValidator.input_email_address')
    # @patch('src.views.admin_views.AdminViews.view_employee_details')
    # @patch('src.views.admin_views.AdminController.get_all_employees')
    # def test_employee_updation_form_positive(self, mock_get_all_emp: Mock, mock_view_emp_details: Mock, mock_input_email: Mock, mock_get_emp_data: Mock, mock_emp_update_menu: Mock, mock_update_emp_details: Mock) -> bool:
    #     mock_get_all_emp.return_value = [("employee data", )]
    #     mock_view_emp_details.return_value = None
    #     mock_input_email.return_value = "demo@gmail.com"
    #     mock_get_emp_data.side_effect = [[("EMP1234", "active", "attendant")], [("EMP1234", "active", "admin")], [("EMP1234", "inactive", "attendant")]]
    #     mock_emp_update_menu.side_effect = [False, True]
    #     mock_update_emp_details.return_value = None
    #     self.admin_views_obj.updated_field = "random"
    #     self.admin_views_obj.new_data = "updated"
    #     self.assertIsNone(self.admin_views_obj.employee_updation_form())
    #     self.assertIsNone(self.admin_views_obj.employee_updation_form())
    #     self.assertIsNone(self.admin_views_obj.employee_updation_form())
    #     mock_update_emp_details.assert_called_once_with("random", "updated", "EMP1234")

    @patch('src.views.admin_views.AdminController.get_employee_data')
    @patch('src.views.admin_views.UserControllerValidator.input_email_address')
    @patch('src.views.admin_views.AdminViews.view_employee_details')
    @patch('src.views.admin_views.AdminController.get_all_employees')
    def test_employee_updation_form_negative(self, mock_get_all_emp: Mock, mock_view_emp_details: Mock, mock_input_email: Mock, mock_get_emp_data: Mock) -> bool:
        mock_get_all_emp.side_effect = [[], [("employee data", )]]
        mock_view_emp_details.return_value = None
        mock_input_email.return_value = "demo@gmail.com"
        mock_get_emp_data.return_value = []
        self.assertIsNone(self.admin_views_obj.employee_updation_form())
        self.assertIsNone(self.admin_views_obj.employee_updation_form())

    @patch('src.views.admin_views.AdminController.get_default_password_for_employee')
    @patch('src.views.admin_views.UserControllerValidator.input_email_address')
    @patch('src.views.admin_views.AdminViews.view_employee_details')
    @patch('src.views.admin_views.AdminController.get_all_employees')
    def test_view_default_password_positive(self, mock_get_all_emp: Mock, mock_view_emp_details: Mock, mock_input_email: Mock, mock_get_default_password: Mock) -> bool:
        mock_get_all_emp.return_value = [("employee data", )]
        mock_view_emp_details.return_value = None
        mock_input_email.return_value = "demo@gmail.com"
        mock_get_default_password.side_effect = [[("default", "random_pass")], [("permanent", "random_pass")]]
        self.assertIsNone(self.admin_views_obj.view_default_password())
        self.assertIsNone(self.admin_views_obj.view_default_password())

    @patch('src.views.admin_views.AdminController.get_default_password_for_employee')
    @patch('src.views.admin_views.UserControllerValidator.input_email_address')
    @patch('src.views.admin_views.AdminViews.view_employee_details')
    @patch('src.views.admin_views.AdminController.get_all_employees')
    def test_view_default_password_negative(self, mock_get_all_emp: Mock, mock_view_emp_details: Mock, mock_input_email: Mock, mock_get_default_password: Mock) -> bool:
        mock_get_all_emp.side_effect = [[], [("employee data", )]]
        mock_view_emp_details.return_value = None
        mock_input_email.return_value = "demo@gmail.com"
        mock_get_default_password.return_value = []
        self.assertIsNone(self.admin_views_obj.view_default_password())
        self.assertIsNone(self.admin_views_obj.view_default_password())

    # @patch('src.views.admin_views.AdminController.remove_employee')
    # @patch('src.views.admin_views.AdminController.get_employee_data')
    # @patch('src.views.admin_views.UserControllerValidator.input_email_address')
    # @patch('src.views.admin_views.AdminViews.view_employee_details')
    # @patch('src.views.admin_views.AdminController.get_all_employees')
    # def test_employee_removal_form_positive(self, mock_get_all_emp: Mock, mock_view_emp_details: Mock, mock_input_email: Mock, mock_get_emp_data: Mock, mock_remove_emp: Mock) -> bool:
    #     mock_get_all_emp.return_value = [("employee data", )]
    #     mock_view_emp_details.return_value = None
    #     mock_input_email.return_value = "demo@gmail.com"
    #     mock_get_emp_data.side_effect = [[("EMP1234", "active", "attendant")], [("EMP1234", "active", "admin")], [("EMP1234", "inactive", "attendant")]]
    #     mock_remove_emp.return_value = None
    #     self.assertIsNone(self.admin_views_obj.employee_removal_form())
    #     self.assertIsNone(self.admin_views_obj.employee_removal_form())
    #     self.assertIsNone(self.admin_views_obj.employee_removal_form())
    #     mock_remove_emp.assert_called_once_with("status", "inactive", "EMP1234")

    @patch('src.views.admin_views.AdminController.get_employee_data')
    @patch('src.views.admin_views.UserControllerValidator.input_email_address')
    @patch('src.views.admin_views.AdminViews.view_employee_details')
    @patch('src.views.admin_views.AdminController.get_all_employees')
    def test_employee_removal_form_negative(self, mock_get_all_emp: Mock, mock_view_emp_details: Mock, mock_input_email: Mock, mock_get_emp_data: Mock) -> bool:
        mock_get_all_emp.side_effect = [[], [("employee data", )]]
        mock_view_emp_details.return_value = None
        mock_input_email.return_value = "demo@gmail.com"
        mock_get_emp_data.return_value = []
        self.assertIsNone(self.admin_views_obj.employee_removal_form())
        self.assertIsNone(self.admin_views_obj.employee_removal_form())

    @patch('src.views.admin_views.EmployeeViews.manage_profile_menu')
    @patch('src.views.admin_views.ParkingStatusViews.parking_status_menu')
    @patch('src.views.admin_views.ParkingSlotViews.parking_slot_menu')
    @patch('src.views.admin_views.VehicleTypeViews.vehicle_type_menu')
    @patch('src.views.admin_views.AdminViews.employee_removal_form')
    @patch('src.views.admin_views.AdminViews.view_default_password')
    @patch('src.views.admin_views.AdminViews.view_employee_details')
    @patch('src.views.admin_views.AdminViews.employee_updation_form')
    @patch('src.views.admin_views.AdminViews.employee_registration_form')
    @patch('builtins.input')
    def test_admin_menu_negative(self, mock_input: Mock, mock_case_1: Mock, mock_case_2: Mock, mock_case_3: Mock, mock_case_4: Mock, mock_case_5: Mock, mock_case_6: Mock, mock_case_7: Mock, mock_case_8: Mock, mock_case_9: Mock) -> bool:
        mock_input.side_effect = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'default', '10']
        mock_case_1.return_value = None
        mock_case_2.return_value = None
        mock_case_3.return_value = None
        mock_case_4.return_value = None
        mock_case_5.return_value = None
        mock_case_6.return_value = None
        mock_case_7.return_value = None
        mock_case_8.return_value = None
        mock_case_9.return_value = None
        self.assertTrue(self.admin_views_obj.admin_menu())
        mock_case_1.assert_called_once()
        mock_case_2.assert_called_once()
        mock_case_3.assert_called_once()
        mock_case_4.assert_called_once()
        mock_case_5.assert_called_once()
        mock_case_6.assert_called_once()
        mock_case_7.assert_called_once()
        mock_case_8.assert_called_once()
        mock_case_9.assert_called_once()

    @patch('builtins.input')
    def test_admin_menu_positive(self, mock_input: Mock) -> bool:
        mock_input.return_value = '10'
        self.assertTrue(self.admin_views_obj.admin_menu())
