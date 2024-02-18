"""Module for testing parking controller input."""
from datetime import datetime
import unittest
from unittest.mock import Mock, patch
from utils.input_validator.parking_controller_validator import ParkingControllerValidator

class TestParkingControllerValidator(unittest.TestCase):
    """
        Class containing methods for testing ParkingControllerValidator.
        ...
        Methods
        ------
        test_vehicle_type_name() -> Method for testing vehicle type name input.
        test_input_price_per_hour() -> Method for testing price per hour input.
        test_input_vehicle_type_id -> Method for testing vehicle type id input.
        test_input_parking_slot_number() -> Method for testing parking slot number input.
        test_input_vehicle_number() -> Method for testing vehicle number input.
        test_input_out_date() -> Method for testing out date input.
    """
    @patch("utils.input_validator.parking_controller_validator.CommonHelper.regex_validation")
    @patch("builtins.input")
    def test_input_vehicle_type_name(self, mock_input: Mock, mock_regex_validation: Mock) -> bool:
        """
            Method for testing vehicle type name input.
            Parameter -> self, mock_input: Mock, mock_regex_validation: Mock
            Return type -> bool
        """
        mock_input.side_effect = ["123", " ", "car"]
        mock_regex_validation.side_effect = [False, False, True]
        self.assertEqual(ParkingControllerValidator.input_vehicle_type_name(), "Car")

    @patch("utils.input_validator.parking_controller_validator.CommonHelper.regex_validation")
    @patch("builtins.input")
    def test_input_price_per_hour(self, mock_input: Mock, mock_regex_validation: Mock) -> bool:
        """
            Method for testing price per hour input.
            Parameter -> self, mock_input: Mock, mock_regex_validation: Mock
            Return type -> bool
        """
        mock_input.side_effect = ["14.", "kghdfg", " ", "12"]
        mock_regex_validation.side_effect = [False, False, False, True]
        self.assertEqual(ParkingControllerValidator.input_price_per_hour(), 12)

    @patch("utils.input_validator.parking_controller_validator.CommonHelper.regex_validation")
    @patch("builtins.input")
    def test_input_vehicle_type_id(self, mock_input: Mock, mock_regex_validation: Mock) -> bool:
        """
            Method for testing vehicle type id input.
            Parameter -> self, mock_input: Mock, mock_regex_validation: Mock
            Return type -> bool
        """
        mock_input.side_effect = ["TYPE", "123", "TYPE1234"]
        mock_regex_validation.side_effect = [False, False, True]
        self.assertEqual(ParkingControllerValidator.input_vehicle_type_id(), "TYPE1234")

    @patch("utils.input_validator.parking_controller_validator.CommonHelper.regex_validation")
    @patch("builtins.input")
    def test_input_parking_slot_number(self, mock_input: Mock, mock_regex_validation: Mock) -> bool:
        """
            Method for testing parking slot number input.
            Parameter -> self, mock_input: Mock, mock_regex_validation: Mock
            Return type -> bool
        """
        mock_input.side_effect = ["psn", "12", "PSN12"]
        mock_regex_validation.side_effect = [False, False, True]
        self.assertEqual(ParkingControllerValidator.input_parking_slot_number(), "PSN12")

    @patch("utils.input_validator.parking_controller_validator.CommonHelper.regex_validation")
    @patch("builtins.input")
    def test_input_vehicle_number(self, mock_input: Mock, mock_regex_validation: Mock) -> bool:
        """
            Method for testing input vehicle number input.
            Parameter -> self, mock_input: Mock, mock_regex_validation: Mock
            Return type -> bool
        """
        mock_input.side_effect = ["RJ-02-AB-", " ", "RJ-02-AB-1974"]
        mock_regex_validation.side_effect = [False, False, True]
        self.assertEqual(ParkingControllerValidator.input_vehicle_number(), "RJ-02-AB-1974")

    @patch("builtins.input")
    def test_input_out_date(self, mock_input: Mock) -> bool:
        """
            Method for testing out date input.
            Parameter -> self, mock_input: Mock, mock_regex_validation: Mock
            Return type -> bool
        """
        current_date = datetime.now().date()
        current_date = current_date.strftime("%d-%m-%Y")
        mock_input.side_effect = ["12-22-2023", "27-11-2023", current_date]
        self.assertEqual(ParkingControllerValidator.input_out_date(), current_date)

if __name__ == '__main__':
    unittest.main()
