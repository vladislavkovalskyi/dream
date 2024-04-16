from mubble import Dispatch, Message
from mubble.rules import StartCommand


dp = Dispatch()


@dp.message(StartCommand())
async def start(message: Message):
    await message.answer("Hello test")