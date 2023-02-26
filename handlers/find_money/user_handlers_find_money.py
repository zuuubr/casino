from config.bot_config import dp, bot
from aiogram import types
from Games.find_money import GameFindMoney
from keyboards.find_money.user_keyboards_find_money import map_keyboards_find_money

obj = None
count_repeat = 0
nums = []


@dp.message_handler(commands=['find_money'])
async def find_money(message: types.Message):
    global obj, count_repeat, nums
    count_repeat = 0
    nums.clear()
    obj = GameFindMoney(10)

    obj.get_map(3, 3)
    obj.active_map(3, 3)

    await bot.send_message(chat_id=message.from_user.id,
                           text=f"Депозит: {obj.deposit} рублей\n"
                                f"Нажмите на ячейку, чтобы ее открыть.\n"
                                f"Удачи!",
                           reply_markup=map_keyboards_find_money(obj.show_map))

    @dp.callback_query_handler(text="cell_button_0_0")
    async def left_btn(callback_query: types.CallbackQuery):

        obj.show_map[0 + 0 * 3] = obj.map[0 + 0 * 3].type

        await bot.delete_message(chat_id=callback_query.from_user.id,
                                 message_id=callback_query.message.message_id)
        await bot.send_message(chat_id=callback_query.from_user.id,
                               text=f"Депозит: {obj.deposit} рублей\n"
                                    f"Нажмите на ячейку, чтобы ее открыть.\n"
                                    f"Удачи!",
                               reply_markup=map_keyboards_find_money(obj.show_map))

        nums.append(obj.map[0 + 0 * 3].type)
        if len(nums) == 3:
            buf = nums[0]
            for num in nums:
                if buf != num:
                    await bot.send_message(chat_id=callback_query.from_user.id,
                                           text="Вы проиграли!")
                    return 0
            await bot.send_message(chat_id=callback_query.from_user.id,
                                   text="Вы выиграли!")

    @dp.callback_query_handler(text="cell_button_1_0")
    async def left_btn(callback_query: types.CallbackQuery):

        obj.show_map[1 + 0 * 3] = obj.map[1 + 0 * 3].type

        await bot.delete_message(chat_id=callback_query.from_user.id,
                                 message_id=callback_query.message.message_id)
        await bot.send_message(chat_id=callback_query.from_user.id,
                               text=f"Депозит: {obj.deposit} рублей\n"
                                    f"Нажмите на ячейку, чтобы ее открыть.\n"
                                    f"Удачи!",
                               reply_markup=map_keyboards_find_money(obj.show_map))

        nums.append(obj.map[1 + 0 * 3].type)
        if len(nums) == 3:
            buf = nums[0]
            for num in nums:
                if buf != num:
                    await bot.send_message(chat_id=callback_query.from_user.id,
                                           text="Вы проиграли!")
                    return 0
            await bot.send_message(chat_id=callback_query.from_user.id,
                                   text="Вы выиграли!")

    @dp.callback_query_handler(text="cell_button_2_0")
    async def left_btn(callback_query: types.CallbackQuery):

        obj.show_map[2 + 0 * 3] = obj.map[2 + 0 * 3].type

        await bot.delete_message(chat_id=callback_query.from_user.id,
                                 message_id=callback_query.message.message_id)
        await bot.send_message(chat_id=callback_query.from_user.id,
                               text=f"Депозит: {obj.deposit} рублей\n"
                                    f"Нажмите на ячейку, чтобы ее открыть.\n"
                                    f"Удачи!",
                               reply_markup=map_keyboards_find_money(obj.show_map))

        nums.append(obj.map[2 + 0 * 3].type)
        if len(nums) == 3:
            buf = nums[0]
            for num in nums:
                if buf != num:
                    await bot.send_message(chat_id=callback_query.from_user.id,
                                           text="Вы проиграли!")
                    return 0
            await bot.send_message(chat_id=callback_query.from_user.id,
                                   text="Вы выиграли!")

    @dp.callback_query_handler(text="cell_button_0_1")
    async def left_btn(callback_query: types.CallbackQuery):

        obj.show_map[0 + 1 * 3] = obj.map[0 + 1 * 3].type

        await bot.delete_message(chat_id=callback_query.from_user.id,
                                 message_id=callback_query.message.message_id)
        await bot.send_message(chat_id=callback_query.from_user.id,
                               text=f"Депозит: {obj.deposit} рублей\n"
                                    f"Нажмите на ячейку, чтобы ее открыть.\n"
                                    f"Удачи!",
                               reply_markup=map_keyboards_find_money(obj.show_map))

        nums.append(obj.map[0 + 1 * 3].type)
        if len(nums) == 3:
            buf = nums[0]
            for num in nums:
                if buf != num:
                    await bot.send_message(chat_id=callback_query.from_user.id,
                                           text="Вы проиграли!")
                    return 0
            await bot.send_message(chat_id=callback_query.from_user.id,
                                   text="Вы выиграли!")

    @dp.callback_query_handler(text="cell_button_1_1")
    async def left_btn(callback_query: types.CallbackQuery):

        obj.show_map[1 + 1 * 3] = obj.map[1 + 1 * 3].type

        await bot.delete_message(chat_id=callback_query.from_user.id,
                                 message_id=callback_query.message.message_id)
        await bot.send_message(chat_id=callback_query.from_user.id,
                               text=f"Депозит: {obj.deposit} рублей\n"
                                    f"Нажмите на ячейку, чтобы ее открыть.\n"
                                    f"Удачи!",
                               reply_markup=map_keyboards_find_money(obj.show_map))

        nums.append(obj.map[1 + 1 * 3].type)
        if len(nums) == 3:
            buf = nums[0]
            for num in nums:
                if buf != num:
                    await bot.send_message(chat_id=callback_query.from_user.id,
                                           text="Вы проиграли!")
                    return 0
            await bot.send_message(chat_id=callback_query.from_user.id,
                                   text="Вы выиграли!")

    @dp.callback_query_handler(text="cell_button_2_1")
    async def left_btn(callback_query: types.CallbackQuery):

        obj.show_map[2 + 1 * 3] = obj.map[2 + 1 * 3].type

        await bot.delete_message(chat_id=callback_query.from_user.id,
                                 message_id=callback_query.message.message_id)
        await bot.send_message(chat_id=callback_query.from_user.id,
                               text=f"Депозит: {obj.deposit} рублей\n"
                                    f"Нажмите на ячейку, чтобы ее открыть.\n"
                                    f"Удачи!",
                               reply_markup=map_keyboards_find_money(obj.show_map))

        nums.append(obj.map[2 + 1 * 3].type)
        if len(nums) == 3:
            buf = nums[0]
            for num in nums:
                if buf != num:
                    await bot.send_message(chat_id=callback_query.from_user.id,
                                           text="Вы проиграли!")
                    return 0
            await bot.send_message(chat_id=callback_query.from_user.id,
                                   text="Вы выиграли!")

    @dp.callback_query_handler(text="cell_button_0_2")
    async def left_btn(callback_query: types.CallbackQuery):

        obj.show_map[0 + 2 * 3] = obj.map[0 + 2 * 3].type

        await bot.delete_message(chat_id=callback_query.from_user.id,
                                 message_id=callback_query.message.message_id)
        await bot.send_message(chat_id=callback_query.from_user.id,
                               text=f"Депозит: {obj.deposit} рублей\n"
                                    f"Нажмите на ячейку, чтобы ее открыть.\n"
                                    f"Удачи!",
                               reply_markup=map_keyboards_find_money(obj.show_map))

        nums.append(obj.map[0 + 2 * 3].type)
        if len(nums) == 3:
            buf = nums[0]
            for num in nums:
                if buf != num:
                    await bot.send_message(chat_id=callback_query.from_user.id,
                                           text="Вы проиграли!")
                    return 0
            await bot.send_message(chat_id=callback_query.from_user.id,
                                   text="Вы выиграли!")

    @dp.callback_query_handler(text="cell_button_1_2")
    async def left_btn(callback_query: types.CallbackQuery):

        obj.show_map[1 + 2 * 3] = obj.map[1 + 2 * 3].type

        await bot.delete_message(chat_id=callback_query.from_user.id,
                                 message_id=callback_query.message.message_id)
        await bot.send_message(chat_id=callback_query.from_user.id,
                               text=f"Депозит: {obj.deposit} рублей\n"
                                    f"Нажмите на ячейку, чтобы ее открыть.\n"
                                    f"Удачи!",
                               reply_markup=map_keyboards_find_money(obj.show_map))

        nums.append(obj.map[1 + 2 * 3].type)
        if len(nums) == 3:
            buf = nums[0]
            for num in nums:
                if buf != num:
                    await bot.send_message(chat_id=callback_query.from_user.id,
                                           text="Вы проиграли!")
                    return 0
            await bot.send_message(chat_id=callback_query.from_user.id,
                                   text="Вы выиграли!")

    @dp.callback_query_handler(text="cell_button_2_2")
    async def left_btn(callback_query: types.CallbackQuery):

        obj.show_map[2 + 2 * 3] = obj.map[2 + 2 * 3].type

        await bot.delete_message(chat_id=callback_query.from_user.id,
                                 message_id=callback_query.message.message_id)
        await bot.send_message(chat_id=callback_query.from_user.id,
                               text=f"Депозит: {obj.deposit} рублей\n"
                                    f"Нажмите на ячейку, чтобы ее открыть.\n"
                                    f"Удачи!",
                               reply_markup=map_keyboards_find_money(obj.show_map))

        nums.append(obj.map[2 + 2 * 3].type)
        if len(nums) == 3:
            buf = nums[0]
            for num in nums:
                if buf != num:
                    await bot.send_message(chat_id=callback_query.from_user.id,
                                           text="Вы проиграли!")
                    return 0
            await bot.send_message(chat_id=callback_query.from_user.id,
                                   text="Вы выиграли!")
