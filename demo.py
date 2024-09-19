import requests

url = 'https://api.umate.me/api/circle/circle_post_list?'

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
}

data = {
    "username": "Minimmm2006",
    "circle_slug": "OvnSl7",
    "page": "1",
    "media_type": "-1",
    "page_size": "5"
}

response = requests.get(url,headers=headers,params=data)
res = response.json()
print(res["data"])
for i in range(0,len(res["data"]["data"])):
    print('博主昵称：'+res["data"]["data"][i]["author"]['nickname'])
    medium = res["data"]["data"][i]["media"]
    try:
        print('博主该帖子m3u8视频地址为：'+medium[0]['paths']['medium'])
    except:
        print('m3u8视频为空')
    try:
        print('博主该帖子视频封面图片地址为：'+medium[0]['paths']['medium'])
    except:
        print('图片为空')
    print('博主帖子文案：'+res["data"]["data"][i]["content"])
