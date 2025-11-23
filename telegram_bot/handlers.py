from aiogram import types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

from telegram_bot.loader import dp
from supabase_connection import supabase_client


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    telegram_id = message.from_user.id
    username = message.from_user.username

    # Проверяем в Supabase
    existing = supabase_client.table("users").select("*").eq("telegram_id", telegram_id).execute()

    if not existing.data:
        supabase_client.table("users").insert({
            "telegram_id": telegram_id,
            "username": username
        }).execute()

        response_text = "Welcome! Your account has been created!"
    else:
        response_text = "Welcome back!"

    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(
            text="Launch QuestWalk",
            web_app=WebAppInfo(url="https://create-react-app-rust-seven-80.vercel.app")
        )]
    ])

    await message.answer(response_text, reply_markup=kb)
