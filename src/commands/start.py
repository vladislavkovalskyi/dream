import asyncio

from mubble import Dispatch, WaiterMachine, Message, CallbackQuery
from mubble.rules import StartCommand, CallbackDataMarkup, HasText

from src.keyboards import Keyboard
from src.database import User, Business, Supplier

dp = Dispatch()
wm = WaiterMachine()


@dp.message(StartCommand())
async def start(message: Message):
    await message.answer(
        f"💸 {message.from_user.first_name}\, *Dream* вітає тебе\!\n"
        "Для людей\, які тільки *починають розвивати свій бізнес*\, або вже *мають* його\, я просто *must have\.*",
        parse_mode="MarkdownV2"
    )
    await asyncio.sleep(1.5)

    await message.answer("📌 Чому?")
    await asyncio.sleep(0.7)

    await message.answer(
        "💼 *Переваги для бізнесменів*\:\n"
        "• Я маю потужний функціонал для *пошуку тендерів та грантів*\.\n"
        "• Я допоможу знайти *надійного* та *перевіреного* постачальника\.\n"
        "• Я можу *провести аналіз ринку* на основі твоєї бізнес\-ідеї\.\n"
        "• Я *перевірю* твої ідеї на *унікальність* та *допоможу* розробити новаторську ідею\.",
        parse_mode="MarkdownV2"
    )
    await asyncio.sleep(10)

    await message.answer(
        "📦 *Переваги для постачальників*\:\n"
        "• Я допоможу тобі *знайти надійного партнера*\, враховуючи твої стандарти\.\n"
        "• Я надам доступ до *широкої бази підприємств*\, які шукають твої товари\.\n"
        "• Я надішлю тобі інсайти щодо попиту на твої товари\, що допоможе планувати виробництво\.\n"
        "• Я створю всі умови\, *для приємної взаємодії* з твоїми *майбутніми партнерами*\.",
        parse_mode="MarkdownV2"
    )
    await asyncio.sleep(10)

    await message.answer(
        "💡 Тобі потрібно обрати *тип акаунта* для подальшого користування ботом\.",
        parse_mode="MarkdownV2",
        reply_markup=Keyboard.get_account_type,
    )


@dp.callback_query(CallbackDataMarkup("choice_<account_type>_account"))
async def choice_account_type(cq: CallbackQuery, account_type: str = None):
    types = {"business": Business, "supplier": Supplier}

    text = (
        f"🎉 Вітаю з реєстрацією акаунта типа *{'Бізнес' if account_type == 'business' else 'Постачальник'}*\n"
    )
    await cq.ctx_api.send_message(cq.message.unwrap().chat.id, text, parse_mode="MarkdownV2")
