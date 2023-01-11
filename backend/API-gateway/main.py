from flask import Flask, request
from flask_cors import CORS
from gevent.pywsgi import WSGIServer
import requests
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-s", "--server", dest = "servermode", default = "dev", help="start dev server or production")

args = parser.parse_args()

app = Flask(__name__)
CORS(app)

@app.route('/auth', methods=['POST'])
def auth():
    ___requestBody = request.get_data(as_text=True)
    print (___requestBody)
    x = requests.post('http://20.6.0.7:3001/auth', ___requestBody)
    return x.content

@app.route('/register', methods=['POST'])
def register():
    ___requestBody = request.get_data(as_text=True)
    print(___requestBody)
    x = requests.post('http://20.6.0.7:3001/register', ___requestBody)
    return x.content

@app.route('/message/post', methods=['POST'])
def postMessage():
    ___requestBody = request.get_data(as_text=True)
    print(___requestBody)
    x = requests.post('http://20.6.0.8:3002/message/post', ___requestBody)
    return x.content

@app.route('/message/get', methods=['POST'])
def getMessage():
    ___requestBody = request.get_data(as_text=True)
    print(___requestBody)
    x = requests.post('http://20.6.0.8:3002/message/get', ___requestBody)
    return x.content

@app.route('/friend/request', methods=['POST'])
def requestFriend():
    ___requestBody = request.get_data(as_text=True)
    print(___requestBody)
    x = requests.post('http://20.6.0.9:3003/friend/request', ___requestBody)
    return x.content

@app.route('/friend/list', methods=['POST'])
def requestFriendList():
    ___requestBody = request.get_data(as_text=True)
    print(___requestBody)
    x = requests.post('http://20.6.0.9:3003/friend/list', ___requestBody)
    return x.content

if __name__ == '__main__':
    #development
    if args.servermode == "dev":
        print("running dev server")
        app.debug = True
        app.run(port="3000")
    
    #production
    elif args.servermode == "production":
        print("running production server")
        http_server = WSGIServer(('', 3000), app)
        http_server.serve_forever()