"""Module for testing parking controller input."""

import unittest
from unittest.mock import Mock, patch
from src.utils.input_validator.parking_controller_validator import ParkingControllerValidator

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
    @patch("src.utils.input_validator.parking_controller_validator.CommonHelper.input_validation")
    @patch("builtins.input")
    def test_input_vehicle_type_name(self, mock_input: Mock, mock_input_validation: Mock) -> bool:
        """
            Method for testing vehicle type name input.
            Parameter -> self, mock_input: Mock, mock_input_validation: Mock
            Return type -> bool
        """
        mock_input.side_effect = ["123", " ", "car"]
        mock_input_validation.side_effect = [False, False, True]
        self.assertEqual(ParkingControllerValidator.input_vehicle_type_name(), "Car")

    @patch("src.utils.input_validator.parking_controller_validator.CommonHelper.input_validation")
    @patch("builtins.input")
    def test_input_price_per_hour(self, mock_input: Mock, mock_input_validation: Mock) -> bool:
        """
            Method for testing price per hour input.
            Parameter -> self, mock_input: Mock, mock_input_validation: Mock
            Return type -> bool
        """
        mock_input.side_effect = ["14.", "kghdfg", " ", "12"]
        mock_input_validation.side_effect = [False, False, False, True]
        self.assertEqual(ParkingControllerValidator.input_price_per_hour(), 12)

    @patch("src.utils.input_validator.parking_controller_validator.CommonHelper.input_validation")
    @patch("builtins.input")
    def test_input_vehicle_type_id(self, mock_input: Mock, mock_input_validation: Mock) -> bool:
        """
            Method for testing vehicle type id input.
            Parameter -> self, mock_input: Mock, mock_input_validation: Mock
            Return type -> bool
        """
        mock_input.side_effect = ["TYPE", "123", "TYPE1234"]
        mock_input_validation.side_effect = [False, False, True]
        self.assertEqual(ParkingControllerValidator.input_vehicle_type_id(), "TYPE1234")

    @patch("src.utils.input_validator.parking_controller_validator.CommonHelper.input_validation")
    @patch("builtins.input")
    def test_input_parking_slot_number(self, mock_input: Mock, mock_input_validation: Mock) -> bool:
        """
            Method for testing parking slot number input.
            Parameter -> self, mock_input: Mock, mock_input_validation: Mock
            Return type -> bool
        """
        mock_input.side_effect = ["psn", "12", "PSN12"]
        mock_input_validation.side_effect = [False, False, True]
        self.assertEqual(ParkingControllerValidator.input_parking_slot_number(), "PSN12")

    @patch("src.utils.input_validator.parking_controller_validator.CommonHelper.input_validation")
    @patch("builtins.input")
    def test_input_vehicle_number(self, mock_input: Mock, mock_input_validation: Mock) -> bool:
        """
            Method for testing input vehicle number input.
            Parameter -> self, mock_input: Mock, mock_input_validation: Mock
            Return type -> bool
        """
        mock_input.side_effect = ["RJ-02-AB-", " ", "RJ-02-AB-1974"]
        mock_input_validation.side_effect = [False, False, True]
        self.assertEqual(ParkingControllerValidator.input_vehicle_number(), "RJ-02-AB-1974")

    # @patch("src.utils.input_validator.parking_controller_validator.datetime.strptime")
    # @patch("src.utils.input_validator.parking_controller_validator.datetime.now")
    @patch("builtins.input")
    def test_input_out_date(self, mock_input: Mock) -> bool:
        """
            Method for testing out date input.
            Parameter -> self, mock_input: Mock, mock_input_validation: Mock
            Return type -> bool
        """
        mock_input.side_effect = ["12-22-2023", "29-11-2023"]
        # mock_datetime_now.return_value = "28-11-2023"
        # mock_datetime_strptime.return_value = "29-11-2023"
        self.assertEqual(ParkingControllerValidator.input_out_date(), "29-11-2023")

if __name__ == '__main__':
    unittest.main()
