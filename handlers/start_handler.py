#start_handler.py
from aiogram import Router, types, F
from keyboards.feedback_keyboard import feedback_keyboard

router = Router()

@router.message(F.text == "/start")
async def start_command(message: types.Message):
    await message.answer(
        "<b>Уважаемые студенты! Я кот <s>бот</s> для сбора и обработки обратной связи. "
        "Выберите один из вариантов на панели:</b>",
        parse_mode="HTML",
        reply_markup=feedback_keyboard()
    )







