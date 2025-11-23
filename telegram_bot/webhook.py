from fastapi import APIRouter, Request
from aiogram import types
from telegram_bot.loader import bot, dp

router = APIRouter()

@router.post("/webhook")
async def telegram_webhook(request: Request):
    data = await request.json()
    update = types.Update(**data)
    await dp.feed_update(bot, update)
    return {"ok": True}
