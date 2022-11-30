from flask import Flask, request
from flask_cors import CORS
from gevent.pywsgi import WSGIServer
import requests

app = Flask(__name__)
CORS(app)

@app.route('/auth', methods=['POST'])
def auth():
    ___requestBody = request.get_data(as_text=True)
    print (___requestBody)
    x = requests.post('http://127.0.0.1:3001/auth', ___requestBody)
    return x.content

@app.route('/register', methods=['POST'])
def register():
    ___requestBody = request.get_data(as_text=True)
    print(___requestBody)
    x = requests.post('http://127.0.0.1:3001/register', ___requestBody)
    return x.content

@app.route('/message/post', methods=['POST'])
def postMessage():
    ___requestBody = request.get_data(as_text=True)
    print(___requestBody)
    x = requests.post('http://127.0.0.1:3002/message/post', ___requestBody)
    return x.content

@app.route('/message/get', methods=['POST'])
def getMessage():
    ___requestBody = request.get_data(as_text=True)
    print(___requestBody)
    x = requests.post('http://127.0.0.1:3002/message/get', ___requestBody)
    return x.content

if __name__ == '__main__':
    #development
    app.debug = True
    app.run(port="3000")
    
    #production
    #http_server = WSGIServer(('', 3000), app)
    #http_server.serve_forever()