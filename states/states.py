from aiogram.dispatcher.filters.state import State, StatesGroup

class Registration(StatesGroup):
    full_name = State()
    age = State()
    phone = State()
    manzil = State()


