import requests
from .models import Token
base_url = "https://tiktok-video-no-watermark2.p.rapidapi.com/"




def play_count(url):
    tokens = Token.objects.all()
    headers = {
        "X-RapidAPI-Key": "fc925ae769msh9314f40d1cfad06p11c327jsn2d390b9482b4",
        "X-RapidAPI-Host": "tiktok-video-no-watermark2.p.rapidapi.com"
    }
    for i in tokens:
        headers['X-RapidAPI-Key'] = i.RapidApiKey
        querystring = {"url": url, "hd": "1"}
        response = requests.get(base_url, headers=headers, params=querystring)
        data = response.json()['data']
        try:
            return [data['play_count'],
                    data['digg_count'], 
                    data['collect_count'], 
                    data['share_count'], 
                    data['comment_count']]
        except Exception as e:
            continue
