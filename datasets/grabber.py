import api_sessions
import requests

# 1. URL infos
mapVer = "v1"
dim = "2dtiles"
zoom = 15
cordinates = [2500, 2500] # [lat, lng]
rocky_dataset_folder = "datasets/rocky/"
baseURL = f"https://tile.googleapis.com/{mapVer}/{dim}/{zoom}/{cordinates[0]}/{cordinates[1]}"

# 2. Querys
querys = {
    "key": api_sessions.API_KEY,
    "session_token": api_sessions.SESSION_TOKEN,
}

# 3. Request
response = requests.get(baseURL, params=querys)
if response.status_code == 200:
    with open(f"{rocky_dataset_folder}colarado_img3.png", 'wb') as wr:
        wr.write(response.content)
        print("Done")
else:
    print(f"{response.status_code}")


