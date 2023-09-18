from .models import Video
def day_statistics():
    videos = Video.objects.all().update()