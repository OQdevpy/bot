TOKEN = "6641753216:AAEbhsq5qljWHbA2Mqt0DczvX_dfGiAs3z4"


import json
import requests
from telebot import TeleBot,types

bot = TeleBot(TOKEN)

bot.set_my_commands(
    [
        types.BotCommand('/start', 'Начать'),
        types.BotCommand('/last_7', 'Последние 7 дней'),
        types.BotCommand('/last_month', 'Последний месяц'),
        types.BotCommand('/videos', 'User videos'),
    ]
)

@bot.message_handler(commands=['start'])
def start(message):
    print(message.chat.id)
    with open('admins.json', 'r') as file:
        admins = json.load(file)
    if message.chat.id not in admins['admins']:
        bot.send_message(message.chat.id, 'Вы не админ')
    
    else:
        bot.send_message(message.chat.id, 'Добро пожаловать в бота')

@bot.message_handler(commands=['last_7'])
def last_7(message):
    url = 'http://localhost:8000/last_7/'
    response = requests.get(url)
    data = response.json()['data']
    with open('admins.json', 'r') as file:
        admins = json.load(file)
    if message.chat.id not in admins['admins']:
        bot.send_message(message.chat.id, 'Вы не админ')
    else:
        bot.send_message(message.chat.id, 'Последние 7 дней')
        for i in data:
                bot.send_message(message.chat.id, f'{i["video__url"]} --- {i["play_count"]} --- 🟢 +{i["total_play_count"]}')




    bot.send_message(message.chat.id, 'Последние 7 дней')

@bot.message_handler(commands=['last_month'])
def last_month(message):
    url = 'http://localhost:8000/last_30/'
    response = requests.get(url)
    data = response.json()['data']
    with open('admins.json', 'r') as file:
        admins = json.load(file)
    if message.chat.id not in admins['admins']:
        bot.send_message(message.chat.id, 'Вы не админ')
    else:
        
        bot.send_message(message.chat.id, 'Последний месяц')
        for i in data:
                bot.send_message(message.chat.id, f'{i["video__url"]} --- {i["play_count"]} --- 🟢 +{i["total_play_count"]}')
        bot.send_message(message.chat.id, 'Последний месяц')
    

@bot.message_handler(commands=['videos'])
def videos(message):
    
    # Foydalanuvchidan username kiritishini so'raymiz
    bot.send_message(message.chat.id, 'Iltimos, foydalanuvchi nomini kiriting:')
    bot.register_next_step_handler(message, process_username_step)

def process_username_step(message):
    try:
        username = message.text

        bot.send_message(message.chat.id, f'Siz kiritgan username: {username}')
        # Boshqa kerakli ishlarni bajaring
    except Exception as e:
        bot.send_message(message.chat.id, 'Xatolik yuz berdi. Iltimos, qaytadan kiriting.')

bot.polling()