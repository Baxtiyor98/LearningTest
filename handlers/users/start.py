from aiogram import types
from aiogram.types import CallbackQuery
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher.storage import FSMContext
from aiogram.types.message import ContentTypes
from aiogram.types import ReplyKeyboardRemove
from keyboards.default.regKey import contact,location,bolim,back
from states.states import Registration
from utils.db_api.database import DB_Commands

from loader import dp

db = DB_Commands()


@dp.message_handler(CommandStart(),state='*')
async def bot_start(message: types.Message):
    await message.answer("Assalom alaykum, to'liq ism familyangizni kiriting!!!")
    await Registration.full_name.set()

@dp.callback_query_handler(state=Registration.region)
async def get_full_name(call: CallbackQuery, state: FSMContext):
    # print(call.data.split('_')[1],call.message)
    if call.data == 'Ortga':
        await call.message.answer("To'liq ism familyangizni kiriting!!!")
        await Registration.full_name.set()
        await call.message.delete()
        return ''
    await call.answer(f"Siz {call.data.split('_')[1]}ni tanladingiz",show_alert=True)
    # await call.answer(f"Siz {call.data.split('_')[1]}ni tanladingiz",show_alert=True)
    await state.update_data({'region': call.data})
    await call.message.delete()
    await call.message.answer("Telefon nomeringizni kiriting!!!",reply_markup=contact)
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



