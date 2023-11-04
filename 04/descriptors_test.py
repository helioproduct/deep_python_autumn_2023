from descriptors import *
import unittest


class TestDescriptors(unittest.TestCase):
    def setUp(self):
        # Create a dummy class to test the descriptors
        class TestClass:
            email = EmailDescriptor()
            age = AgeDescriptor()
            phone_number = PhoneNumberDescriptor()

        self.test_instance = TestClass()

    def test_valid_email(self):
        self.test_instance.email = "test@example.com"
        self.assertEqual(self.test_instance.email, "test@example.com")

    def test_invalid_email(self):
        with self.assertRaises(ValueError):
            self.test_instance.email = "invalid_email"

    def test_valid_age(self):
        self.test_instance.age = 30
        self.assertEqual(self.test_instance.age, 30)

    def test_invalid_age(self):
        with self.assertRaises(ValueError):
            self.test_instance.age = -5

    def test_valid_phone_number(self):
        self.test_instance.phone_number = "1234567890"
        self.assertEqual(self.test_instance.phone_number, "1234567890")

    def test_invalid_phone_number(self):
        with self.assertRaises(ValueError):
            self.test_instance.phone_number = "12345"


if __name__ == "__main__":
    unittest.main()
