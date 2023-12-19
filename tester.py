import links
import random
import makeHTML
import extract

channel_database = links.scanServers(2)
for channel in channel_database:
    # format: {'id': '485196500830519300', 'name': 'Aoun Gang'}
    links.extractAndIndex(channel, random.randint(2,4), 500)