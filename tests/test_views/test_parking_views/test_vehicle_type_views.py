from unittest import TestCase
from unittest.mock import Mock, patch

from src.views.parking_views.vehicle_type_views import VehicleTypeViews

class TestVehicleTypeViews(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.vehicle_type_views_obj = VehicleTypeViews()

    @patch('src.views.parking_views.vehicle_type_views.VehicleType.register_vehicle_type')
    @patch('src.views.parking_views.vehicle_type_views.shortuuid.ShortUUID.random')
    @patch('src.views.parking_views.vehicle_type_views.ParkingControllerValidator.input_price_per_hour')
    @patch('src.views.parking_views.vehicle_type_views.ParkingControllerValidator.input_vehicle_type_name')
    def test_vehicle_type_registration_form(self, mock_input_type_name: Mock, mock_input_price: Mock, mock_shortuuid: Mock, mock_register_vehicle_type: Mock) -> bool:
        mock_input_type_name.return_value = "car"
        mock_input_price.return_value = 25.23
        mock_shortuuid.return_value = "1234"
        self.assertIsNone(self.vehicle_type_views_obj.vehicle_type_registration_form())
        mock_register_vehicle_type.assert_called_once_with("TYPE1234", "car", 25.23)

    @patch('src.views.parking_views.vehicle_type_views.VehicleType.get_all_vehicle_type')
    def test_view_vehicle_type_positive(self, mock_get_all_vehicle_type: Mock) -> bool:
        mock_get_all_vehicle_type.return_value = [("data", )]
        self.assertIsNone(self.vehicle_type_views_obj.view_vehicle_type())

    @patch('src.views.parking_views.vehicle_type_views.VehicleType.get_all_vehicle_type')
    def test_view_vehicle_type_negative(self, mock_get_all_vehicle_type: Mock) -> bool:
        mock_get_all_vehicle_type.return_value = []
        self.assertIsNone(self.vehicle_type_views_obj.view_vehicle_type())

    @patch('src.views.parking_views.vehicle_type_views.VehicleType.update_vehicle_type_detail')
    @patch('src.views.parking_views.vehicle_type_views.ParkingControllerValidator.input_price_per_hour')
    @patch('src.views.parking_views.vehicle_type_views.VehicleType.get_vehicle_type_data_from_type_id')
    @patch('src.views.parking_views.vehicle_type_views.ParkingControllerValidator.input_vehicle_type_id')
    @patch('src.views.parking_views.vehicle_type_views.VehicleTypeViews.view_vehicle_type')
    @patch('src.views.parking_views.vehicle_type_views.VehicleType.get_all_vehicle_type')
    def test_vehicle_type_update_form_positive(self, mock_get_all_vehicle: Mock, mock_view_vehicle: Mock, mock_input_type_id: Mock, mock_get_data_from_type_id: Mock, mock_input_price: Mock, mock_update_vehicle_type: Mock) -> bool:
        mock_get_all_vehicle.return_value = [("employee data", )]
        mock_view_vehicle.return_value = None
        mock_input_type_id.return_value = "TYPE1234"
        mock_get_data_from_type_id.return_value = [(25.23, )]
        mock_input_price.return_value = 30.45
        self.assertIsNone(self.vehicle_type_views_obj.vehicle_type_update_form())
        mock_update_vehicle_type.assert_called_once_with(30.45, "price_per_hour", "TYPE1234")

    @patch('src.views.parking_views.vehicle_type_views.VehicleType.get_vehicle_type_data_from_type_id')
    @patch('src.views.parking_views.vehicle_type_views.ParkingControllerValidator.input_vehicle_type_id')
    @patch('src.views.parking_views.vehicle_type_views.VehicleTypeViews.view_vehicle_type')
    @patch('src.views.parking_views.vehicle_type_views.VehicleType.get_all_vehicle_type')
    def test_vehicle_type_update_form_negative(self, mock_get_all_vehicle: Mock, mock_view_vehicle: Mock, mock_input_type_id: Mock, mock_get_data_from_type_id: Mock) -> bool:
        mock_get_all_vehicle.side_effect = [[], [("employee data", )]]
        mock_view_vehicle.return_value = None
        mock_input_type_id.return_value = "TYPE1234"
        mock_get_data_from_type_id.return_value = []
        self.assertIsNone(self.vehicle_type_views_obj.vehicle_type_update_form())
        self.assertIsNone(self.vehicle_type_views_obj.vehicle_type_update_form())

    @patch('src.views.parking_views.vehicle_type_views.VehicleTypeViews.view_vehicle_type')
    @patch('src.views.parking_views.vehicle_type_views.VehicleTypeViews.vehicle_type_update_form')
    @patch('src.views.parking_views.vehicle_type_views.VehicleTypeViews.vehicle_type_registration_form')
    @patch('builtins.input')
    def test_vehicle_type_menu_negative(self, mock_input: Mock, mock_case_1: Mock, mock_case_2: Mock, mock_case_3: Mock) -> bool:
        mock_input.side_effect = ['1', '2', '3', 'default']
        self.assertFalse(self.vehicle_type_views_obj.vehicle_type_menu())
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