import telebot
from bot_config import cur
from bot_extensions import APIException, Bot_Extensions

bot = telebot.TeleBot(Bot_Extensions.get_token())

# Обрабатываются все сообщения, содержащие команды '/start' or '/help'.
@bot.message_handler(commands=['start', 'help'])
def handle_help(message: telebot.types.Message):
    bot.send_message(message.chat.id, f"Добро пожаловать, {message.chat.username}!\n\n"
                                      f"Чтобы начать работу, введите команду в следующем формате:\n"
                                      f"<имя валюты цену которой нужно узнать> <имя валюты в которой надо узнать цену> <количество валюты> (USD RUB 1000)\n\n"
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
    try:
        values = message.text.split()

        if len(values) != 3:
            raise APIException('"Параметров должно быть три"')

        quote, base, amount = values
        total = Bot_Extensions.get_price(quote, base, amount)
    except APIException as ex:
        bot.send_message(message.chat.id, f'Ошибка:\n{ex}\n'
                                          f'Введите команду в следующем формате:\n'
                                          f'<имя валюты цену которой нужно узнать> <имя валюты в которой надо узнать цену> <количество валюты> (USD RUB 1000)\n\n'
                                          f'список доступных валют можно узнать по команде /values')

    except Exception as ex:
        bot.send_message(message.chat.id, f'Ошибка:\n{ex}\n'
                                          f'Попробуйте команду /help\n'
                                          f'Если ничего не помогло, обратитесь к разработчику.')

    else:
        repl = f'Цена {amount} {quote} в {base} = {round(total, 2)}'
        bot.send_message(message.chat.id, repl)

bot.polling(none_stop=True)

# test area:
# quote, base, amount = 'USD', 'EUR', 1
# req = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={cur[quote]}&tsyms={cur[base]}')
# repl = json.loads(req.content)[cur[base]]
# print(repl)