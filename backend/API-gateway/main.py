from flask import Flask, request
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

@app.route('/auth', methods=['POST'])
def func():
    ___requestBody = request.get_data(as_text=True)
    print (___requestBody)
    x = requests.post('http://localhost:3001/auth', ___requestBody)
    return x.content


if __name__ == '__main__':
    app.debug = True
    app.run(port="3000")