from .models import Day, DayStatistics, Video
TOKEN = "6641753216:AAEbhsq5qljWHbA2Mqt0DczvX_dfGiAs3z4"
from datetime import date, timedelta
from django.db.models import Sum

from telebot import TeleBot

bot = TeleBot(TOKEN)
from .models import TelegamAdmin
def day_statistics():
    videos = Video.objects.all()
    for video in videos:
        try:
            video.save()
        except Exception as e:
            continue



def send_messages():
    try:
        day = Day.objects.last()
        message = "Просмотры за 24 часа\n\n"

        day_videos = DayStatistics.objects.filter(day=day)
        full_view_count = 0
        most_url = str(day_videos.last().video.url)
        most_view = 0
        for i,day_video in enumerate(day_videos):
            try:
                delta_view  = day_video.deltaplay_count
                full_view_count += delta_view
                if day_video.deltaplay_count >most_view:
                    most_view = day_video.deltaplay_count
                    most_url = str(day_video.video)


                message += f'{i+1})\n{day_video.video.url}\n👁 {day_video.play_count}\n🟢 +{day_video.deltaplay_count}\n\n'
            except Exception as e:
                if day_video.deltaplay_count >most_view:
                    most_view = day_video.deltaplay_count
                    most_url = str(day_video.video)
                full_view_count += day_video.deltaplay_count
                message += f'{i+1})\n{day_video.video.url}\n👁 {day_video.play_count}\n🟢 +{day_video.deltaplay_count}\n\n'

        message += f'___\nИтого за 24 часа:👁  +{full_view_count}\nНаибольший прирост:🟢 +{most_view} ({most_url})'
        for chat_id in TelegamAdmin.objects.all().values_list('tg_id', flat=True):
            try:
                bot.send_message(chat_id=chat_id, text=message)
            except Exception as e:
                bot.send_message(chat_id=1614151217, text=f'{chat_id}  ---  {e}')
    
    except Exception as e:
        bot.send_message(chat_id=1614151217, text=f'{e}')


def send_messages_7():
    today = date.today()
    start_date = today - timedelta(days=7)  
    
    video_statistics = []
    videos = Video.objects.all()
    for video in videos:
        day_statistics = DayStatistics.objects.filter(video=video, created_at__date__range=[start_date, today])

        video_statistics.append(
            {
                'total_play_count': day_statistics.aggregate(Sum('deltaplay_count'))['deltaplay_count__sum'],
                'video__url': video.url,
                'play_count': day_statistics.last().play_count,
            }
        )
    message = "Просмотры за последние 7 дней\n\n"
    for i,video in enumerate(video_statistics):
        message += f'{i+1})\n{video["video__url"]}\n👁 {video["play_count"]}\n🟢 +{video["total_play_count"]}\n\n'
    for chat_id in TelegamAdmin.objects.all().values_list('tg_id', flat=True):
        try:
            bot.send_message(chat_id=chat_id, text=message)
        except Exception as e:
            bot.send_message(chat_id=1614151217, text=f'{chat_id}  ---  {e}')

def send_messages_30():
    today = date.today()
    start_date = today - timedelta(days=30)  
    
    video_statistics = []
    videos = Video.objects.all()
    for video in videos:
        day_statistics = DayStatistics.objects.filter(video=video, created_at__date__range=[start_date, today])

        video_statistics.append(
            {
                'total_play_count': day_statistics.aggregate(Sum('deltaplay_count'))['deltaplay_count__sum'],
                'video__url': video.url,
                'play_count': day_statistics.last().play_count,
            }
        )
    message = "Просмотры за последний месяц\n\n"
    for i,video in enumerate(video_statistics):
        message += f'{i+1})\n{video["video__url"]}\n👁 {video["play_count"]}\n🟢 +{video["total_play_count"]}\n\n'
    for chat_id in TelegamAdmin.objects.all().values_list('tg_id', flat=True):
        try:
            bot.send_message(chat_id=chat_id, text=message)
        except Exception as e:
            bot.send_message(chat_id=1614151217, text=f'{chat_id}  ---  {e}')

def send_messages_():
    bot.send_message(chat_id=1614151217, text='test')