from .models import Day, DayStatistics, Video
TOKEN = "6456801430:AAHXFwVb3PWnBRnfKqWuMymz_tjfVClIOtw"



from telebot import TeleBot

bot = TeleBot(TOKEN)
from .models import TelegamAdmin
def day_statistics():
    videos = Video.objects.all()
    for video in videos:
        
        try:
            video.save()
        except Exception as e:
            print(e)
            bot.send_message(chat_id=1614151217, text=f'{video}  ---  {e}')
            print(e)
            continue



def send_messages():
    day = Day.objects.last()
    yestday = Day.objects.all().order_by('-id')[1]
    message = "Просмотры за 24 часа\n\n"

    day_videos = DayStatistics.objects.filter(day=day)
    full_view_count = 0
    most_url = ""
    most_view = 0
    for i,day_video in enumerate(day_videos):
        try:
            yesterday = DayStatistics.objects.get(video = day_video, day=yestday.id-1)
            delta_view  = day_video.play_count - yesterday.play_count
            full_view_count += delta_view
            if day_video.play_count >most_view:
                most_view = day_video.play_count
                most_url = day_video.video.url


            message += f'{i+1})\n{day_video.video.url}\n👁 {day_video.play_count}\n🟢 +{delta_view}\n\n'
        except Exception:
            if day_video.play_count >most_view:
                most_view = day_video.play_count
                most_url = day_video.video.url
            full_view_count += day_video.play_count
            message += f'{i+1})\n{day_video.video.url}\n👁 {day_video.play_count}\n🟢 +{day_video.play_count}\n\n'
    
    message += f'___\nИтого за 24 часа:👁  +{full_view_count}\nНаибольший прирост:🟢 +{most_view} ({most_url})'
    for chat_id in TelegamAdmin.objects.all().values_list('tg_id', flat=True):
        try:
            bot.send_message(chat_id=chat_id, text=message)
        except Exception as e:
            bot.send_message(chat_id=1614151217, text=f'{chat_id}  ---  {e}')
    