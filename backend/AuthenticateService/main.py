from flask import Flask, request
import jwt
from cryptography.hazmat.primitives import serialization
import json
from gevent.pywsgi import WSGIServer

app = Flask(__name__)

@app.route('/auth', methods=['POST'])
def func():
    ___requestBody = json.loads(request.get_data())
    print (___requestBody)
    
    token = 'test'
    payload_data = {
    "email": ___requestBody["email"],
    "username": "empty"
    }
    algorithm = 'ES256'
    key = loadKey('.key/private.ec.key')

    token = createToken(payload_data, key, algorithm)
    decodeToken(token, key, algorithm)
    return token

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
    #app.debug = True
    #app.run(host="0.0.0.0", port="3001")
    
    #production
    http_server = WSGIServer(('', 3001), app)
    http_server.serve_forever()