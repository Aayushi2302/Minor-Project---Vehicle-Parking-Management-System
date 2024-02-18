from datetime import datetime
from unittest import TestCase
from unittest.mock import Mock, patch

from controller.parking_controller.slot_booking import SlotBooking

class TestSlotBooking(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.slot_booking_obj = SlotBooking()

    @patch('controller.parking_controller.slot_booking.random.randrange')
    @patch('controller.parking_controller.slot_booking.db')
    def test_get_vacant_parking_slot(self, mock_db: Mock, mock_random: Mock) -> None:
        mock_db.fetch_data_from_database.return_value = [("PSN001", ), ("PSN002", ), ("PSN005", )]
        mock_random.return_value = 1
        self.assertEqual(self.slot_booking_obj.get_vacant_parking_slot("TYPE1234"), "PSN002")
        mock_db.fetch_data_from_database.assert_called_once()

    @patch('controller.parking_controller.slot_booking.db')
    @patch("controller.parking_controller.slot_booking.SlotBooking.get_vacant_parking_slot")
    @patch('controller.parking_controller.slot_booking.EmployeeController.get_cust_id_from_vehicle_no')
    def test_save_booking_details_positive(self, mock_get_cust_id: Mock, mock_get_vacant_parking_slot: Mock, mock_db: Mock) -> None:
        mock_get_cust_id.return_value = [("CUST123", "TYPE123")]
        mock_get_vacant_parking_slot.return_value = [("PSN001", )]
        mock_db.save_data_to_database.return_value = None
        self.assertEqual(self.slot_booking_obj.save_booking_details(
            "BOOK123",
            "UP-12-AB-1987",
            "16-01-2024",
            "10:40",
            "17-01-2024"
        ), [("PSN001", )])
        mock_db.save_data_to_database.assert_called_once()

    @patch('controller.parking_controller.slot_booking.EmployeeController.get_cust_id_from_vehicle_no')
    def test_save_booking_details_negative(self, mock_get_cust_id: Mock) -> None:
        mock_get_cust_id.return_value = []
        self.assertEqual(self.slot_booking_obj.save_booking_details(
            "BOOK123",
            "UP-12-AB-1987",
            "16-01-2024",
            "10:40",
            "17-01-2024"
        ), "")

    @patch('controller.parking_controller.slot_booking.db')
    def test_get_booking_details(self, mock_db: Mock) -> None:
        mock_db.fetch_data_from_database.return_value = [("slot booking details", )]
        self.assertEqual(self.slot_booking_obj.get_booking_details(), [("slot booking details", )])
        mock_db.fetch_data_from_database.assert_called_once()

    @patch('controller.parking_controller.slot_booking.db')
    def test_get_details_for_vacating_parking_slot(self, mock_db: Mock) -> None:
        mock_db.fetch_data_from_database.return_value = [("booking data", )]
        self.assertEqual(self.slot_booking_obj.get_details_for_vacating_parking_slot("UP-12-AB-1846"), [("booking data", )])
        mock_db.fetch_data_from_database.assert_called_once()

    @patch('controller.parking_controller.slot_booking.datetime')
    def test_calculate_hours_spent_in_parking(self, mock_datetime: Mock) -> None:
        mock_datetime.strptime.return_value = datetime.strptime("11-12-2023 12:54", "%d-%m-%Y %H:%M")
        self.assertAlmostEqual(self.slot_booking_obj.calculate_hours_spent_in_parking("in_date", "in_time", "out_date", "out_time"), 0)

    @patch('controller.parking_controller.slot_booking.db')
    def test_calculate_charges(self, mock_db: Mock) -> None:
        mock_db.fetch_data_from_database.side_effect = [[("TYPE1234", )], [(25.22, )]]
        hours_spent = 5.26  
        ans = round((hours_spent * 25.22), 2)
        self.assertAlmostEqual(self.slot_booking_obj.calculate_charges(hours_spent, "BOOK12345"), ans)

    @patch('controller.parking_controller.slot_booking.db')
    @patch('controller.parking_controller.slot_booking.SlotBooking.calculate_charges')
    @patch('controller.parking_controller.slot_booking.SlotBooking.calculate_hours_spent_in_parking')
    @patch('controller.parking_controller.slot_booking.SlotBooking.get_details_for_vacating_parking_slot')
    def test_save_vacating_details_positive(self, mock_get_vacanting_details: Mock, mock_calculate_hours: Mock, mock_calculate_charges: Mock, mock_db: Mock) -> None:
        mock_get_vacanting_details.return_value = [("BOOK123", "PSN001", "16-01-2024", "10:00", "XX:XX")]
        mock_calculate_hours.return_value = 1.5
        mock_calculate_charges.return_value = 65.34
        mock_db.save_data_to_database.return_value = None
        self.assertEqual(self.slot_booking_obj.save_vacating_details("UP-12-AB-1987", "16-01-2024", "11:45"), (65.34, 1.5))
        mock_db.save_data_to_database.assert_called_once()

    @patch('controller.parking_controller.slot_booking.SlotBooking.get_details_for_vacating_parking_slot')
    def test_save_vacating_details_negative(self, mock_get_vacanting_details: Mock) -> None:
        mock_get_vacanting_details.side_effect = [[], [("BOOK123", "PSN001", "16-01-2024", "10:00", "11:00")]]
        self.assertEqual(self.slot_booking_obj.save_vacating_details("UP-12-AB-1987", "16-01-2024", "11:45"), (-1, ))
        self.assertEqual(self.slot_booking_obj.save_vacating_details("UP-12-AB-1987", "16-01-2024", "11:45"), (0, ))
