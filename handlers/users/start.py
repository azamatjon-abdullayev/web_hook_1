from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp


@dp.message_handler(commands='start')
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}! tarjimon botga hush kelibsiz")
