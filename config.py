import os
from dotenv import load_dotenv

# Загружаем переменные окружения из .env файла
load_dotenv()

class Config:
    BOT_TOKEN = os.getenv("BOT_TOKEN")
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_HOST = os.getenv("DB_HOST", "localhost")  # По умолчанию локальный хост
    DB_NAME = os.getenv("DB_NAME", "feedback_bot")
    ADMIN_ID = os.getenv("ADMIN_ID")
    

