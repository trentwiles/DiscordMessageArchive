import requests
import json

def getToken():
    return open("token.txt").read()

def getMessages(channel_id, limit, before):
    limit = str(limit)
    channel_id = str(channel_id)
    if before != -1:
        x = requests.get(url="https://discord.com/api/v9/channels/{channel_id}/messages?limit={limit}", headers= {"Authorization": getToken()})
    else:
        x = requests.get(url="https://discord.com/api/v9/channels/{channel_id}/messages?limit={limit}", headers= {"Authorization": getToken()})
    print(x.json())