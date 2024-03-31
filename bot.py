import telebot
import config
import replies
import random

from telebot import types

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def start_reply(message):
    
    main_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Нужен совет!")
    item2 = types.KeyboardButton("Сделай предсказание!")

    main_markup.add(item1, item2)

    bot.send_message(message.chat.id, "Привет! Я — котенька Масюня! Рада познакомиться! Пока что я умею немногое, но буду рада помочь, чем смогу!", reply_markup=main_markup)


@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':

        if message.text == "Ты кто?":
            bot.send_message(message.chat.id, "Я котенька Масюня!")
        elif message.text == "Нужен совет!":
            advice_number = random.randint(0, len(replies.ADVICES) - 1)
            bot.send_message(message.chat.id, replies.ADVICES[advice_number])
        elif message.text == "Сделай предсказание!":
            predict_type = random.choice(list(replies.PREDICTS))
            predict_message = random.choice(list(replies.PREDICTS[predict_type]))
            bot.send_message(message.chat.id, predict_message)
        else:
            bot.send_message(message.chat.id, "Я не знаю, что ответить :(")


# RUN
bot.polling(none_stop=True)