from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from aiogram.filters import Command
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TELEGRAM_TOKEN")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")

bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("مرحباً بك في بوت القصص! 📚")

async def on_startup():
    if WEBHOOK_URL:
        await bot.set_webhook(WEBHOOK_URL)

if __name__ == "__main__":
    from aiogram.webhook.aiohttp_server import SimpleRequestHandler
    from aiohttp import web
    
    app = web.Application()
    app.router.add_get("/health", lambda r: web.Response(text="OK"))
    SimpleRequestHandler(dp, bot=bot).register(app, path="/webhook")
    
    web.run_app(app, host="0.0.0.0", port=int(os.getenv("PORT", 8000)))
