import extract
import requests
import time

def scanServers(wait_time):
    holder = []
    r = requests.get("https://discordapp.com/api/users/@me/guilds", headers= {"Authorization": extract.getToken()})
    if r.status_code == 200:
        for x in r.json():
            time.sleep(wait_time)
            c = requests.get("https://discord.com/api/v9/guilds/" + x["id"] + "/channels?channel_limit=100",  headers= {"Authorization": extract.getToken()}).json()
            for ch in c:
                holder.append({"id": ch["id"], "name": ch["name"]})
    return holder

data = scanServers(2)
print(data)
print(len(data))