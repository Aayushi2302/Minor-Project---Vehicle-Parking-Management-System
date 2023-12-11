from unittest import TestCase
from unittest.mock import Mock, patch

from src.controller.admin_controller import AdminController

class TestAdminController(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.admin_controller_obj = AdminController()

    @patch('src.controller.admin_controller.db')
    def test_register_employee(self, mock_db: Mock) -> None:
        mock_db.save_data_to_database.return_value = None
        self.assertIsNone(self.admin_controller_obj.register_employee(
            ("EMPadb12","user@aayushi", "SDK1312", "admin"), 
            ("EMPadb12", "Aayushi Sharma", 22, "Female", "9874563258", "sharmaaayushi2302@gmail.com")
        ))
        mock_db.save_data_to_database.assert_called_once()

    @patch('src.controller.admin_controller.db')
    def test_update_employee_details_auth_table(self, mock_db: Mock) -> None:
        mock_db.save_data_to_database.return_value = None
        self.assertIsNone(self.admin_controller_obj.update_employee_details(
            "role",
            "attendant",
            "EMP1234"
        ))
        mock_db.save_data_to_database.assert_called_once()
    
    @patch('src.controller.admin_controller.db')
    def test_update_employee_details_employee_table(self, mock_db: Mock) -> None:
        mock_db.save_data_to_database.return_value = None
        self.assertIsNone(self.admin_controller_obj.update_employee_details(
            "name",
            "Aditya Soni",
            "EMP1234"
        ))
        mock_db.save_data_to_database.assert_called_once()

    @patch('src.controller.admin_controller.db')
    def test_get_all_employees(self, mock_db: Mock):
        mock_db.fetch_data_from_database.return_value = [("employee data", )]
        self.assertEqual(
            self.admin_controller_obj.get_all_employees(),
            [("employee data", )]
        )
        mock_db.fetch_data_from_database.assert_called_once()

    @patch('src.controller.admin_controller.db')
    def test_get_default_password_for_employees_positive(self, mock_db: Mock) -> None:
        mock_db.fetch_data_from_database.side_effect = [[("EMP1234", )], [("sJF#512j", )]]
        self.assertEqual(self.admin_controller_obj.get_default_password_for_employee("demo@gmail.com"), [("sJF#512j", )])

    @patch('src.controller.admin_controller.db')
    def test_get_default_password_for_employees_negative(self, mock_db: Mock) -> None:
        mock_db.fetch_data_from_database.return_value = []
        self.assertEqual(self.admin_controller_obj.get_default_password_for_employee("demo1@gmail.com"), [])
    
    @patch('src.controller.admin_controller.db')
    def test_get_employee_data(self, mock_db: Mock) -> None:
        mock_db.fetch_data_from_database.return_value = [("EMP1234", "active", "admin")]
        self.assertEqual(self.admin_controller_obj.get_employee_data("demo@gmail.com"), [("EMP1234", "active", "admin")])
        mock_db.fetch_data_from_database.assert_called_once()
    
    @patch('src.controller.admin_controller.db')
    def test_remove_employee(self, mock_db: Mock) -> None:
        mock_db.save_data_to_database.return_value = None
        self.assertIsNone(self.admin_controller_obj.remove_employee(
            "status",
            "inactive",
            "EMP1234"
        ))
        mock_db.save_data_to_database.assert_called_once()
