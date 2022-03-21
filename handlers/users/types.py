from aiogram import types
from aiogram.types.message import ContentTypes

from loader import dp

@dp.message_handler(content_types=ContentTypes.TEXT)
async def mesg(message: types.Message):
    await message.answer(f"{message}")

@dp.message_handler(content_types=ContentTypes.VOICE)
async def audio(message: types.Message):
    await message.answer(f"{message}")

@dp.message_handler(content_types=ContentTypes.AUDIO)
async def audio(message: types.Message):
    await message.answer(f"{message.audio.as_json()}")

@dp.message_handler(content_types=ContentTypes.CONTACT)
async def audio(message: types.Message):
    await message.answer(f"{message.contact.phone_number}")

@dp.message_handler(content_types=ContentTypes.ANIMATION)
async def audio(message: types.Message):
    await message.answer(f"{message}")

@dp.message_handler(content_types=ContentTypes.ANY)
async def audio(message: types.Message):
    await message.answer(f"{message}")