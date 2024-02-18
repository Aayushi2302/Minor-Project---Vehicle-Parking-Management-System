from unittest import TestCase
from unittest.mock import Mock, patch

from views.parking_views.slot_booking_views import SlotBookingViews

class TestSlotBooking(TestCase):
    @classmethod
    def setUpClass(self) -> None:
        self.slot_booking_views_obj = SlotBookingViews()

    @patch('views.parking_views.slot_booking_views.SlotBooking.save_booking_details')
    @patch('views.parking_views.slot_booking_views.SlotBooking.get_vacant_parking_slot')
    @patch('views.parking_views.slot_booking_views.CommonHelper.get_current_date_and_time')
    @patch('views.parking_views.slot_booking_views.ParkingControllerValidator.input_out_date')
    @patch('views.parking_views.slot_booking_views.ParkingControllerValidator.input_vehicle_number')
    @patch('views.parking_views.slot_booking_views.shortuuid.ShortUUID.random')
    def test_book_parking_slot_positive(self, mock_shortuuid: Mock, mock_input_vehicle_no: Mock, mock_input_out_date: Mock, mock_get_curr_date_time: Mock, mock_get_vacant_parking_slot: Mock, mock_save_booking_details: Mock) -> None:
        mock_shortuuid.return_value = "1234"
        mock_input_vehicle_no.return_value = "UP-12-AB-1987"
        mock_input_out_date.return_value = "12-12-2023"
        mock_get_curr_date_time.return_value = ("12-12-2023", "09:54")
        mock_get_vacant_parking_slot.return_value = "PSN001"
        mock_save_booking_details.return_value = True
        self.assertIsNone(self.slot_booking_views_obj.book_parking_slot())
       
    @patch('views.parking_views.slot_booking_views.SlotBooking.save_booking_details')
    @patch('views.parking_views.slot_booking_views.SlotBooking.get_vacant_parking_slot')
    @patch('views.parking_views.slot_booking_views.CommonHelper.get_current_date_and_time')
    @patch('views.parking_views.slot_booking_views.ParkingControllerValidator.input_out_date')
    @patch('views.parking_views.slot_booking_views.ParkingControllerValidator.input_vehicle_number')
    @patch('views.parking_views.slot_booking_views.shortuuid.ShortUUID.random')
    def test_book_parking_slot_negative(self, mock_shortuuid: Mock, mock_input_vehicle_no: Mock, mock_input_out_date: Mock, mock_get_curr_date_time: Mock, mock_get_vacant_parking_slot: Mock, mock_save_booking_details: Mock) -> None:
        mock_shortuuid.return_value = "1234"
        mock_input_vehicle_no.return_value = "UP-12-AB-1987"
        mock_input_out_date.return_value = "12-12-2023"
        mock_get_curr_date_time.return_value = ("12-12-2023", "09:54")
        mock_get_vacant_parking_slot.return_value = "PSN001"
        mock_save_booking_details.return_value = False
        self.assertIsNone(self.slot_booking_views_obj.book_parking_slot())

    @patch('views.parking_views.slot_booking_views.SlotBooking.get_booking_details')
    def test_view_booking_details_positive(self, mock_get_booking_details: Mock) -> None:
        mock_get_booking_details.return_value = [("data", )]
        self.assertIsNone(self.slot_booking_views_obj.view_booking_details())
    
    @patch('views.parking_views.slot_booking_views.SlotBooking.get_booking_details')
    def test_view_booking_details_negative(self, mock_get_booking_details: Mock) -> None:
        mock_get_booking_details.return_value = []
        self.assertIsNone(self.slot_booking_views_obj.view_booking_details())

    @patch('views.parking_views.slot_booking_views.SlotBooking.save_vacating_details')
    @patch('views.parking_views.slot_booking_views.SlotBooking.calculate_charges')
    @patch('views.parking_views.slot_booking_views.SlotBooking.calculate_hours_spent_in_parking')
    @patch('views.parking_views.slot_booking_views.CommonHelper.get_current_date_and_time')
    @patch('views.parking_views.slot_booking_views.ParkingControllerValidator.input_vehicle_number')
    @patch('views.parking_views.slot_booking_views.SlotBookingViews.view_booking_details')
    @patch('views.parking_views.slot_booking_views.SlotBooking.get_booking_details')
    def test_vacate_parking_slot_positive(self, mock_get_booking_details: Mock, mock_view_booking: Mock, mock_input_vehicle_no: Mock, mock_get_curr_date_time: Mock, mock_calc_hours: Mock, mock_calc_charges: Mock, mock_save_vacating_details: Mock) -> None:
        mock_get_booking_details.return_value = [("data", )]
        mock_view_booking.return_value = None
        mock_input_vehicle_no.return_value = "UP-12-AB-1987"
        mock_get_curr_date_time.return_value = ("12-12-2023", "10:54")
        mock_save_vacating_details.return_value = (45, 1)
        self.assertIsNone(self.slot_booking_views_obj.vacate_parking_slot())
    
    @patch('views.parking_views.slot_booking_views.SlotBooking.save_vacating_details')
    @patch('views.parking_views.slot_booking_views.SlotBooking.calculate_charges')
    @patch('views.parking_views.slot_booking_views.SlotBooking.calculate_hours_spent_in_parking')
    @patch('views.parking_views.slot_booking_views.CommonHelper.get_current_date_and_time')
    @patch('views.parking_views.slot_booking_views.ParkingControllerValidator.input_vehicle_number')
    @patch('views.parking_views.slot_booking_views.SlotBookingViews.view_booking_details')
    @patch('views.parking_views.slot_booking_views.SlotBooking.get_booking_details')
    def test_vacate_parking_slot_negative(self, mock_get_booking_details: Mock, mock_view_booking: Mock, mock_input_vehicle_no: Mock, mock_get_curr_date_time: Mock, mock_calc_hours: Mock, mock_calc_charges: Mock, mock_save_vacating_details: Mock) -> None:
        mock_get_booking_details.return_value = [[],[("data", )]]
        mock_view_booking.return_value = None
        mock_input_vehicle_no.return_value = "UP-12-AB-1987"
        mock_get_curr_date_time.return_value = ("12-12-2023", "10:54")
        mock_save_vacating_details.side_effect = [(-1, ), (0, )]
        self.assertIsNone(self.slot_booking_views_obj.vacate_parking_slot())
        self.assertIsNone(self.slot_booking_views_obj.vacate_parking_slot())
        