import extract

def getHeader():
    return open("includes/header.html").read()
def getFooter():
    return open("includes/footer.html").read()

def getHTML(channel_id):
    mcount = 0
    data = extract.getAllMessages(channel_id, -1, 3)
    html = ''
    mcount += len(data)
    for x in data:
        for msg in x:
            html += "<tr><td>" + msg["author"]["username"] + "</td><td>" + msg["content"]
            if msg["attachments"] != {}:
                html += "<br><img src='" + msg["attachments"]["url"] + "' /></td>"
            else:
                html += "</td>"
            html += "<td>" + str(msg["timestamp"]) + "</td></tr>"

    print("[INFO] Exported " + str(mcount) + " messages.")

    return getHeader() + html + getFooter()