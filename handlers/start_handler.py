from aiogram import Router, types, F
from keyboards.feedback_keyboard import feedback_keyboard

router = Router()

@router.message(F.text == "/start")
async def start_command(message: types.Message):
    await message.answer(
        "Привет! Я бот для сбора обратной связи. Выберите один из вариантов:",
        reply_markup=feedback_keyboard()
    )


