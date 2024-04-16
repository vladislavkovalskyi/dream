from tools.search import search
import asyncio

async def main():
    test = await search("привет")
    print(test)

asyncio.run(main())