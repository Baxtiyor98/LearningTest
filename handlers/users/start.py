from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher.storage import FSMContext
from aiogram.types.message import ContentTypes
from aiogram.types import ReplyKeyboardRemove
from keyboards.default.regKey import contact,location,bolim,back
from states.states import Registration

from loader import dp


@dp.message_handler(CommandStart(),state='*')
async def bot_start(message: types.Message):
    # await message.answer(f"Salom, {message.from_user.full_name}!\n👉 Youtube: <a href='https://youtu.be/Ui91xOcFVmk'>Tashrif buyurish</a>")
    # await message.answer("Assalom alaykum, to'liq ism familyangizni kiriting!!!",reply_markup=bolim())
    await message.answer("Assalom alaykum, to'liq ism familyangizni kiriting!!!")
    await Registration.full_name.set()

@dp.message_handler(content_types=ContentTypes.TEXT, state=Registration.full_name)
async def get_full_name(message: types.Message, state: FSMContext):
    # a = await message.answer('salom')
    # await a.delete()
    await message.answer("Telefon nomeringizni kiriting!!!",reply_markup=contact)
    await state.update_data({'full_name': message.text})
    await message.delete()
    await Registration.phone.set()

@dp.message_handler(content_types=ContentTypes.TEXT, state=Registration.phone)
@dp.message_handler(content_types=ContentTypes.CONTACT, state=Registration.phone)
async def get_contact(message: types.Message, state: FSMContext):
    if message.text == '◀️Ortga':
        await message.answer("To'liq ism familyangizni kiriting!!!",reply_markup=ReplyKeyboardRemove())
        await Registration.full_name.set()
        return ''
    await message.answer("Yoshingizni kiriting!!!",reply_markup=back)
    await state.update_data({'phone': message.contact.phone_number})
    await message.delete()
    await Registration.age.set()

@dp.message_handler(content_types=ContentTypes.TEXT, state=Registration.age)
async def get_age(message: types.Message, state: FSMContext):
    if message.text == '◀️Ortga':
        await message.answer("Telefon nomeringizni kiriting!!!",reply_markup=contact)
        await Registration.phone.set()
        return ''
    await message.answer("Lokatsiya yuboring!",reply_markup=location)
    await state.update_data({'age': message.text})
    await Registration.manzil.set()

@dp.message_handler(content_types=ContentTypes.TEXT, state=Registration.manzil)
@dp.message_handler(content_types=ContentTypes.LOCATION, state=Registration.manzil)
async def get_contact(message: types.Message, state: FSMContext):
    if message.text == '◀️Ortga':
        await message.answer("Yoshingizni kiriting!!!",reply_markup=back)
        await Registration.age.set()
        return ''
    if message.text == 'Link':
        await message.answer(f"👉Youtube: <a href='https://youtu.be/Ui91xOcFVmk'>Tashrif buyurish</a>")
        return ''
    await state.update_data({'location': f"{message.location.latitude},{message.location.longitude}"})
    data = await state.get_data()
    await message.answer(f"Siz kiritgan malumotlar:\nIsm: {data['full_name']}\nTel: {data['phone']}\nYosh: {data['age']}\nKoordinata: {data['location']}",reply_markup=ReplyKeyboardRemove())
    await state.finish()



