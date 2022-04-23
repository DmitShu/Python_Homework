import telebot
import requests
import lxml.html

tokfile = 'data\Token'

with open(tokfile, encoding='utf8') as f:
    tok = f.read()

bot = telebot.TeleBot(tok)

cur = {
    'Г1': 'G',
    'Г2': 'H',
    'Г3': 'F',
}

# Обрабатываются все сообщения, содержащие команды '/start' or '/help'.
@bot.message_handler(commands=['start', 'help'])
def handle_help(message: telebot.types.Message):
    bot.send_message(message.chat.id, f"Добро пожаловать, {message.chat.username}!\n"
                                      f"Чтобы начать работу, введите команду в следующем формате:\n"
                                      f"<имя валюты цену которой нужно узнать> <имя валюты в которой надо узнать цену> <количество валюты>"
                                      f"список доступных валют можно узнать по команде /values")

# Обрабатываются все сообщения, содержащие команды '/start' or '/help'.
@bot.message_handler(commands=['values'])
def handle_values(message: telebot.types.Message):
    repl = "Лоступные валюты:"
    for k in cur.keys():
        repl += '\n' + '\t' + k
    bot.send_message(message.chat.id, repl)

bot.polling(none_stop=True)