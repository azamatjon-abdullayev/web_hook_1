from aiogram import types
from googletrans import Translator
from loader import dp

tarjimon = Translator()
# Echo bot
@dp.message_handler()
async def bot_echo(message: types.Message):
    til = tarjimon.detect(text=message.text).lang

    if til == 'uz':
        tarjima_qilish = tarjimon.translate(text=message.text, dest='en', src='uz').text
        await message.answer(text=tarjima_qilish)

    if til == 'ru':
        tarjima_qilish = tarjimon.translate(text=message.text, dest='en', src='ru').text
        await message.answer(text=tarjima_qilish)

    if til == 'en':
        tarjima_qilish = tarjimon.translate(text=message.text, dest='uz', src='en').text
        await message.answer(text=tarjima_qilish)