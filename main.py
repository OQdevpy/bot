urls="https://www.tiktok.com/@pastrychef_am/video/7279831485102722337"
print(urls)
import requests
from pprint import pprint

url = "https://tiktok-video-no-watermark2.p.rapidapi.com/"

querystring = {"url":urls,"hd":"1"}

headers = {
 "X-RapidAPI-Key": "fc925ae769msh9314f40d1cfad06p11c327jsn2d390b9482b4",
 "X-RapidAPI-Host": "tiktok-video-no-watermark2.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)


pprint(response.json())