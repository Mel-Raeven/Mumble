from flask import Flask, request
from flask_cors import CORS
from gevent.pywsgi import WSGIServer
import requests

app = Flask(__name__)
CORS(app)

@app.route('/auth', methods=['POST'])
def func():
    ___requestBody = request.get_data(as_text=True)
    print (___requestBody)
    x = requests.post('http://127.0.0.1:3001/auth', ___requestBody)
    return x.content


if __name__ == '__main__':
    #development
    #app.debug = True
    #app.run(port="3000")
    
    #production
    http_server = WSGIServer(('', 3000), app)
    http_server.serve_forever()