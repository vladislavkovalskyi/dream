import aiohttp
import json

from src.config import SERPER_NEWS_API

url = "https://google.serper.dev/search"

headers = {"X-API-KEY": SERPER_NEWS_API, "Content-Type": "application/json"}


async def search_raw(query: str) -> dict:
    async with aiohttp.ClientSession() as session:
        payload = json.dumps(
            {"q": query, "location": "Ukraine", "gl": "ua", "hl": "ua"}
        )
        async with session.post(url, headers=headers, data=payload) as response:
            return await response.json()


async def get_links(search_responce: dict) -> list:
    links = []
    for result in search_responce["organic"]:
        links.append([result["title"], result["link"]])
    return links
