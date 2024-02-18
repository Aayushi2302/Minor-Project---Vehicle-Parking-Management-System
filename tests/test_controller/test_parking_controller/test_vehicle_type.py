from unittest import TestCase
from unittest.mock import Mock, patch

from controller.parking_controller.vehicle_type import VehicleType

class TestVehicleType(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.vehicle_type_obj = VehicleType()
    
    @patch('controller.parking_controller.vehicle_type.db')
    def test_register_vehicle(self, mock_db: Mock) -> None:
        mock_db.save_data_to_database.return_value = None
        self.assertIsNone(self.vehicle_type_obj.register_vehicle_type("TYPE1234", "CAR", 25.2))
        mock_db.save_data_to_database.assert_called_once()

    @patch('controller.parking_controller.vehicle_type.db')
    def test_get_vehicle_type_data_from_type_id(self, mock_db: Mock) -> None:
        mock_db.fetch_data_from_database.return_value = 23.22
        self.assertEqual(self.vehicle_type_obj.get_vehicle_type_data_from_type_id("TYPE1234"), 23.22)
        mock_db.fetch_data_from_database.assert_called_once()
    
    @patch('controller.parking_controller.vehicle_type.db')
    def test_get_vehicle_type_id_from_type_name(self, mock_db: Mock) -> None:
        mock_db.fetch_data_from_database.return_value = "TYPE1234"
        self.assertEqual(self.vehicle_type_obj.get_vehicle_type_id_from_type_name("car"), "TYPE1234")
        mock_db.fetch_data_from_database.assert_called_once()

    @patch('controller.parking_controller.vehicle_type.db')
    @patch('controller.parking_controller.vehicle_type.VehicleType.get_vehicle_type_data_from_type_id')
    def test_update_vehicle_type_detail_positive(self, mock_get_type_data: Mock, mock_db: Mock) -> None:
        mock_get_type_data.return_value = [("vehicle type data")]
        mock_db.save_data_to_database.return_value = None
        self.assertTrue(self.vehicle_type_obj.update_vehicle_type_detail("TYPE1234", "price_per_hour", 45.25))
        mock_db.save_data_to_database.assert_called_once()

    @patch('controller.parking_controller.vehicle_type.VehicleType.get_vehicle_type_data_from_type_id')
    def test_update_vehicle_type_detail_negative(self, mock_get_type_data: Mock) -> None:
        mock_get_type_data.return_value = []
        self.assertFalse(self.vehicle_type_obj.update_vehicle_type_detail("TYPE1234", "price_per_hour", 45.25))

    @patch('controller.parking_controller.vehicle_type.db')
    def test_get_all_vehicle_type(self, mock_db: Mock) -> None:
        mock_db.fetch_data_from_database.return_value = [("vehicle type data", )]
        self.assertEqual(self.vehicle_type_obj.get_all_vehicle_type(), [("vehicle type data", )])
        mock_db.fetch_data_from_database.assert_called_once()
        