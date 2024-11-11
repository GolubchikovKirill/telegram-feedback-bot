from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext
from services.database import Database
from services.state import FeedbackStates
from config import Config
import logging

router = Router()
db = Database()  # Подключение к базе данных

# Логирование
logger = logging.getLogger(__name__)

@router.message(F.text == "Что понравилось")
async def feedback_like(message: types.Message, state: FSMContext):
    await message.answer("Напишите, что вам понравилось:")
    await state.set_state(FeedbackStates.waiting_for_like_feedback)

@router.message(F.text == "Что можно добавить")
async def feedback_suggestion(message: types.Message, state: FSMContext):
    await message.answer("Напишите, что можно добавить:")
    await state.set_state(FeedbackStates.waiting_for_suggestion_feedback)

@router.message(FeedbackStates.waiting_for_like_feedback)
async def handle_like_feedback(message: types.Message, state: FSMContext):
    text = message.text
    try:
        db.add_feedback("Понравилось", text)  # Сохраняем отзыв в базе данных
        await message.answer("Благодарим за обратную связь!")
        admin_message = f"Новый отзыв 'Понравилось': {text}"
        await message.bot.send_message(Config.ADMIN_ID, admin_message)
    except Exception as e:
        logger.error(f"Ошибка при сохранении отзыва: {e}")
        await message.answer("Произошла ошибка при сохранении вашего отзыва. Попробуйте позже.")
    finally:
        await state.clear()

@router.message(FeedbackStates.waiting_for_suggestion_feedback)
async def handle_suggestion_feedback(message: types.Message, state: FSMContext):
    text = message.text
    try:
        db.add_feedback("Добавить", text)  # Сохраняем отзыв в базе данных
        await message.answer("Благодарим!")
        admin_message = f"Новый отзыв 'Добавить': {text}"
        await message.bot.send_message(Config.ADMIN_ID, admin_message)
    except Exception as e:
        logger.error(f"Ошибка при сохранении отзыва: {e}")
        await message.answer("Произошла ошибка при сохранении вашего отзыва. Попробуйте позже.")
    finally:
        await state.clear()
