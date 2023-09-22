import requests

url = "https://tiktok-video-no-watermark2.p.rapidapi.com/"

querystring = {"url":"https://www.tiktok.com/@vegitodraws_/video/7250542477122243866?_op=1&_r=1&_t=8dcmlmjxcNu","hd":"1"}

headers = {
 "X-RapidAPI-Key": "fc925ae769msh9314f40d1cfad06p11c327jsn2d390b9482b4",
 "X-RapidAPI-Host": "tiktok-video-no-watermark2.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)



import requests

url = "https://tiktok-video-no-watermark2.p.rapidapi.com/"

querystring = {"url":"https://www.tiktok.com/@tiktok/video/7231338487075638570","hd":"1"}

headers = {
 "X-RapidAPI-Key": "54e262782emsh7c9b12dd7f332b4p158bd6jsnaee732e6c4a8",
 "X-RapidAPI-Host": "tiktok-video-no-watermark2.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)
