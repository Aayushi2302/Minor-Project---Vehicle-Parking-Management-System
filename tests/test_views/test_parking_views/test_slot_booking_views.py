from unittest import TestCase
from unittest.mock import Mock, patch

from src.views.parking_views.slot_booking_views import SlotBookingViews

class TestSlotBooking(TestCase):
    @classmethod
    def setUpClass(self) -> None:
        self.slot_booking_views_obj = SlotBookingViews()

    @patch('src.views.parking_views.slot_booking_views.SlotBooking.save_booking_details')
    @patch('src.views.parking_views.slot_booking_views.SlotBooking.get_vacant_parking_slot')
    @patch('src.views.parking_views.slot_booking_views.CommonHelper.get_current_date_and_time')
    @patch('src.views.parking_views.slot_booking_views.ParkingControllerValidator.input_out_date')
    @patch('src.views.parking_views.slot_booking_views.EmployeeController.get_cust_id_from_vehicle_no')
    @patch('src.views.parking_views.slot_booking_views.ParkingControllerValidator.input_vehicle_number')
    @patch('src.views.parking_views.slot_booking_views.shortuuid.ShortUUID.random')
    def test_book_parking_slot_positive(self, mock_shortuuid: Mock, mock_input_vehicle_no: Mock, mock_get_cust_id: Mock, mock_input_out_date: Mock, mock_get_curr_date_time: Mock, mock_get_vacant_parking_slot: Mock, mock_save_booking_details: Mock) -> bool:
        mock_shortuuid.return_value = "1234"
        mock_input_vehicle_no.return_value = "UP-12-AB-1987"
        mock_get_cust_id.return_value = [("CUST1234", "TYPE1234")]
        mock_input_out_date.return_value = "12-12-2023"
        mock_get_curr_date_time.return_value = ("12-12-2023", "09:54")
        mock_get_vacant_parking_slot.return_value = "PSN001"
        mock_save_booking_details.return_value = None
        self.assertIsNone(self.slot_booking_views_obj.book_parking_slot())
        slot_booking_data = ("BOOK1234", "CUST1234", "PSN001", "12-12-2023", "09:54", "12-12-2023")
        parking_slot_data = ("booked", "PSN001")
        mock_save_booking_details.assert_called_once_with(slot_booking_data, parking_slot_data)

    @patch('src.views.parking_views.slot_booking_views.EmployeeController.get_cust_id_from_vehicle_no')
    @patch('src.views.parking_views.slot_booking_views.ParkingControllerValidator.input_vehicle_number')
    @patch('src.views.parking_views.slot_booking_views.shortuuid.ShortUUID.random')
    def test_book_parking_slot_negative(self, mock_shortuuid: Mock, mock_input_vehicle_no: Mock, mock_get_cust_id: Mock) -> bool:
        mock_shortuuid.return_value = "1234"
        mock_input_vehicle_no.return_value = "UP-12-AB-1987"
        mock_get_cust_id.return_value = []
        self.assertIsNone(self.slot_booking_views_obj.book_parking_slot())

    @patch('src.views.parking_views.slot_booking_views.SlotBooking.get_booking_details')
    def test_view_booking_details_positive(self, mock_get_booking_details: Mock) -> bool:
        mock_get_booking_details.return_value = [("data", )]
        self.assertIsNone(self.slot_booking_views_obj.view_booking_details())
    
    @patch('src.views.parking_views.slot_booking_views.SlotBooking.get_booking_details')
    def test_view_booking_details_negative(self, mock_get_booking_details: Mock) -> bool:
        mock_get_booking_details.return_value = []
        self.assertIsNone(self.slot_booking_views_obj.view_booking_details())

    @patch('src.views.parking_views.slot_booking_views.SlotBooking.save_vacating_details')
    @patch('src.views.parking_views.slot_booking_views.SlotBooking.calculate_charges')
    @patch('src.views.parking_views.slot_booking_views.SlotBooking.calculate_hours_spent_in_parking')
    @patch('src.views.parking_views.slot_booking_views.CommonHelper.get_current_date_and_time')
    @patch('src.views.parking_views.slot_booking_views.SlotBooking.get_details_for_vacating_parking_slot')
    @patch('src.views.parking_views.slot_booking_views.ParkingControllerValidator.input_vehicle_number')
    @patch('src.views.parking_views.slot_booking_views.SlotBooking.get_booking_details')
    def test_vacate_parking_slot_positive(self, mock_get_booking_details: Mock, mock_input_vehicle_no: Mock, mock_get_details_for_vacating: Mock, mock_get_curr_date_time: Mock, mock_calc_hours: Mock, mock_calc_charges: Mock, mock_save_vacating_details: Mock) -> bool:
        mock_get_booking_details.return_value = [("data", )]
        mock_input_vehicle_no.return_value = "UP-12-AB-1987"
        mock_get_details_for_vacating.side_effect = [[("BOOK1234", "PSN001", "12-12-2023", "09:54", "XX:XX")], [("BOOK1234", "PSN001", "12-12-2023", "09:54", "10:15")]]
        mock_get_curr_date_time.return_value = ("12-12-2023", "10:54")
        mock_calc_hours.return_value = 1
        mock_calc_charges.return_value = 15.23
        slot_booking_data = ("12-12-2023", "10:54", 1, 15.23, "BOOK1234")
        parking_slot_data = ("vacant", "PSN001")
        mock_save_vacating_details.return_value = None
        self.assertIsNone(self.slot_booking_views_obj.vacate_parking_slot())
        self.assertIsNone(self.slot_booking_views_obj.vacate_parking_slot())
        mock_save_vacating_details.assert_called_once_with(slot_booking_data, parking_slot_data)

    @patch('src.views.parking_views.slot_booking_views.SlotBooking.get_details_for_vacating_parking_slot')
    @patch('src.views.parking_views.slot_booking_views.ParkingControllerValidator.input_vehicle_number')
    @patch('src.views.parking_views.slot_booking_views.SlotBooking.get_booking_details')
    def test_vacate_parking_slot_negative(self, mock_get_booking_details: Mock, mock_input_vehicle_no: Mock, mock_get_details_for_vacating: Mock) -> bool:
        mock_get_booking_details.side_effect = [[],[("data", )]]
        mock_input_vehicle_no.return_value = "UP-12-AB-1987"
        mock_get_details_for_vacating.return_value = []
        self.assertIsNone(self.slot_booking_views_obj.vacate_parking_slot())
        self.assertIsNone(self.slot_booking_views_obj.vacate_parking_slot())
        