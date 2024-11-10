import logging
import atexit
from aiogram import Bot, Dispatcher
from config import Config
from handlers import start_handler, feedback_handler, admin_handler
from services.database import db

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("bot.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

bot = Bot(token=Config.BOT_TOKEN)
dp = Dispatcher()

dp.include_router(start_handler.router)
dp.include_router(feedback_handler.router)
dp.include_router(admin_handler.router)

# Автоматическое закрытие базы данных при завершении работы бота
atexit.register(db.close)

if __name__ == "__main__":
    logger.info("Запуск бота")
    dp.run_polling(bot)

