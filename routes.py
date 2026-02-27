from fastapi import HTTPException, APIRouter, Request
from aiogram import types

from bot.handlers import dp
from bot.main import bot
from services import users, supabase_client

main_routers = APIRouter()


@main_routers.post("/webhook")
async def telegram_webhook(request: Request):
    data = await request.json()
    print(f"Received update: {data}")
    update = types.Update(**data)
    await dp.feed_update(bot, update)
    print("Update processed")
    return {"ok": True}


@main_routers.post("/api/trainings")
def create_training(training: dict):
    response = supabase_client.table("trainings").insert(training).execute()

    if not response.data:
        raise HTTPException(status_code=500, detail="Failed to create training")

    return response.data[0]


@main_routers.patch("/api/trainings/{training_id}")
def update_training(training_id: int, training: dict):
    if not training:
        raise HTTPException(status_code=400, detail="No fields provided for update")

    response = (
        supabase_client
        .table("trainings")
        .update(training)
        .eq("id", training_id)
        .execute()
    )

    if not response.data:
        raise HTTPException(status_code=404, detail="Training not found")

    return response.data[0]


@main_routers.delete("/api/trainings/{training_id}")
def delete_training(training_id: int):
    response = (
        supabase_client
        .table("trainings")
        .delete()
        .eq("id", training_id)
        .execute()
    )

    if not response.data:
        raise HTTPException(status_code=404, detail="Training not found")

    return {"detail": "Training deleted"}

@main_routers.get("/api/users/{telegram_id}")
def get_user_telegram_id(telegram_id: str):
    response = users.service.get_user(telegram_id)

    if len(response) == 0:
        raise HTTPException(status_code=404, detail="User not found")

    return response[0]