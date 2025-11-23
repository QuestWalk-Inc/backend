from fastapi import HTTPException, APIRouter, Request
from aiogram import types

from bot.main import dp, bot
from services import users

main_routers = APIRouter()

@main_routers.post("/webhook")
async def telegram_webhook(request: Request):
    data = await request.json()
    update = types.Update(**data)
    await dp.feed_update(bot, update)
    return {"ok": True}

@main_routers.get("/api/users/{telegram_id}")
def get_user_telegram_id(telegram_id: str):
    response = users.service.get_user(telegram_id)

    if len(response) == 0:
        raise HTTPException(status_code=404, detail="User not found")

    return response[0]