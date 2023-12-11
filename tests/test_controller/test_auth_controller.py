from unittest import TestCase
from unittest.mock import Mock, patch
from src.controller.auth_controller import AuthController

class TestAuthController(TestCase):
    @classmethod
    def setUpClass(cls)-> bool:
        cls.auth_controller_obj = AuthController()

    @patch('src.controller.auth_controller.CommonHelper.create_new_password')
    def test_valid_first_login_positive(self, mock_method: Mock):
        mock_method.return_value = True
        self.assertTrue(self.auth_controller_obj.valid_first_login("user", "hello", "hello"))
    
    def test_valid_first_login_negative(self):
        self.assertFalse(self.auth_controller_obj.valid_first_login("user","hello", "hey"))

    @patch('src.controller.auth_controller.EmployeeViews')
    @patch('src.controller.auth_controller.AdminViews')
    def test_role_based_access_positive(self, mock_admin_views: Mock, mock_employee_views: Mock):
        role_type = iter(["admin", "attendant"])
        mock_admin_views().admin_menu_operations.return_value = True
        mock_employee_views().employee_menu_operations.return_value = True
        self.assertTrue(self.auth_controller_obj.role_based_access(next(role_type), "admin"))
        self.assertTrue(self.auth_controller_obj.role_based_access(next(role_type), "attendant"))

    def test_role_based_access_negative(self):
        self.assertFalse(self.auth_controller_obj.role_based_access("random", "random"))

    @patch('src.controller.auth_controller.AuthController.role_based_access')
    @patch('src.controller.auth_controller.hashlib.sha256')
    @patch('src.controller.auth_controller.AuthController.valid_first_login')
    @patch('src.controller.auth_controller.db')
    def test_authenticate_user_positive(self, mock_db: Mock, mock_valid_first_login: Mock, mock_hashlib: Mock, mock_role_based_access: Mock):
        mock_db.fetch_data_from_database.side_effect = [[("admin@123", "admin", "default")], [("Aayushi@123", "attendant", "permanent")]]
        mock_hashlib().hexdigest.return_value = "Aayushi@123"
        mock_valid_first_login.return_value = True
        mock_role_based_access.return_value = True
        self.assertTrue(self.auth_controller_obj.authenticate_user("user@admin", "admin"))
        self.assertTrue(self.auth_controller_obj.authenticate_user("user@admin", "Aayushi@123"))

    @patch('src.controller.auth_controller.db')
    @patch('src.controller.auth_controller.hashlib.sha256')
    def test_authenticate_user_negative(self, mock_db: Mock, mock_hashlib: Mock):
        mock_db.fetch_data_from_database.side_effect = [[], [("admin@123", "admin", "default")]]
        mock_hashlib().hexdigest.return_value = "admin123"
        self.assertFalse(self.auth_controller_obj.authenticate_user("user@admin", "admin"))
        self.assertFalse(self.auth_controller_obj.authenticate_user("user@admin", "Aayushi@123"))
