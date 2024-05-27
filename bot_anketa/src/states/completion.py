from aiogram.fsm.state import State, StatesGroup


class FillingForm(StatesGroup):
    age = State()
    gender = State()
    city = State()
