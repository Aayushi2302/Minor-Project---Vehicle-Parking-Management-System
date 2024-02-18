from unittest import TestCase
from unittest.mock import Mock, patch

from controller.admin_controller import AdminController

class TestAdminController(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.admin_controller_obj = AdminController()

    @patch('controller.admin_controller.db')
    def test_register_employee(self, mock_db: Mock) -> None:
        mock_db.save_data_to_database.return_value = None
        self.assertIsNone(self.admin_controller_obj.register_employee(
            ("EMPadb12","user@aayushi", "SDK1312", "admin"), 
            ("EMPadb12", "Aayushi Sharma", 22, "Female", "9874563258", "sharmaaayushi2302@gmail.com")
        ))
        mock_db.save_data_to_database.assert_called_once()

    @patch('controller.admin_controller.db')
    @patch('controller.admin_controller.AdminController.get_employee_data')
    def test_update_employee_details_positive(self, mock_get_employee_data: Mock, mock_db: Mock) -> None:
        mock_get_employee_data.return_value = [("EMP123", "active", "attendant")]
        mock_db.save_data_to_database.return_value = None
        self.assertEqual(self.admin_controller_obj.update_employee_details(
            "demo@gmail.com",
            "role",
            "admin"
        ), 1)
        self.assertEqual(self.admin_controller_obj.update_employee_details(
            "demo@gmail.com",
            "name",
            "admin"
        ), 1)

    @patch('controller.admin_controller.AdminController.get_employee_data')
    def test_update_employee_details_negative(self, mock_get_employee_data: Mock) -> None:
        mock_get_employee_data.side_effect = [[], [("EMP123", "active", "admin")], [("EMP123", "inactive", "attendant")]]
        self.assertEqual(self.admin_controller_obj.update_employee_details(
            "demo@gmail.com",
            "role",
            "admin"
        ), -1)
        self.assertEqual(self.admin_controller_obj.update_employee_details(
            "demo@gmail.com",
            "role",
            "admin"
        ), -2)
        self.assertEqual(self.admin_controller_obj.update_employee_details(
            "demo@gmail.com",
            "role",
            "admin"
        ), -3)

    @patch('controller.admin_controller.db')
    def test_get_all_employees(self, mock_db: Mock) -> None:
        mock_db.fetch_data_from_database.return_value = [("employee data", )]
        self.assertEqual(
            self.admin_controller_obj.get_all_employees(),
            [("employee data", )]
        )
        mock_db.fetch_data_from_database.assert_called_once()

    @patch('controller.admin_controller.db')
    def test_get_default_password_for_employees_positive(self, mock_db: Mock) -> None:
        mock_db.fetch_data_from_database.side_effect = [[("EMP1234", )], [("sJF#512j", )]]
        self.assertEqual(self.admin_controller_obj.get_default_password_for_employee("demo@gmail.com"), [("sJF#512j", )])

    @patch('controller.admin_controller.db')
    def test_get_default_password_for_employees_negative(self, mock_db: Mock) -> None:
        mock_db.fetch_data_from_database.return_value = []
        self.assertEqual(self.admin_controller_obj.get_default_password_for_employee("demo1@gmail.com"), [])
    
    @patch('controller.admin_controller.db')
    def test_get_employee_data(self, mock_db: Mock) -> None:
        mock_db.fetch_data_from_database.return_value = [("EMP1234", "active", "admin")]
        self.assertEqual(self.admin_controller_obj.get_employee_data("demo@gmail.com"), [("EMP1234", "active", "admin")])
        mock_db.fetch_data_from_database.assert_called_once()
    
    @patch('controller.admin_controller.db')
    @patch('controller.admin_controller.AdminController.get_employee_data')
    def test_remove_employee_positive(self, mock_get_employee_data: Mock, mock_db: Mock) -> None:
        mock_get_employee_data.return_value = [("EMP123", "active", "attendant")]
        mock_db.save_data_to_database.return_value = None
        self.assertEqual(self.admin_controller_obj.remove_employee(
            "demo@gmail.com",
            "status",
            "inactive"
        ), 2)
        mock_db.save_data_to_database.assert_called_once()

    @patch('controller.admin_controller.AdminController.get_employee_data')
    def test_remove_employee_negative(self, mock_get_employee_data: Mock) -> None:
        mock_get_employee_data.side_effect = [[],[("EMP123", "active", "admin")], [("EMP123", "inactive", "attendant")]]
        self.assertEqual(self.admin_controller_obj.remove_employee(
            "demo@gmail.com",
            "status",
            "inactive"
        ), -1)
        self.assertEqual(self.admin_controller_obj.remove_employee(
            "demo@gmail.com",
            "status",
            "inactive"
        ), 0)
        self.assertEqual(self.admin_controller_obj.remove_employee(
            "demo@gmail.com",
            "status",
            "inactive"
        ), 1)
