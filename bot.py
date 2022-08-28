import telebot
from telebot import types
import settings

TOKEN = settings.API_KEY
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'go'])
def start_handler(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    about_us = types.KeyboardButton('О нас')
    doctors = types.KeyboardButton('Наши врачи')
    price = types.KeyboardButton('Цены')
    answers = types.KeyboardButton('Задать вопрос')
    socials = types.KeyboardButton('Социальные сети')
    map = types.KeyboardButton('Как нас найти')
    markup.add(about_us, doctors, price, answers, socials, map)
    bot.send_message(message.chat.id, f"Здравствуйте, {message.from_user.first_name}! \nЧем я Вам могу помочь?", reply_markup=markup)

@bot.message_handler(content_types=["text"])
def handle_text(message):
    if message.text.strip() == 'О нас':
       bot.send_message(message.chat.id, "Мы лучшие")
    elif message.text.strip() == 'Наши врачи':
        img = open('ymap.png', 'rb')
        bot.send_photo(message.chat.id, img)

    #elif message.text.strip() == 'Цены':

    #elif message.text.strip() == 'Задать вопрос':

    #elif message.text.strip() == 'Социальные сети':

    elif message.text.strip() == 'Как нас найти':
        markup = types.InlineKeyboardMarkup()
        btn_my_site = types.InlineKeyboardButton(text='Проложить маршрут', url='https://yandex.ru/maps/org/1145816778')
        markup.add(btn_my_site)
        img = open('ymap.png', 'rb')
        bot.send_photo(message.chat.id, img)
        bot.send_message(message.chat.id, "Севастопольский медицинский альянс, улица Харьковская, дом 3", reply_markup=markup)



bot.polling(none_stop=True, interval=0)