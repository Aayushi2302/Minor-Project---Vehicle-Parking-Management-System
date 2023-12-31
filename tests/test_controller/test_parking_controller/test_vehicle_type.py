from unittest import TestCase
from unittest.mock import Mock, patch

from src.controller.parking_controller.vehicle_type import VehicleType

class TestVehicleType(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.vehicle_type_obj = VehicleType()
    
    @patch('src.controller.parking_controller.vehicle_type.db')
    def test_register_vehicle(self, mock_db: Mock) -> bool:
        mock_db.save_data_to_database.return_value = None
        self.assertIsNone(self.vehicle_type_obj.register_vehicle_type("TYPE1234", "CAR", 25.2))
        mock_db.save_data_to_database.assert_called_once()

    @patch('src.controller.parking_controller.vehicle_type.db')
    def test_get_vehicle_type_data_from_type_id(self, mock_db: Mock) -> bool:
        mock_db.fetch_data_from_database.return_value = 23.22
        self.assertEqual(self.vehicle_type_obj.get_vehicle_type_data_from_type_id("TYPE1234"), 23.22)
        mock_db.fetch_data_from_database.assert_called_once()
    
    @patch('src.controller.parking_controller.vehicle_type.db')
    def test_get_vehicle_type_id_from_type_name(self, mock_db: Mock) -> bool:
        mock_db.fetch_data_from_database.return_value = "TYPE1234"
        self.assertEqual(self.vehicle_type_obj.get_vehicle_type_id_from_type_name("car"), "TYPE1234")
        mock_db.fetch_data_from_database.assert_called_once()

    @patch('src.controller.parking_controller.vehicle_type.db')
    def test_update_vehicle_type_detail(self, mock_db: Mock) -> bool:
        mock_db.save_data_to_database.return_value = None
        self.assertIsNone(self.vehicle_type_obj.update_vehicle_type_detail(45.25, "price_per_hour", "TYPE1234"))
        mock_db.save_data_to_database.assert_called_once()

    @patch('src.controller.parking_controller.vehicle_type.db')
    def test_get_all_vehicle_type(self, mock_db: Mock) -> bool:
        mock_db.fetch_data_from_database.return_value = [("vehicle type data", )]
        self.assertEqual(self.vehicle_type_obj.get_all_vehicle_type(), [("vehicle type data", )])
        mock_db.fetch_data_from_database.assert_called_once()
        