import extract
import requests
import time
import db

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

def extractAndIndex(server_data, wait_time, channel_limit):
    data = extract.getLimitedMessages(server_data["id"], -1, wait_time, channel_limit)
    for x in data:
        print(x)
        if x == None:
            break
        for y in x:
            db.insMessage(y["content"], "none", y["author"]["username"], server_data["id"], y["id"], round(time.time()))
            print("entered message ID " + y["id"] + " into DB")