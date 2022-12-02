from flask import Flask, request, Response
import jwt
from cryptography.hazmat.primitives import serialization
import json
import bcrypt
from gevent.pywsgi import WSGIServer
import mysql.connector as mariadb

app = Flask(__name__)
mariadb_connection = mariadb.Connect(user='root', password='admin', host='192.168.178.222', port='3306', database='mumble')
create_cursor = mariadb_connection.cursor()

@app.route('/auth', methods=['POST'])
def auth():
    ___requestBody = json.loads(request.get_data())
    print (___requestBody["password"])
    ___sql_statement = 'SELECT * from user where email = %s'
    ___variables = (___requestBody["email"],)
    create_cursor.execute(___sql_statement, ___variables)
    sqlResult = create_cursor.fetchall()
    print(sqlResult[0][3])
    passwordHash = sqlResult[0][4].encode('utf-8')
    username = sqlResult[0][1]
    password = ___requestBody["password"].encode('utf-8')
    
    
    if bcrypt.checkpw(password, passwordHash):    
        payload_data = {
            "email": ___requestBody["email"],
            "username": username
        }
        algorithm = 'ES256'
        key = loadKey('.key/private.ec.key')
        token = createToken(payload_data, key, algorithm)
        decodeToken(token, key, algorithm)
        return token
    else:
        return Response(status=400)

@app.route('/register', methods=['POST'])
def register():
    ___requestBody = json.loads(request.get_data())
    salt = bcrypt.gensalt()    
    password = ___requestBody["password"].encode('utf-8')
    hashedPassword = bcrypt.hashpw(password, salt)
    ___sql_statement = 'INSERT INTO user (Name, Salt, SaltedHash, email) VALUES (%s, %s, %s, %s)'
    ___variables = (
        ___requestBody["username"],
        salt,
        hashedPassword,
        ___requestBody["email"]
    )
    create_cursor.execute(___sql_statement, ___variables)
    mariadb_connection.commit()
    return Response(status=200)

def loadKey(path):
    private_key = open(path, 'r').read()
    key = serialization.load_pem_private_key(private_key.encode(), password=None)
    return key

def createToken(payload, key, algorithm):
    token = jwt.encode(
        payload=payload,
        key=key,
        algorithm=algorithm
    )
    return token

def decodeToken(token, key, algorithm):
    decoded = jwt.decode(token, key, algorithm)
    return decoded

if __name__ == '__main__':
    #development server
    app.debug = True
    app.run(host="0.0.0.0", port="3001")
    
    #production
    #http_server = WSGIServer(('', 3001), app)
    #http_server.serve_forever()