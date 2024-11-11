# models.py
from sqlalchemy import Column, Integer, String, Text, TIMESTAMP, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime

# Определяем базовый класс модели
Base = declarative_base()

# Определяем модель для таблицы feedback
class Feedback(Base):
    __tablename__ = 'feedback'

    id = Column(Integer, primary_key=True)
    feedback_type = Column(String(50), nullable=False)
    content = Column(Text, nullable=False)
    created_at = Column(TIMESTAMP, default=datetime.datetime.utcnow)

# Настройка соединения с базой данных
DATABASE_URL = "postgresql://feedback_user:24101968h@localhost/telegram_feedback"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

# Создаем таблицы (если их нет)
Base.metadata.create_all(engine)
