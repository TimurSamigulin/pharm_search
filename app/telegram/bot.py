import logging

from app.settings import get_settings
from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

setting = get_settings()

API_TOKEN = setting.telegram_token

DESCRIPTION = (
    """
        Данный бот поможет найти вам ближайщую аптеку с необходимым лекарством
    """
)

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

button_send = KeyboardButton('Найти лекарство')

greet_kb = ReplyKeyboardMarkup(resize_keyboard=True)
greet_kb.add(button_send)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply(DESCRIPTION, reply_markup=greet_kb)

def start_bot():
    executor.start_polling(dp, skip_updates=True) 