'''
  ' A flask microservice that serves an arbitrary JSON object at /batch
  ' USAGE: `sudo pip install json; export FLASK_ENV=development; flask run`
'''

# Setup flask
from flask import Flask, Response
app = Flask(__name__)

# Other imports
import json


# Most basic route for reference
@app.route("/")
def hello():
    return "Hello Flask"

# Serves an arbitrary JSON object
@app.route("/batch")
def batch():
    data = {
        'Mark': 'data1',
        'Michael': 'data2',
        'Daniel': 'data3'
    }
    return Response(json.dumps(data), status=200, mimetype='application/json')


# Serve application
if __name__ == '__main__':
    app.run()
