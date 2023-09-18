from django.db import models

# Create your models here.
class Video(models.Model):
    url = models.URLField()
    first_view_count = models.IntegerField()
    author = models.CharField(max_length=50)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        self.url

class DayStatistics(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    view_count = models.IntegerField()
    like_count = models.IntegerField()
    dislike_count = models.IntegerField()
    comment_count = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        self.video.url
        