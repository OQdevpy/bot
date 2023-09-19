TOKEN = "6520623145:AAFfCLyxIAdVzRhYo1LcE0r8oJAKm5gVVdc"


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