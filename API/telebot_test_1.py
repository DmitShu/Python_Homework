import telebot

tokfile = '..\dist\Token'

with open(tokfile, encoding='utf8') as f:
    tok = f.read()

bot = telebot.TeleBot(tok)

# Обрабатываются все сообщения, содержащие команды '/start' or '/help'.
@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
    bot.send_message(message.chat.id, f"Welcome, \ {message.chat.username}")

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
    bot.send_message(message.chat.id, message.text)

bot.polling(none_stop=True)