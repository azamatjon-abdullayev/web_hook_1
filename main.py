from fastapi import FastAPI
from loader import bot,dp
from aiogram import types, Dispatcher, Bot
from data.config import BOT_TOKEN

app = FastAPI()
WEBHOOK_PATH=f'/{BOT_TOKEN}/'
WEBHOOK_URL='https://test-bot-4fvr.onrender.com'+WEBHOOK_PATH

@app.on_event('startup')
async def on_startup():
    url = await bot.get_webhook_info()
    if url !=WEBHOOK_URL:
        await bot.set_webhook(
            url=WEBHOOK_URL)

@app.post(WEBHOOK_PATH)
async def bot_webhook(update: dict):
    telegram_update = types.Update(**update)
    Dispatcher.set_current(dp)
    Bot.set_current(bot)
    await dp.process_update(telegram_update)


@app.on_event("shutdown")
async def on_shutdown():
    await bot.get_session()