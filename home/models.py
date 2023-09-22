from collections.abc import Iterable
from datetime import date
from django.db import models
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
import json
TOKEN = "6641753216:AAEbhsq5qljWHbA2Mqt0DczvX_dfGiAs3z4"



from telebot import TeleBot

bot = TeleBot(TOKEN)
from home.utils import play_count

class Token(models.Model):
    RapidApiKey = models.CharField(max_length=300)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.RapidApiKey


class TelegamAdmin(models.Model):
    name = models.CharField(max_length=50)
    tg_id = models.IntegerField(unique=True)

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Админ'
        verbose_name_plural = 'Админы'


# Create your models here.
class Video(models.Model):
    url = models.URLField(unique=True)
    first_view_count = models.IntegerField()
    author = models.CharField(max_length=50)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.url


    class Meta:
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео'


class Day(models.Model):
    date = models.DateField(unique=True, auto_now_add=True)

    def __str__(self):
        return str(self.date)


    class Meta:
        verbose_name = 'День'
        verbose_name_plural = 'Дни'


class DayStatistics(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    day = models.ForeignKey(Day, on_delete=models.CASCADE)
    play_count = models.IntegerField(default=0)
    digg_count = models.IntegerField(default=0)
    collect_count = models.IntegerField(default=0)
    share_count = models.IntegerField(default=0)
    comment_count = models.IntegerField(default=0)
    deltaplay_count = models.IntegerField(default=0)
    deltadigg_count = models.IntegerField(default=0)
    deltacollect_count = models.IntegerField(default=0)
    deltashare_count = models.IntegerField(default=0)
    deltacomment_count = models.IntegerField(default=0)


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.video} - {self.created_at}'


    class Meta:
        verbose_name = 'Статистика дня'
        verbose_name_plural = 'Статистика дней'



@receiver(pre_save, sender=Video)
def set_initial_view_count(sender, instance, **kwargs):
    
    try:
        counts = play_count(instance.url)
        instance.first_view_count = counts[0]
        today = date.today()
        end_day = DayStatistics.objects.filter(video=instance , created_at__date__lte = today ).order_by('-id').first()
        day = Day.objects.filter(date=today).first() or Day.objects.create(date=today)
        day_video, _ = DayStatistics.objects.get_or_create(
            video=instance,
            day=day,
        )
        day_video.play_count = counts[0]
        day_video.digg_count = counts[1]
        day_video.collect_count = counts[2]
        day_video.share_count = counts[3]
        day_video.comment_count = counts[4]
        if end_day:

                day_video.deltaplay_count = day_video.play_count - end_day.play_count
                day_video.deltadigg_count = day_video.digg_count - end_day.digg_count
                day_video.deltacollect_count = day_video.collect_count - end_day.collect_count
                day_video.deltashare_count = day_video.share_count - end_day.share_count
                day_video.deltacomment_count = day_video.comment_count - end_day.comment_count
        day_video.save()
    except Exception as e:
        bot.send_message(chat_id=1614151217, text=f'{str(instance.url)}  ---  {e}')


@receiver(pre_save, sender=TelegamAdmin)
def write_admins(sender, instance, **kwargs):
    admins = {
        'admins': [i.tg_id for i in TelegamAdmin.objects.all()]
    }

    with open('admins.json', 'w') as f:
        json.dump(admins, f)


@receiver(post_save, sender=TelegamAdmin)
def write_adminss(sender, instance, **kwargs):
    admins = {
        'admins': [i.tg_id for i in TelegamAdmin.objects.all()]
    }

    with open('admins.json', 'w') as f:
        json.dump(admins, f)
