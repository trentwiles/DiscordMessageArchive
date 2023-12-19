import json
import psycopg2

def connect():
    creds = json.loads(open("config.json").read())
    conn = psycopg2.connect(database=creds["DB_NAME"],
                        host=creds["DB_HOST"],
                        user=creds["DB_USER"],
                        password=creds["DB_PASSWORD"],
                        port=creds["DB_PORT"])
    return [conn, conn.cursor()]

def insMessage(content, image, sent_by, serverID, messageID, epoch):
    x = connect()
    connection = x[0]
    cursor = x[1]

    insert_statement = """
            INSERT INTO msg (content, image, sent_by, serverID, messageID, epoch)
            VALUES (%s, %s, %s, %s, %s, %s);
        """
    
    cursor.execute(insert_statement, (
        content,
        "none",
        sent_by,
        serverID,
        messageID,
        epoch
    ))

    connection.commit()