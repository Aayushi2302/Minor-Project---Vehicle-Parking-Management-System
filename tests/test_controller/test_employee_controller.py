from unittest import TestCase
from unittest.mock import Mock, patch

from src.controller.employee_controller import EmployeeController

class TestEmployeeController(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.employee_controller_obj = EmployeeController()

    @patch('src.controller.employee_controller.db')
    def test_register_customer(self, mock_db: Mock) -> None:
        mock_db.save_data_to_database.return_value = None
        self.assertIsNone(self.employee_controller_obj.register_customer((
            "CUST1234",
            "Dev Nathan",
            "7863254175",
            "UP-12-AB-1876",
            "TYPE3256"
        )))
        mock_db.save_data_to_database.assert_called_once()
    
    @patch('src.controller.employee_controller.db')
    def test_get_cust_id_from_vehicle_no(self, mock_db: Mock) -> None:
        mock_db.fetch_data_from_database.return_value = [("CUST1234", "TYPE1234")]
        self.assertEqual(self.employee_controller_obj.get_cust_id_from_vehicle_no("UP-12-AB-1876"), [("CUST1234", "TYPE1234")])
        mock_db.fetch_data_from_database.assert_called_once()

    @patch('src.controller.employee_controller.db')
    def test_get_customer_details(self, mock_db: Mock) -> None:
        mock_db.fetch_data_from_database.return_value = [("customer data", )]
        self.assertEqual(self.employee_controller_obj.get_customer_details(), [("customer data", )])
        mock_db.fetch_data_from_database.assert_called_once()

    @patch('src.controller.employee_controller.db')
    @patch('src.controller.employee_controller.EmployeeController.get_cust_id_from_vehicle_no')
    def test_update_customer_personal_details_positive(self, mock_get_func: Mock, mock_db: Mock) -> None:
        mock_get_func.return_value = [("CUST123")]
        mock_db.save_data_to_database.return_value = None
        self.assertEqual(self.employee_controller_obj.update_customer_details(
            "UP-12-AB-1976",
            "name",
            "Dev Sinha"
        ), 2)
        mock_db.save_data_to_database.assert_called_once()
    
    @patch('src.controller.employee_controller.EmployeeController.get_cust_id_from_vehicle_no')
    def test_update_customer_personal_details_negative(self, mock_get_func: Mock) -> None:
        mock_get_func.return_value = []
        self.assertEqual(self.employee_controller_obj.update_customer_details(
            "UP-12-AB-1976",
            "name",
            "Dev Sinha"
        ), -1)

    @patch('src.controller.employee_controller.db')
    @patch('src.controller.employee_controller.EmployeeController.get_booking_details_from_cust_id')
    @patch('src.controller.employee_controller.EmployeeController.get_cust_id_from_vehicle_no')
    def test_update_slot_booking_details_positive(self, mock_get_func: Mock, mock_get_booking_details: Mock, mock_db: Mock) -> None:
        mock_get_func.return_value = [("CUST123")]
        mock_get_booking_details.side_effect = [[("BOOK123", "XX:XX")], [("BOOK123", "16-01-2024")]]
        mock_db.save_data_to_database.return_value = None
        self.assertEqual(self.employee_controller_obj.update_customer_details(
            "UP-12-AB-1976",
            "out_date",
            "17-01-2024"
        ), 2)
        self.assertEqual(self.employee_controller_obj.update_customer_details(
            "UP-12-AB-1976",
            "out_date",
            "17-01-2024"
        ), 1)
        mock_db.save_data_to_database.assert_called_once()

    @patch('src.controller.employee_controller.EmployeeController.get_booking_details_from_cust_id')
    @patch('src.controller.employee_controller.EmployeeController.get_cust_id_from_vehicle_no')
    def test_update_slot_booking_details_negative(self, mock_get_func: Mock, mock_get_booking_details: Mock) -> None:
        mock_get_func.return_value = [("CUST123")]
        mock_get_booking_details.return_value = []
        self.assertEqual(self.employee_controller_obj.update_customer_details(
            "UP-12-AB-1976",
            "out_date",
            "17-01-2024"
        ), 0)

    @patch('src.controller.employee_controller.db')
    def test_get_booking_details_from_cust_id(self, mock_db: Mock) -> None:
        mock_db.fetch_data_from_database.return_value = [("booking detail", )]
        self.assertEqual(self.employee_controller_obj.get_booking_details_from_cust_id("CUST1234"), [("booking detail", )])
        mock_db.fetch_data_from_database.assert_called_once()
