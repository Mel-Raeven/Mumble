from flask import Flask, request, Response
import json
from gevent.pywsgi import WSGIServer
#import mysql.connector as mariadb
from peewee import *

app = Flask(__name__)
mysql_db = MySQLDatabase(database='mumble', user='root', password='admin', host='192.168.178.222', port=3306)
# mariadb_connection = mariadb.Connect(user='root', password='admin', host='192.168.178.222', port='3306', database='mumble')
# create_cursor = mariadb_connection.cursor()

class user(Model):
    Name = CharField()
    email = CharField()
    Salt = CharField()
    SaltedHash = CharField()
    class Meta:
        database = mysql_db

class friends(Model):
    User1ID = IntegerField()
    User2ID = IntegerField()
    Accepted = BooleanField()
    class Meta:
        database = mysql_db


@app.route('/friend/request', methods=['POST'])
def requestFriend():
    ___requestBody = json.loads(request.get_data())
    mysql_db.connect()
    requester = user.get(user.Name == ___requestBody["user"])
    print(___requestBody["friend"])
    friend = user.get(user.Name == ___requestBody["friend"])
    print(friend.id)
    friendRequest = friends.create(User1ID= requester.id, User2ID= friend.id, Accepted=0)
    friendRequest.save()
    mysql_db.close()
    return Response(status=200)

@app.route('/friend/list', methods=['POST'])
def listFriendRequests():
    ___requestBody = json.loads(request.get_data())
    mysql_db.connect()
    requester = user.get(user.Name == ___requestBody["user"])
    friendRequests = list(friends.select().where(friends.User2ID == requester.id))
    
    arr = []
    for requests in friendRequests:
        print(requests.User1ID)
        fromUser = user.get(user.id == requests.User1ID)
        arr.append([requests.id, fromUser.Name])
    mysql_db.close()
    return arr

# @app.route('/friend/accept', methods=['POST'])
# def accept():
#     ___requestBody = json.loads(request.get_data())
#     ___sql_statement = 'UPDATE Friends SET Accepted=1 WHERE id=%s;'
#     ___variables = (
#         ___requestBody["requestID"],
#     )
#     create_cursor.execute(___sql_statement, ___variables)
#     mariadb_connection.commit()

if __name__ == '__main__':
    #development server
    app.debug = True
    app.run(host="0.0.0.0", port="3003")
    
    #production
    #http_server = WSGIServer(('', 3003), app)
    #http_server.serve_forever()