from django.utils import timezone
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

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
    date = models.DateField(unique=True,auto_now_add=True)

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
    counts = play_count(instance.url)
    instance.first_view_count = counts[0]  
    day, _ = Day.objects.get_or_create()
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


    