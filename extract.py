import requests
import time

def getToken():
    return open("token.txt").read()

def getMessages(channel_id, before, wait_time):
    mcount = 0
    time.sleep(wait_time)
    holder = []
    channel_id = str(channel_id)
    before = str(before)

    if before == "-1":
        x = requests.get(url=f"https://discord.com/api/v9/channels/{channel_id}/messages?limit=50", headers= {"Authorization": getToken()})
    else:
        x = requests.get(url=f"https://discord.com/api/v9/channels/{channel_id}/messages?before={before}&limit=50", headers= {"Authorization": getToken()})
    
    if x.status_code != 200:
        return None

    for msg in x.json():
        msg_id = msg["id"]
        content = msg["content"]
        ts = msg["timestamp"]
        if msg["edited_timestamp"] != None:
            hasEdit = True
            editTs = msg["edited_timestamp"]
        else:
            hasEdit = False
            editTs = None
        attachments = {}
        if len(msg["attachments"]) != 0:
            attachments = {"url": msg["attachments"][0]["url"]}
        author = {"username": msg["author"]["username"], "userID": msg["author"]["id"], "avatar_url": f"https://cdn.discordapp.com/avatars/{msg['author']['id']}/{msg['author']['avatar']}.webp?size=32", "nickname": msg["author"]["global_name"]}
        edits = {"hasEdits": hasEdit, "edit_timestamp": editTs}
        end_product = {"content": content, "id": msg_id, "timestamp": ts, "edits": edits, "author": author, "attachments": attachments}
        
        holder.append(end_product)
    
    return holder
    #return holder.reverse() + getMessages(channel_id, limit)


def getAllMessages(channel_id, before, wait_time):
    holder = []
    b4 = before
    while True:
        data = getMessages(channel_id, b4, wait_time)
        holder.append(data)
        if len(data) != 50:
            break
        b4 = data[49]["id"]
        # print(data)
        # print("==================================")
    return holder[::1]

def getLimitedMessages(channel_id, before, wait_time, limit):
    holder = []
    b4 = before
    while limit > len(holder):
        data = getMessages(channel_id, b4, wait_time)
        holder.append(data)
        if len(data) != 50:
            break
        b4 = data[49]["id"]
        # print(data)
        # print("==================================")
    return holder[::1]