from django.shortcuts import render
from django.http import JsonResponse
from .models import Video, Day, DayStatistics,Token
from datetime import date, timedelta
from django.db.models import Sum
import requests

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


def video(request):
    user_id = request.GET.get('user_id')
    tokens = Token.objects.all()
    videos_ = []
    for i in tokens:
        url = "https://tiktok-video-no-watermark2.p.rapidapi.com/user/posts"
        querystring = {"unique_id":f"@{user_id}","cursor":"0"}
        
        headers = {
        "X-RapidAPI-Key": i.RapidApiKey,
        "X-RapidAPI-Host": "tiktok-video-no-watermark2.p.rapidapi.com"
        }
        response = requests.get(url, headers=headers, params=querystring)
        if response.status_code != 200:
            continue
        
        if response.json()['code'] == -1:
            return JsonResponse({'status':404,'data':'Username not found'})
        
        data = response.json()['data']
        videos = data.get('videos')

        if videos is None:
            return JsonResponse({'status':404,'data':'No videos found'})
        
        for video in videos:
            author = video.get('author')['unique_id']
            video_  = f'tiktok.com/@{author}/video/{video["video_id"]}'
            play_count = video.get('play_count')
            videos_.append({'url':video_,'play_count':play_count})
  

    return JsonResponse({'status':200,'data':videos_})


