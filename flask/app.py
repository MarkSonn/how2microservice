'''
  ' A flask microservice that serves an arbitrary JSON object at /batch
  ' USAGE: `sudo pip install json; export FLASK_ENV=development; flask run`
'''

# Setup flask
from flask import Flask, Response, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

port = 80


# Other imports
import json


# Most basic route for reference
@app.route("/")
def hello():
    return "Hello Flask"

# Serves an arbitrary JSON object
@app.route("/batch")
def batch():
    data = [
        {'sku': 'lol6969', 'isCheckedOut': False},
        {'sku': 'rofl1337', 'isCheckedOut': False},
        {'sku': 'hehe1234', 'isCheckedOut': False},
        {'sku': '306361.3', 'isCheckedOut': False},
        {'sku': '306361.4', 'isCheckedOut': False},
        {'sku': '306361.5', 'isCheckedOut': False},
        {'sku': '306361.1', 'isCheckedOut': False},
        {'sku': '15111111', 'isCheckedOut': False},
        {'sku': '16111111', 'isCheckedOut': False},
        {'sku': '17111111', 'isCheckedOut': False},
        {'sku': '18111111', 'isCheckedOut': False},
        {'sku': '19111111', 'isCheckedOut': False},
        {'sku': '11211111', 'isCheckedOut': False},
        {'sku': '11311111', 'isCheckedOut': False},
        {'sku': '11411111', 'isCheckedOut': False},
        {'sku': '11511111', 'isCheckedOut': False},
        {'sku': '11611111', 'isCheckedOut': False},
        {'sku': '11711111', 'isCheckedOut': False},
        {'sku': '11811111', 'isCheckedOut': False},
        {'sku': '11911111', 'isCheckedOut': False},
        {'sku': '11111111', 'isCheckedOut': False},
        {'sku': '11121111', 'isCheckedOut': False},
        {'sku': '11131111', 'isCheckedOut': False},
        {'sku': '11141111', 'isCheckedOut': False},
        {'sku': '11151111', 'isCheckedOut': False},
        {'sku': '11161111', 'isCheckedOut': False},
        {'sku': '11171111', 'isCheckedOut': False},
        {'sku': '11181111', 'isCheckedOut': False},
        {'sku': '111191111', 'isCheckedOut': False}
    ]
    return Response(json.dumps(data), status=200, mimetype='application/json')

@app.route("/receive", methods=['POST'])
def receive():
    content = request.get_json()
    print (content)
    return Response() # flask must have a response object returned

# Serve application
if __name__ == '__main__':
    app.run(host = "0.0.0.0", port = port, debug = True)
