import os
import time
import api_sessions
import requests
import os

# 1. URL infos
mapVer = "v1"
dim = "2dtiles"
zoom = 15
x = 6294
y = 13288

baseURL = f"https://tile.googleapis.com/{mapVer}/{dim}/{zoom}/{x}/{y}"

querys = {
    "key": api_sessions.API_KEY,
    "session_token": api_sessions.SESSION_TOKEN,
}

response = requests.get(baseURL, params=querys)
if response.status_code == 200:
    with open("./ds/test_img.png", 'wb') as wr:
        wr.write(response.content)
else:
    f"{response.status_code}"

