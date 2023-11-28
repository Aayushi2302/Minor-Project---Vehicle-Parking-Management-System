import unittest

class TestUserControllerValidator(unittest.TestCase):

    def test_input_name(self) -> str:
        self.assertEquals("Aayushi", "Aayushi")

if __name__ == '__main__':
    unittest.main()