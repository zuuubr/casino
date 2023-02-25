import math
from config.bot_config import dp, bot
from aiogram import types
from Games.apples import GameApple
from keyboards.apple.user_keyboards import map_keyboard

obj = None


@dp.message_handler(commands=['apples'])
async def apples(message: types.Message):
    global obj
    obj = GameApple(10)

    obj.get_map(3, 10)
    obj.active_map(obj.map)

    await bot.send_message(chat_id=message.from_user.id,
                           text=f"Депозит: {obj.deposit} рублей\n"
                                f"Уровень: {obj.level + 1}\n"
                                f"Выигрыш: {round(bool(obj.level) * obj.deposit * math.exp(0.2 * obj.level - 0.2), 3)} рублей\n\n"
                                f"Нажмите на ячейку, чтобы ее открыть.\n"
                                f"Удачи!",
                           reply_markup=map_keyboard(obj.show_map))


    @dp.callback_query_handler(text="left_btn")
    async def left_btn(callback_query: types.CallbackQuery):
        global obj

        if obj.map[0 + obj.level * 3].type == "🍏":
            obj.level = obj.level + 1
            obj.active_map(obj.map)

            await bot.delete_message(chat_id=callback_query.from_user.id,
                                     message_id=callback_query.message.message_id)
            await bot.send_message( chat_id=callback_query.from_user.id,
                                    text=f"Депозит: {obj.deposit} рублей\n"
                                         f"Уровень: {obj.level + 1}\n"
                                         f"Выигрыш: {round(bool(obj.level) * obj.deposit * math.exp(0.2 * obj.level - 0.2), 3)} рублей\n\n"
                                         f"Нажмите на ячейку, чтобы ее открыть.\n"
                                         f"Удачи!",
                                    reply_markup=map_keyboard(obj.show_map))


    @dp.callback_query_handler(text="middle_btn")
    async def left_btn(callback_query: types.CallbackQuery):
        global obj

        if obj.map[1 + obj.level * 3].type == "🍏":
           obj.level = obj.level + 1
           obj.active_map(obj.map)

        await bot.delete_message(chat_id=callback_query.from_user.id,
                                     message_id=callback_query.message.message_id)
        await bot.send_message( chat_id=callback_query.from_user.id,
                                    text=f"Депозит: {obj.deposit} рублей\n"
                                         f"Уровень: {obj.level + 1}\n"
                                         f"Выигрыш: {round(bool(obj.level) * obj.deposit * math.exp(0.2 * obj.level - 0.2), 3)} рублей\n\n"
                                         f"Нажмите на ячейку, чтобы ее открыть.\n"
                                         f"Удачи!",
                                    reply_markup=map_keyboard(obj.show_map))


    @dp.callback_query_handler(text="right_btn")
    async def left_btn(callback_query: types.CallbackQuery):
        global obj

        if obj.map[2 + obj.level * 3].type == "🍏":
            obj.level = obj.level + 1
            obj.active_map(obj.map)

        await bot.delete_message(chat_id=callback_query.from_user.id,
                                 message_id=callback_query.message.message_id)
        await bot.send_message( chat_id=callback_query.from_user.id,
                                text=f"Депозит: {obj.deposit} рублей\n"
                                     f"Уровень: {obj.level + 1}\n"
                                     f"Выигрыш: {round(bool(obj.level) * obj.deposit * math.exp(0.2 * obj.level - 0.2), 3)} рублей\n\n"
                                     f"Нажмите на ячейку, чтобы ее открыть.\n"
                                     f"Удачи!",
                                reply_markup=map_keyboard(obj.show_map))
