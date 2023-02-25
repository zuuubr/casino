from aiogram import types
from config.bot_config import dp, bot
from Games.black_jack import GameBlackJack
from keyboards.black_jack.black_jack_keyboards import start_game_menu, stop_hit_bet

obj_black_jack = None


@dp.message_handler(commands=['black_jack'])
async def black_jack(message: types.Message):
    global obj_black_jack
    obj_black_jack = GameBlackJack(10)

    await bot.send_message(chat_id=message.from_user.id,
                           text="Правила игры: смысл игрового процесса заключается в наборе "
                           "большего числа очков, но не больше двадцати одного.\n"
                           "Если количество очков у дилера и игрока совпадают значит "
                           "никто не проиграл, никто не выиграл.\n"
                           "Номинальные значения карт следующее, от двойки до десятки "
                           "совпадают с номиналом. Валет, дама, король имеют десять очков. "
                           "Туз идет всегда либо одно очко, либо одиннадцать т.е. как будет "
                           "выгодно участнику",
                           reply_markup=start_game_menu)

    @dp.callback_query_handler(text='start_game')
    async def start_game(callback_query: types.CallbackQuery):

        buf = obj_black_jack.get_card()
        obj_black_jack.diller_cards.append(buf[0])
        obj_black_jack.diller_score += buf[1]

        buf = obj_black_jack.get_card()
        obj_black_jack.player_cards.append(buf[0])
        obj_black_jack.player_score += buf[1]

        await bot.delete_message(chat_id=callback_query.from_user.id,
                                 message_id=callback_query.message.message_id)

        await bot.send_message(chat_id=callback_query.from_user.id,
                               text=f"Депозит: {obj_black_jack.deposit} рублей\n"
                               f"Выигрыш: {obj_black_jack.deposit * 2} рублей\n\n"
                               f"Выберите действие. Удачи!")

        await bot.send_message(chat_id=callback_query.from_user.id,
                               text="Диллер:\n"
                               f"Карты: {obj_black_jack.diller_cards}, [❓], ...\n"
                               f"Очки: {obj_black_jack.diller_score}\n\n"
                               f"===========\n\n"
                               f"Игрок:\n"
                               f"Карты: {obj_black_jack.player_cards}\n"
                               f"Очки: {obj_black_jack.player_score}",
                               reply_markup=stop_hit_bet)

    @dp.callback_query_handler(text="hit_bet_button")
    async def hit_button(callback_query: types.callback_query):

        buf = obj_black_jack.get_card()
        obj_black_jack.player_cards.append(buf[0])
        obj_black_jack.player_score += buf[1]

        await bot.delete_message(chat_id=callback_query.from_user.id,
                                 message_id=callback_query.message.message_id)

        await bot.send_message(chat_id=callback_query.from_user.id,
                               text="Диллер:\n"
                                    f"Карты: {obj_black_jack.diller_cards}, [❓], ...\n"
                                    f"Очки: {obj_black_jack.diller_score}\n\n"
                                    f"===========\n\n"
                                    f"Игрок:\n"
                                    f"Карты: {obj_black_jack.player_cards}\n"
                                    f"Очки: {obj_black_jack.player_score}",
                               reply_markup=stop_hit_bet)

    @dp.callback_query_handler(text="stop_bet_button")
    async def stop_button(callback_query: types.callback_query):

        while obj_black_jack.diller_score < obj_black_jack.player_score:
            buf = obj_black_jack.get_card()
            obj_black_jack.diller_cards.append(buf[0])
            obj_black_jack.diller_score += buf[1]

        await bot.delete_message(chat_id=callback_query.from_user.id,
                                 message_id=callback_query.message.message_id)

        await bot.send_message(chat_id=callback_query.from_user.id,
                               text="Диллер:\n"
                                    f"Карты: {obj_black_jack.diller_cards}\n"
                                    f"Очки: {obj_black_jack.diller_score}\n\n"
                                    f"===========\n\n"
                                    f"Игрок:\n"
                                    f"Карты: {obj_black_jack.player_cards}\n"
                                    f"Очки: {obj_black_jack.player_score}")
