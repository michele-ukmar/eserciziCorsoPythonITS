import aiohttp
import asyncio

async def check(url):
    async with aiohttp.ClientSession() as session: 
        async with session.get(url) as response:
            print(f"{url}: status →> {response.status}")
            html = await response.text()
            print(f"{url}: type > {html[:17].strip ()}")

async def main():
    await asyncio.gather (
    check ("https://www.realpython.com"),
    check ("https://www.google.com"),
    )

asyncio.run(main ())