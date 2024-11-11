from aiogram import Router, types, F
from keyboards.feedback_keyboard import feedback_keyboard

router = Router()

@router.message(F.text == "/start")
async def start_command(message: types.Message):
    await message.answer(
        "Уважаемые студенты! Я бот для получения и обработки обратной связи. Выберите один из вариантов на панели:",
        reply_markup=feedback_keyboard()
    )


