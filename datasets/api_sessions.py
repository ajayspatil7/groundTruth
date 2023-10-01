import requests
API_KEY = "SIGNATURE-HIDDEN"
SESSION_TOKEN = "SIGNATURE-HIDDEN"

# 1. URL infos

params = {
    "mapType": "satellite",
    "language": "en-US",
    "region": "US",
}

api_Endpoint = f"https://tile.googleapis.com/v1/createSession?key={API_KEY}"
api_Header = {"content-type": "application/json"}

resp = requests.post(api_Endpoint, headers=api_Header, json=params)

if resp.status_code == 200:
    data = resp.json()
    print(data)
    print(data["session"])
else:
    print(f"{resp.status_code}")