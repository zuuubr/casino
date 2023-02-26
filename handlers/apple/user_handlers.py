import math
from config.bot_config import dp, bot
from aiogram import types
from Games.apples import GameApple
from keyboards.apple.user_keyboards import map_keyboard

object_apple_game = None


@dp.message_handler(commands=['apples'])
async def apples(message: types.Message):
    global object_apple_game
    object_apple_game = GameApple(10)

    object_apple_game.get_map(3, 10)
    object_apple_game.active_map(object_apple_game.map)

    await bot.send_message(chat_id=message.from_user.id,
                           text=f"Депозит: {object_apple_game.deposit} рублей\n"
                                f"Уровень: {object_apple_game.level + 1}\n"
                                f"Выигрыш: {round(bool(object_apple_game.level) * object_apple_game.deposit * math.exp(0.2 * object_apple_game.level - 0.2), 3)} рублей\n\n"
                                f"Нажмите на ячейку, чтобы ее открыть.\n"
                                f"Удачи!",
                           reply_markup=map_keyboard(object_apple_game.show_map))

    @dp.callback_query_handler(text="left_btn")
    async def left_btn(callback_query: types.CallbackQuery):

        if object_apple_game.map[0 + object_apple_game.level * 3].type == "🍏":
            object_apple_game.level = object_apple_game.level + 1
            object_apple_game.active_map(object_apple_game.map)

            await bot.delete_message(chat_id=callback_query.from_user.id,
                                     message_id=callback_query.message.message_id)
            await bot.send_message(chat_id=callback_query.from_user.id,
                                   text=f"Депозит: {object_apple_game.deposit} рублей\n"
                                        f"Уровень: {object_apple_game.level + 1}\n"
                                        f"Выигрыш: {round(bool(object_apple_game.level) * object_apple_game.deposit * math.exp(0.2 * object_apple_game.level - 0.2), 3)} рублей\n\n"
                                        f"Нажмите на ячейку, чтобы ее открыть.\n"
                                        f"Удачи!",
                                   reply_markup=map_keyboard(object_apple_game.show_map))

    @dp.callback_query_handler(text="middle_btn")
    async def left_btn(callback_query: types.CallbackQuery):

        if object_apple_game.map[1 + object_apple_game.level * 3].type == "🍏":
            object_apple_game.level = object_apple_game.level + 1
            object_apple_game.active_map(object_apple_game.map)

        await bot.delete_message(chat_id=callback_query.from_user.id,
                                 message_id=callback_query.message.message_id)
        await bot.send_message(chat_id=callback_query.from_user.id,
                               text=f"Депозит: {object_apple_game.deposit} рублей\n"
                                    f"Уровень: {object_apple_game.level + 1}\n"
                                    f"Выигрыш: {round(bool(object_apple_game.level) * object_apple_game.deposit * math.exp(0.2 * object_apple_game.level - 0.2), 3)} рублей\n\n"
                                    f"Нажмите на ячейку, чтобы ее открыть.\n"
                                    f"Удачи!",
                               reply_markup=map_keyboard(object_apple_game.show_map))

    @dp.callback_query_handler(text="right_btn")
    async def left_btn(callback_query: types.CallbackQuery):

        if object_apple_game.map[2 + object_apple_game.level * 3].type == "🍏":
            object_apple_game.level = object_apple_game.level + 1
            object_apple_game.active_map(object_apple_game.map)

        await bot.delete_message(chat_id=callback_query.from_user.id,
                                 message_id=callback_query.message.message_id)
        await bot.send_message(chat_id=callback_query.from_user.id,
                               text=f"Депозит: {object_apple_game.deposit} рублей\n"
                                    f"Уровень: {object_apple_game.level + 1}\n"
                                    f"Выигрыш: {round(bool(object_apple_game.level) * object_apple_game.deposit * math.exp(0.2 * object_apple_game.level - 0.2), 3)} рублей\n\n"
                                    f"Нажмите на ячейку, чтобы ее открыть.\n"
                                    f"Удачи!",
                               reply_markup=map_keyboard(object_apple_game.show_map))
