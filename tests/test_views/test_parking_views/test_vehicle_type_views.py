from unittest import TestCase
from unittest.mock import Mock, patch

from src.views.parking_views.vehicle_type_views import VehicleTypeViews

class TestVehicleTypeViews(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.vehicle_type_views_obj = VehicleTypeViews()

    @patch('src.views.parking_views.vehicle_type_views.VehicleTypeViews.view_vehicle_type')
    @patch('src.views.parking_views.vehicle_type_views.VehicleTypeViews.vehicle_type_update_form')
    @patch('src.views.parking_views.vehicle_type_views.VehicleTypeViews.vehicle_type_registration_form')
    @patch('builtins.input')
    def test_vehicle_type_menu_negative(self, mock_input: Mock, mock_case_1: Mock, mock_case_2: Mock, mock_case_3: Mock) -> bool:
        mock_input.side_effect = ['1', '2', '3']
        self.assertFalse(self.vehicle_type_views_obj.vehicle_type_menu())
        self.assertFalse(self.vehicle_type_views_obj.vehicle_type_menu())
        self.assertFalse(self.vehicle_type_views_obj.vehicle_type_menu())
        mock_case_1.assert_called_once()
        mock_case_2.assert_called_once()
        mock_case_3.assert_called_once()

    @patch('builtins.input')
    def test_vehcile_type_menu_positive(self, mock_input: Mock) -> bool:
        mock_input.return_value = '4'
        self.assertTrue(self.vehicle_type_views_obj.vehicle_type_menu())