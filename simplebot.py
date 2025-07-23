    # Бот на Aiogram
    # https://surik00.gitbooks.io/aiogram-lessons/content/chapter1.html
    token = '8095624904:AAEe-QN1OJdRwgYvl4H7Nkb-e_bSw3N83T8'

    import telebot
    from telebot import types

    bot = telebot.TeleBot(token)

    @bot.message_handler(commands=['start'])
    def start_message(message):
        bot.send_message(message.chat.id,
                         'Я запущен и буду повторять за Вами')

    @bot.message_handler(content_types=['text'])
    def parrot(message):
        bot.send_message(message.chat.id, message.text)

    bot.infinity_polling(none_stop=True)