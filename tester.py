import extract


#print(extract.getMessages(1096633230804930685, 50, -1, 3))
for x in extract.getAllMessages(1181169631826812999, -1, 3):
    print(x["content"])