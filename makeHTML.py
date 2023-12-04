import extract

def getHeader():
    return open("includes/header.html").read()
def getFooter():
    return open("includes/footer.html").read()

def getHTML(channel_id):
    data = extract.getAllMessages(channel_id, -1, 3)
    html = ''
    for x in data:
        for msg in x:
            html += "<tr><td>" + msg["author"]["username"] + "</td><td>" + msg["content"] + "</td>"
            if msg["attachments"] != {}:
                html += "<td><img src='" + msg["attachments"]["url"] + "' /></td>"
            else:
                html += "<td></td>"
            html += "</td>"
            
    return getHeader() + html + getFooter()