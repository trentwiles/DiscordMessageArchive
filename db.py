import os
from sqlalchemy import create_engine, text
import json

username = json.loads(open("config.json").read())["username"]
password = json.loads(open("config.json").read())["password"]
address = json.loads(open("config.json").read())["address"]
database = json.loads(open("config.json").read())["db"]

def connect():
    engine = create_engine(f"cockroachdb://{username}:{password}@{address}/{database}?sslmode=verify-full")
    return engine.connect()

# db structure
"""
CREATE TABLE msg (
  content TEXT,
  image TEXT,
  sent_by VARCHAR(255),
  serverID VARCHAR(255),
  messageID VARCHAR(255),
  epoch INT
); 
"""

def insMessage(content, image, sent_by, serverID, messageID, epoch):
    stmt = text("INSERT INTO msg (content, image, sent_by, serverID, messageID, epoch) VALUES (:content, :image, :sent_by, :serverID, :messageID, :epoch)")

    params = {
        'content': content,
        'image': 'none',
        'sent_by': sent_by,
        'serverID': serverID,
        'messageID': messageID,
        'epoch': epoch
    }

    connect().execute(stmt, params)

def deleteAll():
    res = connect().execute(text("delete from msg where 0=0;"))