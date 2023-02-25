from aiogram import types


start_game_menu = types.InlineKeyboardMarkup()
come_back_to_menu_button = types.InlineKeyboardButton(text="🔙Вернуться назад", callback_data="come_back_to_menu")
start_game_button = types.InlineKeyboardButton(text="▶️Начать игру", callback_data="start_game")
start_game_menu.row(come_back_to_menu_button, start_game_button)


stop_hit_bet = types.InlineKeyboardMarkup()
stop_bet_button = types.InlineKeyboardButton(text="Остановиться", callback_data="stop_bet_button")
hit_bet_button = types.InlineKeyboardButton(text="Добавить", callback_data="hit_bet_button")
stop_hit_bet.row(stop_bet_button, hit_bet_button)
