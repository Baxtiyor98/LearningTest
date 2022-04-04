import logging

from aiogram import Dispatcher

from data.config import ADMINS

from .db_api.database import create_db

async def on_startup_notify(dp: Dispatcher):
    await create_db()
    for admin in ADMINS:
        try:
            await dp.bot.send_message(admin, "Bot ishga tushdi")

        except Exception as err:
            logging.exception(err)