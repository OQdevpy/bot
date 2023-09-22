from django.shortcuts import render
from django.http import JsonResponse
from .models import Video, Day, DayStatistics
from datetime import date, timedelta
from django.db.models import Sum

def last_7(request):
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

    return JsonResponse({'data': list(video_statistics)})


def last_30(request):
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
    return JsonResponse({'data': list(video_statistics)})