from cgitb import text
from pydoc import doc
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
    markup.add(about_us, doctors, price, answers, contacts, map)
    bot.send_message(message.chat.id, f"Здравствуйте, {message.from_user.first_name}! \nЧем я Вам могу помочь?", reply_markup=markup)

@bot.message_handler(commands=['doctors'])
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
       mess = "<b>Севастопольский медицинский альянс</b>-многопрофильный лечебно-диагностический центр в Севастополе с хирургическим уклоном, функционирующий более 11 лет.Наши специалисты обладают большим опытом и продолжительным стажем от 13 до 37 лет работы по специальности. Клиника оснащена высокотехнологичным оборудованием, используются малотравматичные методики лечения.\n \n<b>Прием ведут:</b> \n \n -Мишарев Иван Викторович(флеболог/хирург; стаж 21 год) \n \n -Гансон Алексей Павлович(Лазерный хирург/; стаж 17 лет) \n \n -Мочалова Светлана Вадимовна(гинеколог; стаж 25 лет) \n \n -Михеенко Геннадий Валентинович(гастроэнтеролог; стаж 37 лет) \n \n -Онищук Николай Александрович(проктолог; стаж 21 год) \n \n -Синицына Екатерина Николаевна(дерматовенеролог; стаж 14 лет) \n \n -Кочуров Сергей Юрьевич(травматолог-ортопед; стаж 21 год) \n \n-Мишарева Анна Олеговна (гастроэнтеролог-диетолог; стаж 13 лет) \n \nМы не предлагаем дополнительных скрытых расходов, а назначаем только необходимое лечение "
       bot.send_message(message.chat.id, mess, parse_mode='html')
    elif message.text.strip() == 'Наши врачи':
        def doctors(message):  
            markup = telebot.types.InlineKeyboardMarkup()
            markup.add(telebot.types.InlineKeyboardButton(text='Травматолог', callback_data=1))
            markup.add(telebot.types.InlineKeyboardButton(text='Гинеколог', callback_data=2))
            markup.add(telebot.types.InlineKeyboardButton(text='Лазерный хирург', callback_data=3))
            markup.add(telebot.types.InlineKeyboardButton(text='Хирург', callback_data=4))
            markup.add(telebot.types.InlineKeyboardButton(text='Гастроентеролог', callback_data=5))
            bot.send_message(message.chat.id, text="Какой врач Вас интересует?", reply_markup=markup)
        doctors(message)

    elif message.text.strip() == 'Цены':
        mess = "<b>ЦЕНЫ НА КОНСУЛЬТАЦИИ:</b> \n \n<b>-Травматолог:</b> 1500, повторная 1200 \n \n<b>-Дерматовенеролог:</b> 1500, повторная 1200\n \n<b>-Хирург:</b> 1000 \n \n<b>-Проктолог:</b> 1000, повторная 1000, с ретроскопией 2500 \n \n<b>-Лор:</b> 1500 \n \n<b>-Гастроэнтеролог:</b> 1500, повторная 1200 \n \n<b>-Гинеколог:</b> 1500, повторная 1200 \n \n<b>-Флеболог:</b> 1000 \n \n<u>*повторная консультация действует в течение месяца</u>"
        bot.send_message(message.chat.id, mess, parse_mode='html')
    elif message.text.strip() == 'Задать вопрос':
        markup = types.InlineKeyboardMarkup()
        support = types.InlineKeyboardButton(text='Перейти в чат с администратором', url='https://t.me/mashakoshevets')
        markup.add(support)
        bot.send_message(message.chat.id, "Если у Вас остались какие-либо вопросы или предложения - пишите, обязательно на все ответим!", reply_markup=markup)

    elif message.text.strip() == 'Контакты':
        markup = types.InlineKeyboardMarkup()
        vk = types.InlineKeyboardButton(text='Вконтакте', url='https://vk.com/sevmedalians')
        inst = types.InlineKeyboardButton(text='Инстаграм', url='https://instagram.com/sevmedalians?igshid=YmMyMTA2M2Y=')
        markup.add(vk, inst)
        bot.send_message(message.chat.id, "Телефон для записи: \n+7(978)-840-08-85 \n+7(8692)55-11-88", reply_markup=markup)

    elif message.text.strip() == 'Как нас найти':
        markup = types.InlineKeyboardMarkup()
        btn_my_site = types.InlineKeyboardButton(text='Проложить маршрут', url='https://yandex.ru/maps/org/1145816778')
        markup.add(btn_my_site)
        img = open('ymap.png', 'rb')
        bot.send_photo(message.chat.id, img)
        bot.send_message(message.chat.id, "Севастопольский медицинский альянс, улица Харьковская, дом 3", reply_markup=markup)

bot.polling(none_stop=True, interval=0)