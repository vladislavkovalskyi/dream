from mubble import InlineKeyboard, InlineButton


class Keyboard:
    get_account_type = (
        InlineKeyboard()
        .add(InlineButton("💼 Я бізнесмен", callback_data="choice_business_account"))
        .add(InlineButton("📦 Я постачальник", callback_data="choice_supplier_account"))
    ).get_markup()
