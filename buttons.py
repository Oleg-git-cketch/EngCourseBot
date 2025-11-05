from telebot import types

def choose_course_buttons():
    kb = types.InlineKeyboardMarkup()

    but1 = types.InlineKeyboardButton('Beginner', callback_data='beginner')
    but2 = types.InlineKeyboardButton('Elementary', callback_data='elementary')
    but3 = types.InlineKeyboardButton('Pre-intermediate', callback_data='pre_intermediate')
    but4 = types.InlineKeyboardButton('Intermediate', callback_data='intermediate')
    but5 = types.InlineKeyboardButton('Upper-Intermediate', callback_data='upper_intermediate')
    but6 = types.InlineKeyboardButton('Advanced', callback_data='advanced')


    kb.add(but1, but2, but3, but4, but5, but6)

    return kb

def one_button(link):
    kb = types.InlineKeyboardMarkup()

    but1 = types.InlineKeyboardButton('Ссылка', url=link)

    kb.add(but1)

    return kb