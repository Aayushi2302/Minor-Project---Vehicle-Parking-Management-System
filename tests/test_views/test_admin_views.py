from unittest import TestCase
from unittest.mock import Mock, patch

from src.views.admin_views import AdminViews

class TestAdminViews(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.admin_views_obj = AdminViews()

    @patch('src.views.admin_views.AdminViews.admin_menu')
    def test_admin_menu_operations_positive(self, mock_admin_menu: Mock) -> bool:
        mock_admin_menu.return_value = True
        self.assertIsNone(self.admin_views_obj.admin_menu_operations())
        mock_admin_menu.assert_called_once()

    @patch('src.views.admin_views.AdminViews.admin_menu')
    def test_admin_menu_operations_negative(self, mock_admin_menu: Mock) -> bool:
        mock_admin_menu.side_effect = [False, False, True]
        self.assertIsNone(self.admin_views_obj.admin_menu_operations())
        self.assertEqual(mock_admin_menu.call_count, 3)

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

    def test_employee_updation_form(self):
        pass

    @patch('src.views.admin_views.AdminViews.manage_profile_menu')
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
        mock_input.side_effect = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        mock_case_6.side_effect = [False, True]
        mock_case_7.side_effect = [False, True]
        mock_case_8.side_effect = [False, True]
        mock_case_9.side_effect = [False, True]
        for _ in range(9):
            self.assertFalse(self.admin_views_obj.admin_menu())
        mock_case_1.assert_called_once()
        mock_case_2.assert_called_once()
        mock_case_3.assert_called_once()
        mock_case_4.assert_called_once()
        mock_case_5.assert_called_once()

    @patch('builtins.input')
    def test_admin_menu_positive(self, mock_input: Mock) -> bool:
        mock_input.return_value = '10'
        self.assertTrue(self.admin_views_obj.admin_menu())
        
    @patch('src.views.admin_views.CommonHelper.create_new_password')   
    @patch('src.views.admin_views.CommonHelper.view_individual_employee_details')   
    @patch('builtins.input')
    def test_manage_profile_menu_negative(self, mock_input: Mock, mock_case_1: Mock, mock_case_2: Mock) -> bool:
        mock_input.side_effect = ['1', '2']
        self.assertFalse(self.admin_views_obj.manage_profile_menu())
        self.assertFalse(self.admin_views_obj.manage_profile_menu())
        mock_case_1.assert_called_once()
        mock_case_2.assert_called_once()

    @patch('builtins.input')
    def test_manage_profile_menu_positive(self, mock_input: Mock) -> bool:
        mock_input.return_value = '3'
        self.assertTrue(self.admin_views_obj.manage_profile_menu)