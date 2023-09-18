import requests

base_url = "https://tiktok-video-no-watermark2.p.rapidapi.com/"


headers = {
    "X-RapidAPI-Key": "fc925ae769msh9314f40d1cfad06p11c327jsn2d390b9482b4",
    "X-RapidAPI-Host": "tiktok-video-no-watermark2.p.rapidapi.com"
}


def play_count(url):
    querystring = {"url": url, "hd": "1"}
    response = requests.get(base_url, headers=headers, params=querystring)
    data = response.json()['data']
    try:
        return [data['play_count'],
                data['digg_count'], 
                data['collect_count'], 
                data['share_count'], 
                data['comment_count']]
    except Exception:
        return 0
