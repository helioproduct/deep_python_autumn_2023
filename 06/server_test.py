import unittest
import socket
from unittest.mock import patch, MagicMock
from server import count_top_frequent_words
import requests
import json


class TestCountTopFrequentWords(unittest.TestCase):
    @patch("server.requests.get")
    def test_count_top_frequent_words(self, mock_get):
        mock_response = requests.Response()
        mock_response.status_code = 200
        mock_response._content = b"<html>test test test example example word</html>"
        mock_get.return_value = mock_response

        url = "http://example.com"
        result = count_top_frequent_words(url, 2)

        expected_result = json.dumps(
            {"test": 3, "example": 2}, indent=4, ensure_ascii=False
        )
        self.assertEqual(result, expected_result)

    @patch("server.requests.get")
    def test_invalid_url(self, mock_get):
        mock_get.side_effect = requests.exceptions.RequestException()

        url = "http://invalidurl.com"
        with self.assertRaises(requests.exceptions.RequestException):
            count_top_frequent_words(url, 2)


if __name__ == "__main__":
    unittest.main()
