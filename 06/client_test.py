import unittest
import socket
from unittest.mock import patch, MagicMock
from client import make_request, read_file


class TestLRUCache(unittest.TestCase):
    @patch("client.socket.socket")
    def test_make_request_sends_data(self, mock_socket):
        mock_socket_instance = MagicMock()
        mock_socket.return_value = mock_socket_instance

        url = "test"
        make_request(url)

        mock_socket.assert_called_once_with(socket.AF_INET, socket.SOCK_STREAM)

        mock_socket_instance.__enter__().connect.assert_called_once_with(
            ("127.0.0.1", 53210)
        )

        mock_socket_instance.__enter__().sendall.assert_called_once_with(url.encode())
        mock_socket_instance.__enter__().recv.assert_called_once_with(1024)


if __name__ == "__main__":
    unittest.main()
