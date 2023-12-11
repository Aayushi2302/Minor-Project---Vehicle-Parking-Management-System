from datetime import datetime
from unittest import TestCase
from unittest.mock import Mock, patch

from src.controller.parking_controller.slot_booking import SlotBooking

class TestSlotBooking(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.slot_booking_obj = SlotBooking()

    @patch('src.controller.parking_controller.slot_booking.random.randrange')
    @patch('src.controller.parking_controller.slot_booking.db')
    def test_get_vacant_parking_slot(self, mock_db: Mock, mock_random: Mock) -> bool:
        mock_db.fetch_data_from_database.return_value = [("PSN001", ), ("PSN002", ), ("PSN005", )]
        mock_random.return_value = 1
        self.assertEqual(self.slot_booking_obj.get_vacant_parking_slot("TYPE1234"), "PSN002")
        mock_db.fetch_data_from_database.assert_called_once()

    @patch('src.controller.parking_controller.slot_booking.db')
    def test_save_booking_details(self, mock_db: Mock) -> bool:
        mock_db.save_data_to_database.return_value = None
        self.assertIsNone(self.slot_booking_obj.save_booking_details(("slot booking data"), ("parking slot data")))
        mock_db.save_data_to_database.assert_called_once()

    @patch('src.controller.parking_controller.slot_booking.db')
    def test_get_booking_details(self, mock_db: Mock) -> bool:
        mock_db.fetch_data_from_database.return_value = [("slot booking details", )]
        self.assertEqual(self.slot_booking_obj.get_booking_details(), [("slot booking details", )])
        mock_db.fetch_data_from_database.assert_called_once()

    @patch('src.controller.parking_controller.slot_booking.db')
    def test_get_details_for_vacating_parking_slot(self, mock_db: Mock) -> bool:
        mock_db.fetch_data_from_database.return_value = [("booking data", )]
        self.assertEqual(self.slot_booking_obj.get_details_for_vacating_parking_slot("UP-12-AB-1846"), [("booking data", )])
        mock_db.fetch_data_from_database.assert_called_once()

    @patch('src.controller.parking_controller.slot_booking.datetime')
    def test_calculate_hours_spent_in_parking(self, mock_datetime: Mock) -> bool:
        mock_datetime.strptime.return_value = datetime.strptime("11-12-2023 12:54", "%d-%m-%Y %H:%M")
        self.assertAlmostEqual(self.slot_booking_obj.calculate_hours_spent_in_parking("in_date", "in_time", "out_date", "out_time"), 0)

    @patch('src.controller.parking_controller.slot_booking.db')
    def test_calculate_charges(self, mock_db: Mock) -> bool:
        mock_db.fetch_data_from_database.side_effect = [[("TYPE1234", )], [(25.22, )]]
        hours_spent = 5.26  
        ans = round((hours_spent * 25.22), 2)
        self.assertAlmostEqual(self.slot_booking_obj.calculate_charges(hours_spent, "BOOK12345"), ans)

    @patch('src.controller.parking_controller.slot_booking.db')
    def test_save_vacating_details(self, mock_db: Mock) -> bool:
        mock_db.save_data_to_database.return_value = None
        self.assertIsNone(self.slot_booking_obj.save_vacating_details(("slot booking data"), ("parking slot data")))
        mock_db.save_data_to_database.assert_called_once()
        