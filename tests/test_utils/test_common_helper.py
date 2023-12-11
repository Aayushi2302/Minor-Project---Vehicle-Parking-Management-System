import unittest
from unittest.mock import Mock, patch
from src.utils.common_helper import CommonHelper

class TestCommonHelper(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls) -> None:
        cls.common_helper_obj = CommonHelper()

    @patch("src.utils.common_helper.db")
    def test_is_admin_registered_positive(self, mock_db: Mock)-> bool:
        mock_db.fetch_data_from_database.return_value = ["admin"]
        self.assertTrue(self.common_helper_obj.is_admin_registered())
        mock_db.fetch_data_from_database.asset_called_once()
    
    @patch("src.utils.common_helper.db")
    def test_is_admin_registered_negative(self, mock_db: Mock)-> bool:
        mock_db.fetch_data_from_database.return_value = []
        self.assertFalse(self.common_helper_obj.is_admin_registered())
        mock_db.fetch_data_from_database.asset_called_once()

    @patch("src.utils.common_helper.db")
    @patch('src.utils.common_helper.hashlib.sha256')
    @patch('src.utils.common_helper.CommonHelper.input_validation')
    @patch('src.utils.common_helper.maskpass.askpass')
    def test_create_new_password(self, mock_maskpass: Mock, mock_input_validation: Mock, mock_hashlib: Mock, mock_db: Mock)-> bool:
        mock_maskpass.side_effect = ["123", "Aayushi@123", "Aayushi123", "Aayushi@123", "Aayushi@123"]
        mock_input_validation.side_effect = [False, True, True]
        mock_hashlib().hexdigest.return_value = "PasswordHashed"
        mock_db.save_data_to_database.return_value = True
        self.assertEqual(self.common_helper_obj.create_new_password("demo"), None)
        mock_db.save_data_to_database.asset_called_once()

    @patch("src.utils.common_helper.db")
    def test_view_individual_employee_details(self, mock_db: Mock)-> bool:
        mock_db.fetch_data_from_database.return_value = ["data"]
        self.assertIsNone(self.common_helper_obj.view_individual_employee_details("user@aayushi"))
        mock_db.fetch_data_from_database.asset_called_once()
        
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