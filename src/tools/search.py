import aiohttp
import json
from mubble import Dispatch, Message
from mubble.rules import Command

url = "https://google.serper.dev/search"

headers = {
    'X-API-KEY': '',
    'Content-Type': 'application/json'
}

dp = Dispatch()


async def search(query):
    async with aiohttp.ClientSession() as session:
        payload = json.dumps({
            "q": query,
            "location": "Ukraine",
            "gl": "ua",
            "hl": "ua"
        })
        async with session.post(url, headers=headers, data=payload) as response:
            return await response.json()


@dp.message(Command('search'))
async def search_handler(message: Message):
    query = message.text.split(' ', 1)[1]  # Витягуємо запитання з повідомлення користувача

    search_results = await search(query)

    if 'organic_results' in search_results:
        results = search_results['organic_results']
        response_text = "Результати пошуку:\n"
        for result in results:
            response_text += f"{result['title']}: {result['link']}\n"
    else:
        response_text = "На жаль, за вашим запитом нічого не знайдено."

    await message.answer(response_text)