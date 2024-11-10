from aiogram.fsm.state import StatesGroup, State

class FeedbackStates(StatesGroup):
    waiting_for_like_feedback = State()
    waiting_for_suggestion_feedback = State()

