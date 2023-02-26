from config.bot_config import dp
from aiogram import executor
from handlers.apple.user_handlers import *
from handlers.find_money.user_handlers_find_money import *
from handlers.black_jack.black_jack_handlers import *
from keyboards import *

# В игре find_money сделать проверку чтобы выбирали не одну и ту же ячейку
# В игре apple сделать проверку на последний уровень + механику победы/проигрыша
# В игре сделать механику победы/проигрыша
# Добавить механику создания ставки
# В каждой игре сделать надпись с правилами


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
