from aiogram.dispatcher.filters.state import State, StatesGroup

class Registration(StatesGroup):
    region = State()
    test = State()
    test2 = State()
    son = State()
    full_name = State()
    age = State()
    phone = State()
    manzil = State()
    confirm = State()


