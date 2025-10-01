# /api/utils/database.py

import aiosqlite

DB_PATH = "database.db" # Vercel создаст этот файл

async def setup_database():
    # Ваша функция для создания таблиц, если их нет
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("""
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY,
                balance REAL DEFAULT 0.0
            )
        """)
        await db.commit()

async def get_user_profile(user_id: int):
    # Пример функции, которую будет вызывать API
    async with aiosqlite.connect(DB_PATH) as db:
        cursor = await db.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))
        return await cursor.fetchone()

# ... добавьте сюда все остальные ваши функции для работы с БД