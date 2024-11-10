from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def feedback_keyboard():
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Что понравилось")],
            [KeyboardButton(text="Что можно добавить")]
        ],
        resize_keyboard=True
    )
    return keyboard


