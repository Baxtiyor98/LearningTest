from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher.storage import FSMContext
from aiogram.types.message import ContentTypes
from states.states import Registration

from loader import dp


@dp.message_handler(CommandStart(),state='*')
async def bot_start(message: types.Message):
    # await message.answer(f"Salom, {message.from_user.full_name}!\n👉 Youtube: <a href='https://youtu.be/Ui91xOcFVmk'>Tashrif buyurish</a>")
    await message.answer("Assalom alaykum, to'liq ism familyangizni kiriting!!!")
    await Registration.full_name.set()

@dp.message_handler(content_types=ContentTypes.TEXT, state=Registration.full_name)
async def get_full_name(message: types.Message, state: FSMContext):
    await message.answer("Telefon nomeringizni kiriting!!!")
    await state.update_data({'full_name': message.text})
    await Registration.phone.set()

@dp.message_handler(content_types=ContentTypes.CONTACT, state=Registration.phone)
async def get_contact(message: types.Message, state: FSMContext):
    await message.answer("Yoshingizni kiriting!!!")
    await state.update_data({'phone': message.contact.phone_number})
    await Registration.age.set()

@dp.message_handler(content_types=ContentTypes.TEXT, state=Registration.age)
async def get_age(message: types.Message, state: FSMContext):
    await message.answer("Siz ro'yhatdan o'tdizngiz")
    await state.update_data({'age': message.text})
    data = await state.get_data()
    print(data)
    await message.answer(f"Siz kiritgan malumotlar:\nIsm: {data['full_name']}\nTel: {data['phone']}\nYosh: {data['age']}")
    await state.finish()




