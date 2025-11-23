import os
from aiogram import Bot, Dispatcher

bot = Bot(os.getenv("BOT_KEY"))
dp = Dispatcher()
