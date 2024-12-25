import asyncio
import unittest
from unittest import TestCase, mock
from unittest.mock import patch, MagicMock
import fetcher


class TestFetchURL(TestCase):
    @patch("fethcer.aiohttp.ClientSession.get")
    async def test_fetch_url_success(self, mock_get):
        mock_response = MagicMock(status=200)
        mock_response.text = asyncio.Future()
        mock_response.text.set_result("response content")
        mock_get.return_value = asyncio.Future()
        mock_get.return_value.set_result(mock_response)

        success = await fetcher.fetch_url("http://example.com", "output_test.txt")

        self.assertTrue(success)
        with open("output_test.txt", "r") as file:
            self.assertEqual(file.read(), "response content")

    @patch("fetcher.aiohttp.ClientSession.get")
    async def test_fetch_url_failure(self, mock_get):
        mock_response = MagicMock(status=404)
        mock_get.return_value = asyncio.Future()
        mock_get.return_value.set_result(mock_response)

        success = await fetcher.fetch_url("http://example.com", "output_test.txt")

        self.assertFalse(success)


class TestFetchURLs(TestCase):
    @patch("your_script.fetch_url")
    async def test_fetch_urls(self, mock_fetch_url):
        mock_fetch_url.side_effect = [True, False, True]

        urls = ["http://example.com/1", "http://example.com/2", "http://example.com/3"]
        count = 2

        actually_fetched = await fetcher.fetch_urls(urls, count)

        self.assertEqual(actually_fetched, 2)
        self.assertEqual(mock_fetch_url.call_count, 3)


if __name__ == "__main__":
    asyncio.run(unittest.main())
