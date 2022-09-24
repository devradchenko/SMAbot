import telebot
from telebot import types
import setting

TOKEN = setting.API_KEY
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'go'])
def start_handler(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    about_us = types.KeyboardButton('О нас')
    doctors = types.KeyboardButton('Наши врачи')
    price = types.KeyboardButton('Цены')
    answers = types.KeyboardButton('Задать вопрос')
    contacts = types.KeyboardButton('Контакты')
    map = types.KeyboardButton('Как нас найти')
    markup.add(about_us, doctors, price, answers, socials, map)
    bot.send_message(message.chat.id, f"Здравствуйте, {message.from_user.first_name}! \nЧем я Вам могу помочь?", reply_markup=markup)

@bot.message_handler(commands=['doctora'])
def doctors(message):  
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton(text='Травматолог', callback_data=1))
    markup.add(telebot.types.InlineKeyboardButton(text='Гинеколог', callback_data=2))
    markup.add(telebot.types.InlineKeyboardButton(text='Лазерный хирург', callback_data=3))
    markup.add(telebot.types.InlineKeyboardButton(text='Хирург', callback_data=4))
    markup.add(telebot.types.InlineKeyboardButton(text='Гастроентеролог', callback_data=5))
    bot.send_message(message.chat.id, text="Какой врач Вас интересует?", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):

    bot.answer_callback_query(callback_query_id=call.id, text='Давайте знакомиться!')
    answer = ''
    img = ''
    if call.data == '1':
        answer = 'Текст про нашего травматолога!'
        img = open('travma.png', 'rb')
    elif call.data == '2':
        answer = 'текст про гинеколога!'
        img = open('ginekolog.png', 'rb')
    elif call.data == '3':
        answer = 'текст про лазерного хирурга!'
        img = open('laser.png', 'rb')
    elif call.data == '4':
        answer = 'текст про хирурга!'
        img = open('hirurg.png', 'rb')
    elif call.data == '5':
        answer = 'текст про гастроентеролога!'
        img = open('gastro.png', 'rb')

    bot.send_photo(call.message.chat.id, img)
    bot.send_message(call.message.chat.id, answer)

@bot.message_handler(content_types=["text"])
def handle_text(message):
    if message.text.strip() == 'О нас':
       bot.send_message(message.chat.id, "Мы лучшие")
    elif message.text.strip() == 'Наши врачи':
        bot.send_message(message.chat.id, "/doctora")
       

    #elif message.text.strip() == 'Цены':

    #elif message.text.strip() == 'Задать вопрос':

    elif message.text.strip() == 'Контакты':
        markup = types.InlineKeyboardMarkup()
        vk = types.InlineKeyboardButton(text='Вконтакте', url='https://vk.com/sevmedalians')
        inst = types.InlineKeyboardButton(text='инстаграм', url='https://instagram.com/sevmedalians?igshid=YmMyMTA2M2Y=')
        markup.add(vk, inst)
        bot.send_message(message.chat.id, "Наши контакты:", reply_markup=markup)


    elif message.text.strip() == 'Как нас найти':
        markup = types.InlineKeyboardMarkup()
        btn_my_site = types.InlineKeyboardButton(text='Проложить маршрут', url='https://yandex.ru/maps/org/1145816778')
        markup.add(btn_my_site)
        img = open('ymap.png', 'rb')
        bot.send_photo(message.chat.id, img)
        bot.send_message(message.chat.id, "Севастопольский медицинский альянс, улица Харьковская, дом 3", reply_markup=markup)



bot.polling(none_stop=True, interval=0)