import os
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from bot.main import bot

from contextlib import asynccontextmanager
from dotenv import load_dotenv

from routes import main_routers

load_dotenv()

@asynccontextmanager
async def lifespan(app: FastAPI):
    webhook = f"https://{os.getenv('WEBHOOK_URL')}/webhook"
    await bot.set_webhook(webhook)
    print(f"Webhook set → {webhook}")

    yield

    await bot.delete_webhook()
    await bot.session.close()
    print("Webhook deleted and bot session closed.")

app = FastAPI(
    title="Vercel + FastAPI",
    description="Vercel + FastAPI",
    version="1.0.0",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://create-react-app-rust-seven-80.vercel.app"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(main_routers)