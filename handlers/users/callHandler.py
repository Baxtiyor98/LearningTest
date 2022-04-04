from aiogram.types import CallbackQuery

from keyboards.inline.regionKey import viloyat, sonlar, jins, confirm
from aiogram import types
from aiogram.dispatcher.storage import FSMContext
from aiogram.types.message import ContentTypes
from states.states import Registration
from loader import dp


@dp.message_handler(content_types=ContentTypes.TEXT,state=Registration.full_name)
async def bot_start1(message: types.Message,state: FSMContext):
    await message.answer("Viloyatingizni tanlang!",reply_markup=viloyat)
    await state.update_data({'full_name': message.text})
    await Registration.test.set()

@dp.callback_query_handler(state=Registration.test)
async def bot_start2(call: CallbackQuery,state: FSMContext):
    print(call.data)
    if call.data == 'back':
        await call.message.answer("To'liq ism familyangizni kiriting!!!")
        await Registration.full_name.set()
        await call.message.delete()
        return ''
    elif call.data == 'next':
        await call.message.answer("Yoqtirgan raqamingizni tanlang tanlang!",reply_markup=sonlar)
        await Registration.son.set()
        await call.message.delete()
        return ''
    await call.answer(f"Siz {call.data.split('_')[1]}ni tanladingiz", show_alert=False)
    await call.message.answer("Yoqtirgan raqamingizni tanlang tanlang!",reply_markup=sonlar)
    await state.update_data({'viloyat': call.data.split('_')[0]})
    await call.message.delete()
    await Registration.son.set()

@dp.callback_query_handler(state=Registration.son)
async def son(call: CallbackQuery,state: FSMContext):
    print(call.data,1)
    if call.data == 'back':
        # await call.message.delete()
        await call.message.edit_text('salom',reply_markup=viloyat)
        await Registration.test.set()
        return ''
    await call.answer(f"Siz {call.data}ni tanladingiz", show_alert=False)
    await call.message.answer('Jinsingizni tanlang!',reply_markup=jins)
    await state.update_data({'like': call.data.split('_')[1]})
    await call.message.delete()
    await Registration.test2.set()

@dp.callback_query_handler(state=Registration.test2)
async def bot_start2(call: CallbackQuery,state: FSMContext):
    print(call.data)
    if call.data == 'back':
        await call.message.answer('Yoqtirgan raqamingizni tanlang!',reply_markup=viloyat)
        await call.message.delete()
        await Registration.test2.set()
        return ''
    await state.update_data({'jins': call.data})
    await call.message.delete()
    data = await state.get_data()
    await call.message.answer(f"Ism: {data['full_name']}\nViloyat: {data['viloyat']}\nSon: {data['like']}\nJins: {data.get('jins')}",reply_markup=confirm)
    await Registration.confirm.set()

@dp.callback_query_handler(state=Registration.confirm)
async def bot_start3(call: CallbackQuery,state: FSMContext):
    print(call.data)
    if call.data == '1':
        await call.answer("Qabul qilindi",show_alert=False)
        await call.message.delete()
        await state.finish()
        return ''
    elif call.data == '0':
        await call.message.delete()
        await call.message.answer("To'liq ism familyangizni kiriting!!!")
        await Registration.full_name.set()
        return ''
