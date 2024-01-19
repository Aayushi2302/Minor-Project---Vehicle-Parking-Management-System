"""Module for testing user controller input."""

import unittest
from unittest.mock import Mock, patch
from src.utils.input_validator.user_controller_validator import UserControllerValidator

class TestUserControllerValidator(unittest.TestCase):
    """
        Class containing methods for testing UserControllerValidator.
        ...
        Methods
        ------
        test_input_name() -> Method for testing name input.
        test_input_username() -> Method for testing username input.
        test_input_age -> Method for testing age input.
        test_input_gender() -> Method for testing gender input.
        test_input_role() -> Method for testing role input.
        test_input_role_admin() -> Method for testing admin role input.
        test_input_email_address() -> Method for testing email address input.
        test_input_mobile_number() -> Method for testing mobile number input.
    """
    @patch("src.utils.input_validator.user_controller_validator.CommonHelper.input_validation")
    @patch("builtins.input")
    def test_input_name(self, mock_input: Mock, mock_input_validation: Mock) -> bool:
        """
            Method for testing name input.
            Parameter -> self, mock_input: Mock, mock_input_validation: Mock
            Return type -> bool
        """
        mock_input.side_effect = ["123", "tanya-verma", " ","Aayushi Sharma"]
        mock_input_validation.side_effect = [False, False, False, True]
        self.assertEqual(UserControllerValidator.input_name(), "Aayushi Sharma")

    @patch("src.utils.input_validator.user_controller_validator.CommonHelper.input_validation")
    @patch("builtins.input")
    def test_input_username(self, mock_input: Mock, mock_input_validation: Mock) -> bool:
        """
            Method for testing username input.
            Parameter -> self, mock_input: Mock, mock_input_validation: Mock
            Return type -> bool
        """
        mock_input.side_effect = ["123", "user@123", "user@", "user@abc", "user@aayushi"]
        mock_input_validation.side_effect = [False, False, False, False, True]
        self.assertEqual(UserControllerValidator.input_username(), "user@aayushi")

    @patch("src.utils.input_validator.user_controller_validator.CommonHelper.input_validation")
    @patch("builtins.input")
    def test_input_age(self, mock_input: Mock, mock_input_validation: Mock) -> bool:
        """
            Method for testing age input.
            Parameter -> self, mock_input: Mock, mock_input_validation: Mock
            Return type -> bool
        """
        mock_input.side_effect = ["abc", "123", "10", "65", "45"]
        mock_input_validation.side_effect = [False, False, False, False, True]
        self.assertEqual(UserControllerValidator.input_age(), 45)

    @patch("builtins.input")
    def test_input_gender(self, mock_input: Mock) -> bool:
        """
            Method for testing gender input.
            Parameter -> self, mock_input: Mock
            Return type -> bool
        """
        mock_input.side_effect = ["N", "F", "M"]
        self.assertEqual(UserControllerValidator.input_gender(), "Female")
        self.assertEqual(UserControllerValidator.input_gender(), "Male")

    @patch("src.utils.input_validator.user_controller_validator.CommonHelper.input_validation")
    @patch("builtins.input")
    def test_input_role(self, mock_input: Mock, mock_input_validation: Mock) -> bool:
        """
            Method for testing role input.
            Parameter -> self, mock_input: Mock, mock_input_validation: Mock
            Return type -> bool
        """
        mock_input.side_effect = ["123", "attendant"]
        mock_input_validation.side_effect = [False, True]
        self.assertEqual(UserControllerValidator.input_role(), "attendant")

    @patch("src.utils.input_validator.user_controller_validator.CommonHelper.input_validation")
    @patch("builtins.input")
    def test_input_role_admin(self, mock_input: Mock, mock_input_validation: Mock) -> bool:
        """
            Method for testing admin role input.
            Parameter -> self
            Return type -> bool
        """
        mock_input.side_effect = ["admin", "staff"]
        mock_input_validation.return_value = True
        self.assertEqual(UserControllerValidator.input_role(), "staff")

    @patch("src.utils.input_validator.user_controller_validator.CommonHelper.input_validation")
    @patch("builtins.input")
    def test_input_email_address(self, mock_input: Mock, mock_input_validation: Mock) -> bool:
        """
            Method for testing email address input.
            Parameter -> self, mock_input: Mock, mock_input_validation: Mock
            Return type -> bool
        """
        mock_input.side_effect = ["admin", "123", "sharmaaayushi2302@gmail.com"]
        mock_input_validation.side_effect = [False, False, True]
        self.assertEqual(UserControllerValidator.input_email_address(), "sharmaaayushi2302@gmail.com")
    
    @patch("src.utils.input_validator.user_controller_validator.CommonHelper.input_validation")
    @patch("builtins.input")
    def test_input_mobile_number(self, mock_input: Mock, mock_input_validation: Mock) -> bool:
        """
            Method for testing email address input.
            Parameter -> self, mock_input: Mock, mock_input_validation: Mock
            Return type -> bool
        """
        mock_input.side_effect = ["12345", "96874563", "6378964512"]
        mock_input_validation.side_effect = [False, False, True]
        self.assertEqual(UserControllerValidator.input_mobile_number(), "6378964512")
