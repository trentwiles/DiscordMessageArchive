import links
import makeHTML
import extract

channel_database = links.scanServers(2)
for channel in channel_database:
    # format: {'id': '485196500830519300', 'name': 'Aoun Gang'}
    extract.getLimitedMessages(channel["id"], -1, 2, 500)