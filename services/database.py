from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Base, Feedback
from sqlalchemy.exc import SQLAlchemyError

class Database:
    def __init__(self, db_url: str = "postgresql://feedback_user:24101968h@localhost/telegram_feedback"):
        self.db_url = db_url
        self.engine = create_engine(self.db_url, echo=True)
        self.Session = sessionmaker(bind=self.engine)
        
        # Создаем таблицы при инициализации
        Base.metadata.create_all(self.engine)

    def add_feedback(self, feedback_type: str, content: str):
        """Добавление отзыва в базу данных."""
        try:
            with self.Session() as session:
                new_feedback = Feedback(feedback_type=feedback_type, content=content)
                session.add(new_feedback)
                session.commit()
        except SQLAlchemyError as e:
            print(f"Ошибка при добавлении отзыва: {e}")

    def get_feedbacks(self):
        """Получение всех отзывов из базы данных."""
        try:
            with self.Session() as session:
                feedbacks = session.query(Feedback).all()
                return feedbacks
        except SQLAlchemyError as e:
            print(f"Ошибка при получении отзывов: {e}")
            return []

    def close(self):
        """Закрытие соединений с базой данных."""
        self.engine.dispose()  # Освобождаем все соединения с базой данных






