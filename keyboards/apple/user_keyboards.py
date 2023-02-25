from aiogram import types

user_answer = types.ReplyKeyboardMarkup()
disagree = types.KeyboardButton("Вернуться назад")
agree = types.KeyboardButton("Продолжить")
user_answer.row(disagree, agree)


def map_keyboard(show_map):

    map = types.InlineKeyboardMarkup()

    for y in range(10):
        cell_button_0 = types.InlineKeyboardButton(text=show_map[0 + y * 3], callback_data=f"cell_button_{0}_{y}")
        cell_button_1 = types.InlineKeyboardButton(text=show_map[1 + y * 3], callback_data=f"cell_button_{1}_{y}")
        cell_button_2 = types.InlineKeyboardButton(text=show_map[2 + y * 3], callback_data=f"cell_button_{2}_{y}")
        map.row(cell_button_0, cell_button_1, cell_button_2)

    left_button = types.InlineKeyboardButton(text="⬅", callback_data="left_btn")
    middle_button = types.InlineKeyboardButton(text="⬆", callback_data="middle_btn")
    right_button = types.InlineKeyboardButton(text="➡", callback_data="right_btn")
    map.row(left_button, middle_button, right_button)

    return map
