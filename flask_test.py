from flask import Flask, request
from uuid import uuid4
import json

app = Flask(__name__)

@app.route('/')
def index():
    res = json.dumps(uuid4().hex)
    return res, 200


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
