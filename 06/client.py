import argparse


if __name__ == "__main__":
    argument_parser = argparse.ArgumentParser(
        "Client", "Multithreading app for sending url to server, recieving answer"
    )
    argument_parser.add_argument("threads count", default=None, type=int)
    argument_parser.add_argument("urls file", default=None, type=str)

    args = argument_parser.parse_args()
