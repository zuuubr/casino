from aiogram import types


def map_keyboards_find_money(show_map):

    map = types.InlineKeyboardMarkup()

    for y in range(3):
        cell_button_0 = types.InlineKeyboardButton(text=show_map[0 + y * 3], callback_data=f"cell_button_{0}_{y}")
        cell_button_1 = types.InlineKeyboardButton(text=show_map[1 + y * 3], callback_data=f"cell_button_{1}_{y}")
        cell_button_2 = types.InlineKeyboardButton(text=show_map[2 + y * 3], callback_data=f"cell_button_{2}_{y}")
        map.row(cell_button_0, cell_button_1, cell_button_2)

    return map
