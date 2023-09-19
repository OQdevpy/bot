from .models import Video
TOKEN = "6456801430:AAHXFwVb3PWnBRnfKqWuMymz_tjfVClIOtw"



from telebot import TeleBot

from .models import TelegamAdmin
def day_statistics():
    videos = Video.objects.all()
    for video in videos:
        
        video.save()



def send_message():
    bot = TeleBot(TOKEN)
    
    message = "Salom, bu avtomatik xabar!"
    for chat_id in TelegamAdmin.objects.all().values_list('tg_id', flat=True):
        bot.send_message(chat_id=chat_id, text=message)

    