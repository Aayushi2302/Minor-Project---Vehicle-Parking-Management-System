from unittest import TestCase
from unittest.mock import Mock, patch

from src.views.parking_views.parking_slot_views import ParkingSlotViews

class TestParkingSlotViews(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.parking_slot_views_obj = ParkingSlotViews()

    @patch('src.views.parking_views.parking_slot_views.ParkingSlot.register_parking_slot')
    @patch('src.views.parking_views.parking_slot_views.VehicleType.get_vehicle_type_id_from_type_name')
    @patch('src.views.parking_views.parking_slot_views.ParkingControllerValidator.input_vehicle_type_name')
    @patch('src.views.parking_views.parking_slot_views.ParkingControllerValidator.input_parking_slot_number')
    def test_parking_slot_registration_positive(self, mock_intput_parking_slot_no: Mock, mock_input_vehicle_type_name: Mock, mock_get_vehicle_type_id: Mock, mock_register_parking_slot: Mock) -> bool:
        mock_intput_parking_slot_no.return_value = "PSN001"
        mock_input_vehicle_type_name.return_value = "Car"
        mock_get_vehicle_type_id.return_value = [("TYPE1234", )]
        mock_register_parking_slot.return_value = None
        self.assertIsNone(self.parking_slot_views_obj.parking_slot_registration_form())
        mock_register_parking_slot.assert_called_once_with("PSN001", "TYPE1234")

    @patch('src.views.parking_views.parking_slot_views.VehicleType.get_vehicle_type_id_from_type_name')
    @patch('src.views.parking_views.parking_slot_views.ParkingControllerValidator.input_vehicle_type_name')
    @patch('src.views.parking_views.parking_slot_views.ParkingControllerValidator.input_parking_slot_number')
    def test_parking_slot_registration_negative(self, mock_intput_parking_slot_no: Mock, mock_input_vehicle_type_name: Mock, mock_get_vehicle_type_id: Mock) -> bool:
        mock_intput_parking_slot_no.return_value = "PSN001"
        mock_input_vehicle_type_name.return_value = "Car"
        mock_get_vehicle_type_id.return_value = []
        self.assertIsNone(self.parking_slot_views_obj.parking_slot_registration_form())

    @patch('src.views.parking_views.parking_slot_views.ParkingSlot.get_all_parking_slots')
    def test_view_parking_slots_positive(self, mock_get_all_parking_slots: Mock) -> bool:
        mock_get_all_parking_slots.return_value = [("parking slot data", )]
        self.assertIsNone(self.parking_slot_views_obj.view_parking_slots())

    @patch('src.views.parking_views.parking_slot_views.ParkingSlot.get_all_parking_slots')
    def test_view_parking_slots_negative(self, mock_get_all_parking_slots: Mock) -> bool:
        mock_get_all_parking_slots.return_value = []
        self.assertIsNone(self.parking_slot_views_obj.view_parking_slots())

    @patch('src.views.parking_views.parking_slot_views.ParkingSlot.update_parking_slot')
    @patch('src.views.parking_views.parking_slot_views.ParkingSlot.get_parking_slot_status')
    @patch('src.views.parking_views.parking_slot_views.ParkingControllerValidator.input_parking_slot_number')
    @patch('src.views.parking_views.parking_slot_views.ParkingSlotViews.view_parking_slots')
    @patch('src.views.parking_views.parking_slot_views.ParkingSlot.get_all_parking_slots')
    def test_parking_slot_status_updation_form_positive(self, mock_get_all_parking_slots: Mock, mock_view_parking_slots: Mock, mock_input_parking_slot_no: Mock,  mock_get_parking_slot_status: Mock, mock_update_parking_slot: Mock) -> bool:
        mock_get_all_parking_slots.return_value = [("data", )]
        mock_view_parking_slots.return_value = None
        mock_input_parking_slot_no.return_value = "PSN001"
        mock_get_parking_slot_status.return_value = [("booked", )]
        mock_update_parking_slot.return_value = None
        self.assertIsNone(self.parking_slot_views_obj.parking_slot_status_updation_form("booked"))
        self.assertIsNone(self.parking_slot_views_obj.parking_slot_status_updation_form("vacant"))
        mock_update_parking_slot.assert_called_once_with("PSN001","status", "vacant")

    @patch('src.views.parking_views.parking_slot_views.ParkingSlot.get_parking_slot_status')
    @patch('src.views.parking_views.parking_slot_views.ParkingControllerValidator.input_parking_slot_number')
    @patch('src.views.parking_views.parking_slot_views.ParkingSlotViews.view_parking_slots')
    @patch('src.views.parking_views.parking_slot_views.ParkingSlot.get_all_parking_slots')
    def test_parking_slot_status_updation_form_negative(self, mock_get_all_parking_slots: Mock, mock_view_parking_slots: Mock, mock_input_parking_slot_no: Mock,  mock_get_parking_slot_status: Mock) -> bool:
        mock_get_all_parking_slots.side_effect = [[], [("data", )]]
        mock_view_parking_slots.return_value = None
        mock_input_parking_slot_no.return_value = "PSN001"
        mock_get_parking_slot_status.return_value = []
        self.assertIsNone(self.parking_slot_views_obj.parking_slot_status_updation_form("booked"))
        self.assertIsNone(self.parking_slot_views_obj.parking_slot_status_updation_form("vacant"))


    @patch('src.views.parking_views.parking_slot_views.ParkingSlotViews.parking_slot_status_updation_form')
    @patch('src.views.parking_views.parking_slot_views.ParkingSlotViews.parking_slot_registration_form')
    @patch('builtins.input')
    def test_parking_slot_menu_negative(self, mock_input: Mock, mock_registration_form: Mock, mock_updation_form: Mock) -> bool:
        mock_input.side_effect = ['1', '2', '3', '4', '5', 'default']
        mock_registration_form.return_value = None
        mock_updation_form.return_value = None
        for _ in range(6):
            self.assertFalse(self.parking_slot_views_obj.parking_slot_menu())
    
    @patch('builtins.input')
    def test_parking_slot_menu_positive(self, mock_input: Mock) -> bool:
        mock_input.return_value = '6'
        self.assertTrue(self.parking_slot_views_obj.parking_slot_menu())