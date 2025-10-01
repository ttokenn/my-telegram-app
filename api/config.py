# /api/config.py

import os

# Загружаем переменные из окружения Vercel
BOT_TOKEN = os.environ.get("BOT_TOKEN", "YOUR_FALLBACK_TOKEN")
WEB_APP_URL = os.environ.get("WEB_APP_URL", "https://yourapp.vercel.app")

# Добавьте сюда все остальные переменные:
# CRYPTO_TOKEN = os.environ.get("CRYPTO_TOKEN")
# и т.д.