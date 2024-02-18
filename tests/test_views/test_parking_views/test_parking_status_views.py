from unittest import TestCase
from unittest.mock import Mock, patch

from views.parking_views.parking_status_views import ParkingStatusViews

class TestParkingStatusViews(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.parking_status_views_obj = ParkingStatusViews()

    @patch('views.parking_views.parking_status_views.ParkingStatus.get_current_date_status')
    def test_view_current_date_status_positive(self, mock_get_curr_date_status: Mock) -> bool:
        mock_get_curr_date_status.return_value = [("data", )]
        self.assertIsNone(self.parking_status_views_obj.view_current_date_status())

    @patch('views.parking_views.parking_status_views.ParkingStatus.get_current_date_status')
    def test_view_current_date_status_negative(self, mock_get_curr_date_status: Mock) -> bool:
        mock_get_curr_date_status.return_value = []
        self.assertIsNone(self.parking_status_views_obj.view_current_date_status())

    @patch('views.parking_views.parking_status_views.ParkingStatus.get_current_year_status')
    def test_view_current_year_status_positive(self, mock_get_curr_year_status: Mock) -> bool:
        mock_get_curr_year_status.return_value = [("data", )]
        self.assertIsNone(self.parking_status_views_obj.view_current_year_status())

    @patch('views.parking_views.parking_status_views.ParkingStatus.get_current_year_status')
    def test_view_current_year_status_negative(self, mock_get_curr_year_status: Mock) -> bool:
        mock_get_curr_year_status.return_value = []
        self.assertIsNone(self.parking_status_views_obj.view_current_year_status())

    @patch('views.parking_views.parking_status_views.SlotBookingViews.view_booking_details')
    @patch('views.parking_views.parking_status_views.ParkingStatusViews.view_current_year_status')
    @patch('views.parking_views.parking_status_views.ParkingStatusViews.view_current_date_status')
    @patch('builtins.input')
    def test_parking_status_menu_negative(self, mock_input: Mock, mock_curr_date_status: Mock, mock_curr_year_status: Mock, mock_view_booking_details: Mock) -> bool:
        mock_input.side_effect = ['1', '2', '3', 'default', '4']
        mock_curr_date_status.return_value = None
        mock_curr_year_status.return_value = None
        mock_view_booking_details.return_value = None
        self.assertTrue(self.parking_status_views_obj.parking_status_menu())
        mock_curr_date_status.assert_called_once()
        mock_curr_year_status.assert_called_once()
        mock_view_booking_details.assert_called_once()

    @patch('builtins.input')
    def test_parking_status_menu_positive(self, mock_input: Mock) -> bool:
        mock_input.return_value = '4'
        self.assertTrue(self.parking_status_views_obj.parking_status_menu())
