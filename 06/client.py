import socket
import argparse


from concurrent.futures import ThreadPoolExecutor


TCP_ADRESS = "127.0.0.1"
PORT = 53210


def make_request(url: str):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((TCP_ADRESS, PORT))
        s.sendall(b"Hello, world")
        answer = s.recv(1024)

        print(answer.decode())
    return answer


if __name__ == "__main__":
    argument_parser = argparse.ArgumentParser(
        "Client", "Multithreading app for sending url to server, recieving answer"
    )
    argument_parser.add_argument("threads_count", default=None, type=int)
    argument_parser.add_argument("urls_file", default=None, type=str)

    args = argument_parser.parse_args()

    make_request("google.com")
