import telebot
import requests
import lxml.html
import json

tokf = 'data\Token'

with open(tokf) as f:
    tok = f.read()

bot = telebot.TeleBot(tok)

cur = {
    'USD': 'USD',
    'EUR': 'EUR',
    'RUB': 'RUB',
    'Доллар': 'USD',
    'Евро': 'EUR',
    'Рубль': 'RUB',
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

# Обрабатываются все сообщения
@bot.message_handler(content_types=['text'])
def do_convert(message: telebot.types.Message):
    quote, base, amount = message.text.split()
    req = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={cur[quote]}&tsyms={cur[base]}')
    repl = json.loads(req.content)[cur[base]]
    bot.send_message(message.chat.id, repl)


bot.polling(none_stop=True)

# test area:
# quote, base, amount = 'USD', 'EUR', 1
# req = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={cur[quote]}&tsyms={cur[base]}')
# repl = json.loads(req.content)[cur[base]]
# print(repl)