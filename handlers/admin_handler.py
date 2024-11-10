from aiogram import Router, types, F
from config import Config
from services.database import Database

router = Router()
db = Database()

@router.message(F.text == "/view_feedback")
async def view_feedback(message: types.Message):
    if message.from_user.id != Config.ADMIN_ID:
        await message.answer("У вас нет прав для выполнения этой команды.")
        return

    feedbacks = db.cursor.execute("SELECT type, message FROM feedback").fetchall()
    if not feedbacks:
        await message.answer("Нет доступных отзывов.")
        return

    response = "\n\n".join([f"{f[0]}: {f[1]}" for f in feedbacks])
    await message.answer(response)

