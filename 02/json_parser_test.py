import unittest
from unittest import mock
from unittest.mock import MagicMock
from faker import Faker
from json_parser import parse_json


class TestParseJson(unittest.TestCase):
    
    def setUp(self):
        self.keyword_callback = MagicMock()
        self.json_str = ""


    def test_parse_json_none(self):
        required_fileds = []


        result = parse_json(self.json_str, self.keyword_callback, required_fields, keywords)
        self.assertEqual()
        


if __name__ == '__main__':
    unittest.main()