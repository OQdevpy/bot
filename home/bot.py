TOKEN = "6456801430:AAHXFwVb3PWnBRnfKqWuMymz_tjfVClIOtw"



from telebot import TeleBot

from .models import TelegamAdmin
bot = TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    if message.chat.id not in TelegamAdmin.objects.all().values_list('tg_id', flat=True):
        bot.send_message(message.chat.id, "You are not admin!")
    else:
        bot.send_message(message.chat.id, "Hello, I'm a bot!")





bot.polling()