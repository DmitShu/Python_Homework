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

class APIException(Exception):
    pass

# Обрабатываются все сообщения, содержащие команды '/start' or '/help'.
@bot.message_handler(commands=['start', 'help'])
def handle_help(message: telebot.types.Message):
    bot.send_message(message.chat.id, f"Добро пожаловать, {message.chat.username}!\n\n"
                                      f"Чтобы начать работу, введите команду в следующем формате:\n"
                                      f"<имя валюты цену которой нужно узнать> <имя валюты в которой надо узнать цену> <количество валюты>\n\n"
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
    values = message.text.split()

    if len(values) > 3:
        raise APIException('Слишком меого параметров.')

    quote, base, amount = values

    if quote == base:
        raise APIException(f'Введены одинаковые валюты {base}.')

    try:
        quote_ticker = cur[quote]
    except KeyError:
        raise APIException(f'Не удалось обработать валюту {quote}.')

    try:
        base_ticker = cur[base]
    except KeyError:
        raise APIException(f'Не удалось обработать валюту {base}.')

    try:
        amount = float(amount)
    except KeyError:
        raise APIException(f'Не удалось обработать количество {amount}.')

    req = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
    total = json.loads(req.content)[cur[base]] * amount
    repl = f'Цена {amount} {quote} в {base} = {round(total, 2)}'
    bot.send_message(message.chat.id, repl)


bot.polling(none_stop=True)

# test area:
# quote, base, amount = 'USD', 'EUR', 1
# req = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={cur[quote]}&tsyms={cur[base]}')
# repl = json.loads(req.content)[cur[base]]
# print(repl)