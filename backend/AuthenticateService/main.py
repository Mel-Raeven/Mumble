from flask import Flask, request
import jwt
from cryptography.hazmat.primitives import serialization
import json

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
    
    key = loadKey()
    print(key)
    
    token = jwt.encode(
    payload=payload_data,
    key=key,
    algorithm='ES256'
    )
    print(token)
    return token

def loadKey():
    private_key = open('.key/private.ec.key', 'r').read()
    key = serialization.load_pem_private_key(private_key.encode(), password=None)
    return key


if __name__ == '__main__':
    app.debug = True
    app.run(port="3001")