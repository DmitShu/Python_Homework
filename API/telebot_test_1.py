import telebot
import requests
import lxml.html

tokfile = '..\dist\Token'

with open(tokfile, encoding='utf8') as f:
    tok = f.read()

bot = telebot.TeleBot(tok)

def fact_data():
    html = requests.get('https://www.yacgms.ru/fakticheskie-dannye/').content  # фактические данные

    # создадим объект ElementTree. Он возвращается функцией parse()
    tree = lxml.html.document_fromstring(html)

    tbody = tree.findall(
        'body/div[1]/div[2]/div/div/div[1]/main/article/div/div/table/tbody/tr')  # помещаем в аргумент методу findall скопированный xpath

    message = 'Данные в реальном времени по ЯО \nМС - Метеорологическая станция \nАМС - Автоматическая метеорологическая станция\n' + 69 * '-' + '\n'

    # print('Данные в реальном времени по ЯО \nМС - Метеорологическая станция \nАМС - Автоматическая метеорологическая станция')
    # print(69*'-')

    for tr in tbody:
        tmp = tr.findall('td')
        if len(tmp):
            message += f'\t{tmp[0].text}\nТемпература: {tmp[1].text} °C\nДавление: {tmp[3].text} мм р.ст.\nВлажность: {tmp[4].text} %\nСкорость ветра: {tmp[2].text} м/с\n\n'
            # print(f'\t{tmp[0].text}\nТемпература: {tmp[1].text} °C\nДавление: {tmp[3].text} мм р.ст.\nВлажность: {tmp[4].text} %\nСкорость ветра: {tmp[2].text} м/с\n')
    # print(message)
    return(message)

# Обрабатываются все сообщения, содержащие команды '/start' or '/help'.
@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
    bot.send_message(message.chat.id, f"Welcome, \ {message.chat.username}")

# Обрабатываются все сообщения, содержащие команды '/start' or '/help'.
@bot.message_handler(commands=['ytemp'])
def handle_ytemp(message):
    bot.send_message(message.chat.id, fact_data())

# Обрабатываются все документы и аудиозаписи
@bot.message_handler(content_types=['document', 'audio'])
def handle_docs_audio(message):
    pass

# На фотки
@bot.message_handler(content_types=['photo'])
def say_lmao(message: telebot.types.Message):
    bot.reply_to(message, 'Nice meme XDD')

# Повторяло
@bot.message_handler()
def say_lmao(message: telebot.types.Message):
    bot.send_message(message.chat.id, f'Здорова, \ {message.chat.username} \n Чтобы узнать данные с метеостанции ЯО введи \ytemp')

bot.polling(none_stop=True)