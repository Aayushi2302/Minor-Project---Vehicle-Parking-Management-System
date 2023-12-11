from unittest import TestCase
from unittest.mock import Mock, patch

from src.controller.parking_controller.parking_status import ParkingStatus
class TestParkingStatus(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.parking_status_obj = ParkingStatus()

    @patch('src.controller.parking_controller.parking_status.db')
    def test_get_current_date_status(self, mock_db: Mock) -> None:
        mock_db.fetch_data_from_database.return_value = [("curr date booking data", )]
        self.assertEqual(self.parking_status_obj.get_current_date_status(), [("curr date booking data", )])
        mock_db.fetch_data_from_database.assert_called_once()

    @patch('src.controller.parking_controller.parking_status.db')
    def test_get_current_year_status(self, mock_db: Mock) -> None:
       mock_db.fetch_data_from_database.return_value = [("curr year booking data", )]
       self.assertEqual(self.parking_status_obj.get_current_year_status(), [("curr year booking data", )])
       mock_db.fetch_data_from_database.assert_called_once()

