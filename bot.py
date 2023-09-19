TOKEN = "6456801430:AAHXFwVb3PWnBRnfKqWuMymz_tjfVClIOtw"


import json
from telebot import TeleBot

bot = TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    with open('admins.json', 'r') as file:
        admins = json.load(file)
    if message.chat.id not in admins['admins']:
        bot.send_message(message.chat.id, 'Вы не админ')
    else:
        bot.send_message(message.chat.id, 'Добро пожаловать в бота')

bot.polling()