from collections.abc import Iterable
from django.utils import timezone
from django.db import models
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
import json
TOKEN = "6456801430:AAHXFwVb3PWnBRnfKqWuMymz_tjfVClIOtw"



from telebot import TeleBot

bot = TeleBot(TOKEN)
from home.utils import play_count


class TelegamAdmin(models.Model):
    name = models.CharField(max_length=50)
    tg_id = models.IntegerField(unique=True)

    def __str__(self):
        return self.name


# Create your models here.
class Video(models.Model):
    url = models.URLField(unique=True)
    first_view_count = models.IntegerField()
    author = models.CharField(max_length=50)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.url


class Day(models.Model):
    date = models.DateField(unique=True, auto_now_add=True)

    def __str__(self):
        return str(self.date)


class DayStatistics(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    day = models.ForeignKey(Day, on_delete=models.CASCADE)
    play_count = models.IntegerField(default=0)
    digg_count = models.IntegerField(default=0)
    collect_count = models.IntegerField(default=0)
    share_count = models.IntegerField(default=0)
    comment_count = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.video} - {self.created_at}'


@receiver(pre_save, sender=Video)
def set_initial_view_count(sender, instance, **kwargs):
    try:

        counts = play_count(instance.url)
        instance.first_view_count = counts[0]
        day, _ = Day.objects.get_or_create(date=timezone.now().date())
        day_video, _ = DayStatistics.objects.get_or_create(
            video=instance,
            day=day,
        )
        day_video.play_count = counts[0]
        day_video.digg_count = counts[1]
        day_video.collect_count = counts[2]
        day_video.share_count = counts[3]
        day_video.comment_count = counts[4]
        day_video.save()
    except Exception as e:
        print(e)
        bot.send_message(chat_id=1614151217, text=f'{instance.url}  ---  {e}')


# post save for telegramadmin
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
