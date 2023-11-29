import unittest
from unittest.mock import Mock, patch
from src.utils.common_helper import CommonHelper

class TestCommonHelper(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.db_helper_obj = Mock()
        cls.common_helper_obj = CommonHelper()

    @patch("src.utils.common_helper.DBHelper.get_employee")
    def test_is_admin_registered(self, mock_db_helper):
        mock_db_helper.side_effect = [[], ["admin"]]
        self.assertFalse(self.common_helper_obj.is_admin_registered())
        self.assertTrue(self.common_helper_obj.is_admin_registered())

    @patch('src.utils.common_helper.DBHelper.update_password')
    @patch('hashlib.sha256')
    @patch('src.utils.common_helper.CommonHelper.input_validation')
    @patch('maskpass.askpass')
    def test_create_new_password(self, mock_maskpass, mock_input_validation, mock_hashlib, mock_db_helper):
        mock_maskpass.side_effect = ["Aayushi@123", "Aayushi123", "Aayushi@123", "Aayushi@123"]
        mock_input_validation.side_effect = [False, True]
        mock_hashlib.hexdigest.return_value = "2234sdfkdg"
        mock_db_helper.return_value = True
        self.assertEqual(self.common_helper_obj.create_new_password("demo"), None)
