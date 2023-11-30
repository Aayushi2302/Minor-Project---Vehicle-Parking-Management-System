from unittest import TestCase
from unittest.mock import Mock, patch
from src.controller.auth_controller import AuthController

class TestAuthController(TestCase):
    @classmethod
    @patch('src.controller.auth_controller.DBHelper')
    def setUpClass(cls, mock_cls: Mock)-> bool:
        cls.db_helper_obj = mock_cls()
        cls.auth_controller_obj = AuthController()

    @patch('src.controller.auth_controller.CommonHelper.create_new_password')
    def test_first_login_positive(self, mock_obj):
        mock_obj.return_value = True
        self.assertTrue(self.auth_controller_obj.valid_first_login("user", "hello", "hello"))
    
    def test_valid_first_login_negative(self):
        self.assertFalse(self.auth_controller_obj.valid_first_login("user","hello", "hey"))

    @patch('src.controller.auth_controller.EmployeeViews')
    @patch('src.controller.auth_controller.AdminViews')
    def test_role_based_access_positive(self, mock_admin_views, mock_employee_views):
        role_type = iter(["admin", "attendant"])
        mock_admin_views().admin_menu_operations.return_value = True
        mock_employee_views().employee_menu_operations.return_value = True
        self.assertTrue(self.auth_controller_obj.role_based_access(next(role_type), "admin"))
        self.assertTrue(self.auth_controller_obj.role_based_access(next(role_type), "attendant"))

    def test_role_based_access_negative(self):
        self.assertFalse(self.auth_controller_obj.role_based_access("random", "random"))

    # @patch('src.controller.auth_controller.AuthController.role_based_access')
    # @patch('src.controller.auth_controller.AuthController.valid_first_login')
    # def authenticate_user_positive(self, mock_valid_first_login, mock_role_based_access):
    #     self.db_helper_obj.get_employee_credentails.side_effect = [("admin@123", "admin", "default"), ("Aayushi@123", "attendant", "permanent")]
    #     mock_valid_first_login.

