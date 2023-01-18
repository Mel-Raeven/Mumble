from flask import Flask, request, Response
import json
from gevent.pywsgi import WSGIServer
import mysql.connector as mariadb

app = Flask(__name__)
mariadb_connection = mariadb.Connect(user='root', password='admin', host='192.168.178.222', port='3306', database='mumble')
create_cursor = mariadb_connection.cursor()

@app.route('/message/post', methods=['POST'])
def post():
    ___requestBody = json.loads(request.get_data())
    ___sql_statement = 'INSERT INTO message (Content, Sender) VALUES (%s, %s);'
    ___variables = (
        ___requestBody["content"],
        ___requestBody["from"],
    )
    create_cursor.execute(___sql_statement, ___variables)
    mariadb_connection.commit()
    
    ___sql_statement = 'SELECT LAST_INSERT_ID();'
    create_cursor.execute(___sql_statement)
    insertedID = create_cursor.fetchone()
    insertedID = insertedID[0]

    ___sql_statement = 'SELECT id from user where Name=%s;'
    print(___requestBody["from"])
    ___variables = (
        ___requestBody["from"],
    )
    create_cursor.execute(___sql_statement, ___variables)
    userID = create_cursor.fetchone()
    userID = userID[0]

    ___sql_statement = 'SELECT id from user where Name=%s;'
    ___variables = (
        ___requestBody["destination"],
    )
    create_cursor.execute(___sql_statement, ___variables)
    friendID = create_cursor.fetchone()
    friendID = friendID[0]

    ___sql_statement = 'INSERT INTO messageuser (MessageID, UserID, User2ID) VALUES (%s, %s, %s)'
    ___variables = (
        insertedID,
        userID,
        friendID,
    )
    create_cursor.execute(___sql_statement, ___variables)
    mariadb_connection.commit()
    return Response(status=200)

@app.route('/message/get', methods=['POST'])
def get():
    ___requestBody = json.loads(request.get_data())

    ___sql_statement = 'SELECT id from user where Name=%s;'
    ___variables = (
        ___requestBody["friend"],
    )
    create_cursor.execute(___sql_statement, ___variables)
    friendID = create_cursor.fetchone()
    friendID = friendID[0]

    ___sql_statement = 'SELECT id from user where Name=%s;'
    ___variables = (
        ___requestBody["user"],
    )
    create_cursor.execute(___sql_statement, ___variables)
    userID = create_cursor.fetchone()
    userID = userID[0]

    ___sql_statement = 'SELECT MessageID from messageuser where UserID=%s AND User2ID=%s OR UserID=%s AND User2ID=%s;'
    ___variables = (
        userID,
        friendID,
        friendID,
        userID,
    )
    create_cursor.execute(___sql_statement, ___variables)
    messageIdList = create_cursor.fetchall()
    
    list = []
    for item in messageIdList:
        list.append(item[0])
    print(list)
    messageList = []
    for id in tuple(list):
        ___sql_statement = 'SELECT * from message where id=%s;'
        ___variables=(
            id,
        )
        create_cursor.execute(___sql_statement, ___variables)
        ___message = create_cursor.fetchall()
        messageList.append(___message)
    print(messageList)
    return messageList

if __name__ == '__main__':
    #development server
    app.debug = True
    app.run(host="0.0.0.0", port="3002")
    
    #production
    #http_server = WSGIServer(('', 3002), app)
    #http_server.serve_forever()