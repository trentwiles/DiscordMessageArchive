import extract
import makeHTML


#print(extract.getMessages(1096633230804930685, 50, -1, 3))
# for x in extract.getAllMessages(1181173210717360169, -1, 3):
#     for y in x:
#         print(y["content"])

# # for x in extract.getMessages(1181169631826812999, 1181169646112620554, 2):
#     print(x["content"])

with open("example.html", "a", encoding="utf-8") as e:
    e.write(makeHTML.getHTML(1096633230804930685))