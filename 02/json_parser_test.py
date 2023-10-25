import unittest
from unittest.mock import MagicMock
from unittest import mock
from json_parser import parse_json


class TestParseJson(unittest.TestCase):
    def setUp(self):
        self.keyword_callback = MagicMock()

    def test_parse_json_none(self):
        required_fileds = None
        keywords = None
        json_str = '{"key1": "Word1 word2", "key2": "word2 word3"}'
        result = parse_json(
            json_str,
            self.keyword_callback,
            required_fields=required_fileds,
            keywords=keywords,
        )
        self.assertEqual(result, False)
        self.assertEqual([], self.keyword_callback.mock_calls)

    def test_parse_json_keywords_none(self):
        required_fileds = ["key1"]
        keywords = None
        json_str = '{"key1": "Word1 word2", "key2": "word2 word3"}'
        result = parse_json(
            json_str,
            self.keyword_callback,
            required_fields=required_fileds,
            keywords=keywords,
        )
        self.assertEqual(result, False)
        self.assertEqual([], self.keyword_callback.mock_calls)

    def test_parse_json_from_example(self):
        json_str = '{"key1": "Word1 word2", "key2": "word2 word3"}'
        required_fileds = ["key1"]
        keywords = ["word2"]
        result = parse_json(
            json_str,
            self.keyword_callback,
            required_fields=required_fileds,
            keywords=keywords,
        )
        expected_calls = [mock.call("key1", "word2")]

        self.assertEqual(result, True)
        self.assertEqual(expected_calls, self.keyword_callback.mock_calls)


if __name__ == "__main__":
    unittest.main()
