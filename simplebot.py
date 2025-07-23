# Бот на Aiogram
# https://surik00.gitbooks.io/aiogram-lessons/content/chapter1.html
token = '8095624904:AAEe-QN1OJdRwgYvl4H7Nkb-e_bSw3N83T8'

import telebot
from telebot import types

bot = telebot.TeleBot(token)

kb = types.ReplyKeyboardMarkup(row_width=2)
btn1 = types.KeyboardButton('/url')
btn2 = types.KeyboardButton('/help')
btn3 = types.KeyboardButton('Как дела?')
kb.add(btn1, btn2, btn3)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,
                     'Я запущен и буду повторять за Вами',
                     reply_markup=kb)


@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(message.chat.id,
                     'Я пока всего лишь ваше эхо и умею немного!')


@bot.message_handler(commands=['url'])
def url_message(message):
    markup = types.InlineKeyboardMarkup()
    btn = types.InlineKeyboardButton(text='Сайт Яндекса', url='https://ya.ru')
    markup.add(btn)
    bot.send_message(message.chat.id, 'Перейти на сайт Яндекса',
                     reply_markup=markup)


@bot.message_handler(content_types=['text'])
def parrot(message):
    if message.text.strip().lower() == 'привет':
        bot.send_message(message.chat.id, 'Ну, здорово!!! 👏')
    elif message.text.strip().lower() == 'как дела?':
        # bot.send_message(message.chat.id, '👍')
        answer = types.InlineKeyboardMarkup(row_width=2)
        btn_good = types.InlineKeyboardButton('Хорошо', callback_data='good')
        btn_bad = types.InlineKeyboardButton('Плохо', callback_data='bad')
        answer.add(btn_good, btn_bad)
        bot.send_message(message.chat.id, 'У меня то хорошо, а у тебя',
                         reply_markup=answer)
    else:
        bot.send_message(message.chat.id, message.text)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == 'good':
        bot.send_message(call.message.chat.id, 'О, круто, рад!!!')
    if call.data == 'bad':
        bot.send_message(call.message.chat.id, 'Не переживай, всё наладится!!!')


bot.infinity_polling(none_stop=True)