from config.bot_config import dp
from aiogram import executor
from handlers.apple.user_handlers import *
from handlers.find_money.user_handlers_find_money import *
from handlers.black_jack.black_jack_handlers import *
from keyboards import *


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
