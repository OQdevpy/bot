import requests
base_url = "https://tiktok-video-no-watermark2.p.rapidapi.com/"

TOKEN = "6641753216:AAEbhsq5qljWHbA2Mqt0DczvX_dfGiAs3z4"



from telebot import TeleBot

bot = TeleBot(TOKEN)


def play_count(url):
    from .models import Token
    tokens = Token.objects.all().order_by('-id')
    headers = {
        "X-RapidAPI-Key": "fc925ae769msh9314f40d1cfad06p11c327jsn2d390b9482b4",
        "X-RapidAPI-Host": "tiktok-video-no-watermark2.p.rapidapi.com"
    }
    for i in tokens:
        try:
            headers['X-RapidAPI-Key'] = i.RapidApiKey
            querystring = {"url": url, "hd": "1"}
            response = requests.get(base_url, headers=headers, params=querystring)
            data = response.json()['data']
            return [data['play_count'],
                    data['digg_count'], 
                    data['collect_count'], 
                    data['share_count'], 
                    data['comment_count']]
        
        except Exception as e:
            bot.send_message(chat_id=1614151217, text=f'token:---  {i} ---  {e}')
            continue
