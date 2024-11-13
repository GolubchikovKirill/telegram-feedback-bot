# bot.py
import logging
import atexit
from aiogram import Bot, Dispatcher
from config import Config
from handlers import start_handler, feedback_handler, admin_handler
from services.database import Database

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler()  # Убираем запись в файл, т.к. на сервере файловая система доступна только для чтения
    ]
)

logger = logging.getLogger(__name__)

# Создаем объект бота и диспетчера
bot = Bot(token=Config.BOT_TOKEN)
dp = Dispatcher()

# Подключаем обработчики
dp.include_router(start_handler.router)
dp.include_router(feedback_handler.router)
dp.include_router(admin_handler.router)

# Инициализируем подключение к базе данных
db = Database()

# Автоматическое закрытие базы данных при завершении работы бота
atexit.register(db.close)

if __name__ == "__main__":
    logger.info("Запуск бота")
    dp.run_polling(bot)


