import os
import time
import api_sessions
import requests
import os


baseURL = "https://tile.googleapis.com/v1/2dtiles/15/6294/13288"

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

