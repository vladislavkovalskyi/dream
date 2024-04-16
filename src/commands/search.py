import asyncio

from mubble import Dispatch, WaiterMachine, Message, CallbackQuery
from mubble.rules import StartCommand, CallbackDataMarkup, HasText, Markup

from src.tools.search import search_raw, get_links

dp = Dispatch()
wm = WaiterMachine()


@dp.message(Markup("/search <query>"))
async def search_handler(message: Message, query: str = None):
    search_results = await search_raw(query)
    links = await get_links(search_results)

    text = ""
    for title, link in links:
        text += f"{title}: {link}\n\n"
    await message.answer(text)
