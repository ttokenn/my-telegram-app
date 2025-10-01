# /api/index.py

from fastapi import FastAPI, Request
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo

# Импортируем конфиги и утилиты
from .config import BOT_TOKEN, WEB_APP_URL
from .utils import database

# --- Настройка Aiogram ---
bot = Bot(token=BOT_TOKEN, parse_mode="HTML")
dp = Dispatcher()

# --- Логика FastAPI ---
app = FastAPI()

# --- Aiogram хэндлеры ---
@dp.message(commands=["start"])
async def start_handler(message: types.Message):
    # Пример добавления пользователя в БД при старте
    await database.setup_database() # Убедимся, что таблицы созданы

    keyboard = ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text="🚀 Открыть магазин", web_app=WebAppInfo(url=WEB_APP_URL))]],
        resize_keyboard=True
    )
    await message.answer(
        "<b>🎉 Добро пожаловать!</b>\n\nНажмите кнопку ниже, чтобы открыть наш магазин.",
        reply_markup=keyboard
    )

# --- Эндпоинты ---
@app.post("/api/webhook")
async def telegram_webhook(update: dict):
    # Обрабатываем входящие обновления от Telegram
    await dp.feed_webhook_update(bot=bot, update=update)

@app.get("/api/profile/{user_id}")
async def get_user_profile_api(user_id: int):
    # Пример API-эндпоинта для вашего фронтенда
    user_data = await database.get_user_profile(user_id)
    if user_data:
        return {"user_id": user_data[0], "balance": user_data[1]}
    return {"error": "User not found"}, 404