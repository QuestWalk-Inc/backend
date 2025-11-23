from aiogram import types, Dispatcher
from aiogram.filters import Command


from bot.markups import launch_kb
from services import users

dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    print(f"Handler called! User: {message.from_user.id}")
    telegram_id = message.from_user.id
    username = message.from_user.username
    response_text = "Welcome back!"

    response = users.service.get_user(telegram_id)

    if len(response) == 0:
        users.service.create_user(telegram_id, username)
        response_text = "Welcome! Your account has been created!"

    await message.answer(response_text, reply_markup=launch_kb)

print(f"Handlers registered: {len(dp.message.handlers)}")
