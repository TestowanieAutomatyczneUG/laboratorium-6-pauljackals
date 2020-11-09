import unittest
from ex2_valid_password.ex2_valid_password import ValidPassword


class TestValidPassword(unittest.TestCase):
    def setUp(self):
        self.temp = ValidPassword()

    def test_valid_password(self):
        self.assertTrue(self.temp.valid_password('fEr!gr9ht'))

    def test_valid_password_all_uppercase(self):
        self.assertTrue(self.temp.valid_password('FER!GR9T'))

    def test_too_short(self):
        self.assertFalse(self.temp.valid_password('4r3ff'))

    def test_no_uppercase(self):
        self.assertFalse(self.temp.valid_password('fer!gr9ht'))

    def test_no_digit(self):
        self.assertFalse(self.temp.valid_password('fEr!grht'))

    def test_no_special(self):
        self.assertFalse(self.temp.valid_password('feRgr9ht'))

    def test_wrong_type(self):
        with self.assertRaises(ValueError):
            self.temp.valid_password([])

    def tearDown(self):
        self.temp = None


if __name__ == '__main__':
    unittest.main()
