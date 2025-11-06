import os

import telebot
from buttons import choose_course_buttons, one_button
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('BOT_TOKEN')
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id

    bot.send_message(user_id, 'Выберите курс', reply_markup=choose_course_buttons())

@bot.callback_query_handler(func=lambda call: call.data in ['beginner', 'elementary', 'pre_intermediate', 'intermediate', 'upper_intermediate', 'advanced'])
def callback(call):
    bot.answer_callback_query(call.id)

    if call.data == 'beginner':

        bot.send_message(call.message.chat.id, 'Beginner audio', reply_markup=one_button('https://t.me/+ZgVqGVoWejw2NjNi'))
        bot.send_message(call.message.chat.id, 'Beginner video', reply_markup=one_button('https://t.me/+ZbXsqs6aj6cxN2Uy'))

    if call.data == 'elementary':

        bot.send_message(call.message.chat.id, 'Elementary audio', reply_markup=one_button('https://t.me/+i39y2WNngXFmM2Yy'))
        bot.send_message(call.message.chat.id, 'Elementary video', reply_markup=one_button('https://t.me/+LxKixadK_mYxMDgy'))

    if call.data == 'pre_intermediate':

        bot.send_message(call.message.chat.id, 'Pre_intermediate audio', reply_markup=one_button('https://t.me/+EQAHWsKgkMRiNTIy'))
        bot.send_message(call.message.chat.id, 'Pre_intermediate video', reply_markup=one_button('https://t.me/+g-A5aWUCkW4zMTIy'))

    if call.data == 'intermediate':

        bot.send_message(call.message.chat.id, 'Intermediate audio', reply_markup=one_button('https://t.me/+Xg8G7wG_aEZiZTBi'))
        bot.send_message(call.message.chat.id, 'Intermediate video', reply_markup=one_button('https://t.me/+8oUE3y4W-aEyZmQy'))

    if call.data == 'upper_intermediate':

        bot.send_message(call.message.chat.id, 'Upper_intermediate audio', reply_markup=one_button('https://t.me/+LLkwBZlEqMxkMDUy'))
        bot.send_message(call.message.chat.id, 'Upper_intermediate video', reply_markup=one_button('https://t.me/+0NSqgFTFIV5jYjFi'))

    if call.data == 'Advanced':

        bot.send_message(call.message.chat.id, 'Advanced audio', reply_markup=one_button('https://t.me/+LLkwBZlEqMxkMDUy'))
        bot.send_message(call.message.chat.id, 'Advanced video', reply_markup=one_button('https://t.me/+KWnhBJhTFTAwNWUy'))

    else:
        return False

bot.polling(none_stop=True)
