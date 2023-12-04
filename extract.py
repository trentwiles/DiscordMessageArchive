import requests
import json

def getToken():
    return open("token.txt").read()

def getMessages(channel_id, limit, before):
    holder = []
    limit = str(limit)
    channel_id = str(channel_id)

    if before != -1:
        x = requests.get(url=f"https://discord.com/api/v9/channels/{channel_id}/messages?limit={limit}", headers= {"Authorization": getToken()})
    else:
        x = requests.get(url=f"https://discord.com/api/v9/channels/{channel_id}/messages?limit={limit}", headers= {"Authorization": getToken()})
    
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
        author = {"username": msg["author"]["username"], "userID": msg["author"]["id"], "avatar_url": f"https://cdn.discordapp.com/avatars/{msg['author']['id']}/{msg['author']['avatar']}.webp?size=32", "nickname": msg["author"]["global_name"]}
        edits = {"hasEdits": hasEdit, "edit_timestamp": editTs}
        end_product = {"content": content, "id": msg_id, "timestamp": ts, "edits": edits, "author": author}
        
        holder.append(end_product)
        
    return holder