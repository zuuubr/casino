from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import logging
from dotenv import dotenv_values

config = dotenv_values('./config/.env')
API_TOKEN = config['API_TOKEN']

logging.basicConfig(level = logging.INFO)
bot = Bot(token=API_TOKEN)

storage = MemoryStorage()
dp = Dispatcher(bot=bot, storage=storage)
