from unittest import TestCase
from unittest.mock import Mock, patch

from views.parking_views.parking_slot_views import ParkingSlotViews

class TestParkingSlotViews(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.parking_slot_views_obj = ParkingSlotViews()

    @patch('views.parking_views.parking_slot_views.ParkingSlot.register_parking_slot')
    @patch('views.parking_views.parking_slot_views.ParkingControllerValidator.input_vehicle_type_name')
    @patch('views.parking_views.parking_slot_views.ParkingControllerValidator.input_parking_slot_number')
    def test_parking_slot_registration_positive(self, mock_intput_parking_slot_no: Mock, mock_input_vehicle_type_name: Mock, mock_register_parking_slot: Mock) -> None:
        mock_intput_parking_slot_no.return_value = "PSN001"
        mock_input_vehicle_type_name.return_value = "Car"
        mock_register_parking_slot.return_value = True
        self.assertIsNone(self.parking_slot_views_obj.parking_slot_registration_form())
        mock_register_parking_slot.assert_called_once_with("PSN001", "Car")

    @patch('views.parking_views.parking_slot_views.ParkingSlot.register_parking_slot')
    @patch('views.parking_views.parking_slot_views.ParkingControllerValidator.input_vehicle_type_name')
    @patch('views.parking_views.parking_slot_views.ParkingControllerValidator.input_parking_slot_number')
    def test_parking_slot_registration_negative(self, mock_intput_parking_slot_no: Mock, mock_input_vehicle_type_name: Mock, mock_register_parking_slot: Mock) -> None:
        mock_intput_parking_slot_no.return_value = "PSN001"
        mock_input_vehicle_type_name.return_value = "Car"
        mock_register_parking_slot.return_value = False
        self.assertIsNone(self.parking_slot_views_obj.parking_slot_registration_form())
        mock_register_parking_slot.assert_called_once_with("PSN001", "Car")

    @patch('views.parking_views.parking_slot_views.ParkingSlot.get_all_parking_slots')
    def test_view_parking_slots_positive(self, mock_get_all_parking_slots: Mock) -> None:
        mock_get_all_parking_slots.return_value = [("parking slot data", )]
        self.assertIsNone(self.parking_slot_views_obj.view_parking_slots())

    @patch('views.parking_views.parking_slot_views.ParkingSlot.get_all_parking_slots')
    def test_view_parking_slots_negative(self, mock_get_all_parking_slots: Mock) -> None:
        mock_get_all_parking_slots.return_value = []
        self.assertIsNone(self.parking_slot_views_obj.view_parking_slots())

    @patch('views.parking_views.parking_slot_views.ParkingSlot.update_parking_slot_status')
    @patch('views.parking_views.parking_slot_views.ParkingControllerValidator.input_parking_slot_number')
    @patch('views.parking_views.parking_slot_views.ParkingSlotViews.view_parking_slots')
    @patch('views.parking_views.parking_slot_views.ParkingSlot.get_all_parking_slots')
    def test_parking_slot_status_updation_form_positive(self, mock_get_all_parking_slots: Mock, mock_view_parking_slots: Mock, mock_input_parking_slot_no: Mock, mock_update_parking_slot: Mock) -> None:
        mock_get_all_parking_slots.return_value = [("data", )]
        mock_view_parking_slots.return_value = None
        mock_input_parking_slot_no.return_value = "PSN001"
        mock_update_parking_slot.return_value = 1
        self.assertIsNone(self.parking_slot_views_obj.parking_slot_status_updation_form("vacant"))
        mock_update_parking_slot.assert_called_once_with("PSN001","status", "vacant")

    @patch('views.parking_views.parking_slot_views.ParkingControllerValidator.input_parking_slot_number')
    @patch('views.parking_views.parking_slot_views.ParkingSlotViews.view_parking_slots')
    @patch('views.parking_views.parking_slot_views.ParkingSlot.get_all_parking_slots')
    def test_parking_slot_status_updation_form_negative(self, mock_get_all_parking_slots: Mock, mock_view_parking_slots: Mock, mock_input_parking_slot_no: Mock) -> None:
        mock_get_all_parking_slots.side_effect = [[], [("data", )]]
        mock_view_parking_slots.return_value = None
        mock_input_parking_slot_no.return_value = "PSN001"
        self.assertIsNone(self.parking_slot_views_obj.parking_slot_status_updation_form("booked"))
        self.assertIsNone(self.parking_slot_views_obj.parking_slot_status_updation_form("vacant"))

    @patch('views.parking_views.parking_slot_views.ParkingSlotViews.view_parking_slots')
    @patch('views.parking_views.parking_slot_views.ParkingSlotViews.parking_slot_status_updation_form')
    @patch('views.parking_views.parking_slot_views.ParkingSlotViews.parking_slot_registration_form')
    @patch('builtins.input')
    def test_parking_slot_menu_negative(self, mock_input: Mock, mock_registration_form: Mock, mock_updation_form: Mock, mock_view_parking_slots: Mock) -> None:
        mock_input.side_effect = ['1', '2', '3', '4', '5', 'default', '6']
        mock_registration_form.return_value = None
        mock_updation_form.return_value = None
        mock_view_parking_slots.return_value = None
        self.assertTrue(self.parking_slot_views_obj.parking_slot_menu())
        mock_registration_form.assert_called_once()
        mock_view_parking_slots.assert_called_once()
    
    @patch('builtins.input')
    def test_parking_slot_menu_positive(self, mock_input: Mock) -> None:
        mock_input.return_value = '6'
        self.assertTrue(self.parking_slot_views_obj.parking_slot_menu())
