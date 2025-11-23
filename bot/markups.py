from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

launch_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(
        text="Launch QuestWalk",
        web_app=WebAppInfo(url="https://questwalk.vercel.app/")
    )]
])