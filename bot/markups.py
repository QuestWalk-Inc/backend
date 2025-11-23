from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

launch_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(
        text="Launch QuestWalk",
        web_app=WebAppInfo(url="https://create-react-app-rust-seven-80.vercel.app/")
    )]
])