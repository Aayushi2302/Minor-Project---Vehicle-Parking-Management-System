from unittest import TestCase
from unittest.mock import Mock, patch

from src.controller.parking_controller.parking_slot import ParkingSlot
class TestParkingSlot(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.parking_slot_obj = ParkingSlot()

    @patch('src.controller.parking_controller.parking_slot.db')
    @patch('src.controller.parking_controller.parking_slot.VehicleType.get_vehicle_type_id_from_type_name')
    def test_register_parking_slot_positive(self, mock_get_vehicle_type_id: Mock, mock_db: Mock) -> None:
        mock_get_vehicle_type_id.return_value = [("TYPE123")]
        mock_db.save_data_to_database.return_value = None
        self.assertTrue(self.parking_slot_obj.register_parking_slot("PSN001", "Car"))
        mock_db.save_data_to_database.assert_called_once()

    @patch('src.controller.parking_controller.parking_slot.VehicleType.get_vehicle_type_id_from_type_name')
    def test_register_parking_slot_negative(self, mock_get_vehicle_type_id: Mock) -> None:
        mock_get_vehicle_type_id.return_value = []
        self.assertFalse(self.parking_slot_obj.register_parking_slot("PSN001", "Car"))

    @patch('src.controller.parking_controller.parking_slot.db')
    def test_get_parking_slot_status(self, mock_db: None) -> None:
        mock_db.fetch_data_from_database.return_value = [("vacant", )]
        self.assertEqual(self.parking_slot_obj.get_parking_slot_status("PSN002"), [("vacant", )])
        mock_db.fetch_data_from_database.assert_called_once()

    @patch('src.controller.parking_controller.parking_slot.db')
    def test_get_all_parking_slots(self, mock_db: Mock) -> None:
        mock_db.fetch_data_from_database.return_value = [("parking slot data", )]
        self.assertEqual(self.parking_slot_obj.get_all_parking_slots(), [("parking slot data", )])
        mock_db.fetch_data_from_database.assert_called_once()

    @patch('src.controller.parking_controller.parking_slot.db')
    @patch('src.controller.parking_controller.parking_slot.ParkingSlot.get_parking_slot_status')
    def test_update_parking_slot_status_positive(self, mock_get_parking_slot_status: Mock, mock_db: Mock) -> None:
        mock_get_parking_slot_status.return_value = [("vacant", )]
        mock_db.save_data_to_database.return_value = None
        self.assertEqual(self.parking_slot_obj.update_parking_slot_status("PSN001", "status", "inactive"), 1)
        mock_db.save_data_to_database.assert_called_once()

    @patch('src.controller.parking_controller.parking_slot.ParkingSlot.get_parking_slot_status')
    def test_update_parking_slot_status_negative(self, mock_get_parking_slot_status: Mock) -> None:
        mock_get_parking_slot_status.side_effect = [[], [("vacant", )]]
        self.assertEqual(self.parking_slot_obj.update_parking_slot_status("PSN001", "status", "inactive"), -1)
        self.assertEqual(self.parking_slot_obj.update_parking_slot_status("PSN001", "status", "vacant"), 0)
    