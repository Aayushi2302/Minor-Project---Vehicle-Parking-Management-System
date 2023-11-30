import unittest
from unittest.mock import Mock, patch
from src.utils.common_helper import CommonHelper

class TestCommonHelper(unittest.TestCase):
    
    @classmethod
    @patch('src.utils.common_helper.DBHelper')
    def setUpClass(cls, mock_cls: Mock)-> bool:
        cls.db_helper_obj = mock_cls()
        cls.common_helper_obj = CommonHelper()

    def test_is_admin_registered_positive(self)-> bool:
        self.db_helper_obj.get_employee.return_value = ["admin"]
        self.assertTrue(self.common_helper_obj.is_admin_registered())
    
    def test_is_admin_registered_negative(self)-> bool:
        self.db_helper_obj.get_employee.return_value = []
        self.assertFalse(self.common_helper_obj.is_admin_registered())

    @patch('src.utils.common_helper.hashlib.sha256')
    @patch('src.utils.common_helper.CommonHelper.input_validation')
    @patch('src.utils.common_helper.maskpass.askpass')
    def test_create_new_password(self, mock_maskpass: Mock, mock_input_validation: Mock, mock_hashlib: Mock)-> bool:
        mock_maskpass.side_effect = ["123", "Aayushi@123", "Aayushi123", "Aayushi@123", "Aayushi@123"]
        mock_input_validation.side_effect = [False, True, True]
        mock_hashlib().hexdigest.return_value = "PasswordHashed"
        self.db_helper_obj.update_password.return_value = True
        self.assertEqual(self.common_helper_obj.create_new_password("demo"), None)

    def test_view_individual_employee_details(self)-> bool:
        self.db_helper_obj.get_single_employee_details.return_value = ["data"]
        self.assertIsNone(self.common_helper_obj.view_individual_employee_details("user@aayushi"))
    
    @patch('src.utils.common_helper.re.match')
    def test_input_validation_positive(self, mock_re: Mock)-> bool:
        mock_re.return_value = "Matched"
        self.assertTrue(self.common_helper_obj.input_validation("demo_regex", "demo_data"))

    @patch('src.utils.common_helper.re.match')
    def test_input_validation_negative(self, mock_re: Mock)-> bool:
        mock_re.return_value = None
        self.assertFalse(self.common_helper_obj.input_validation("demo_regex", "demo_data"))

if __name__ == '__main__':
    unittest.main()