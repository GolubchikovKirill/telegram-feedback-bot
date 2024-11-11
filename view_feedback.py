from services.database import Database
from services.models import Feedback

# Создаем экземпляр базы данных
db = Database()

# Получаем все отзывы
feedbacks = db.get_feedbacks()

# Выводим данные
for feedback in feedbacks:
    print(f"ID: {feedback.id}, Тип: {feedback.feedback_type}, Отзыв: {feedback.content}")
