import aiohttp
import asyncio

import argparse

from typing import List
from time import time


async def fetch_url(url: str, output_filename: str) -> bool:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                with open(output_filename, "w+") as output:
                    output.write(await response.text())
                    return True
            return False


async def fetch_urls(urls: List[str], count: int) -> int:
    if count <= 0:
        return

    fetched = 0
    actually_fetched = 0

    while fetched < len(urls):
        tasks = []

        for i in range(min(count, len(urls))):
            if fetched + i >= len(urls):
                break

            tasks.append(
                asyncio.create_task(
                    fetch_url(urls[fetched + i], f"output_{fetched + i + 1}")
                )
            )

        result = await asyncio.gather(*tasks)
        actually_fetched += result.count(True)
        fetched += min(len(urls), count)

    return actually_fetched


if __name__ == "__main__":
    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument("-c", "--count", type=int, required=True, help="count")
    argument_parser.add_argument("source", help="source")
    args = argument_parser.parse_args()

    count, urls_file = vars(args)["count"], vars(args)["source"]
    urls = []

    with open(urls_file) as source_file:
        for line in source_file:
            urls.append(line)

    start = time()
    result = asyncio.run(fetch_urls(urls, count))
    print(f"fetched {result} / {len(urls)} urls in {time() - start} sec")
