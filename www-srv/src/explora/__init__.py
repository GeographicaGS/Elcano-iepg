from flask import Flask,jsonify
from common.config import explora as config

app = Flask(__name__)
app.config.update(
    DEBUG=True
)

app.config["SECRET_KEY"] = config["SECRET_KEY"]

import country
import ranking

@app.route('/', methods = ['GET'])
def alive():
    return jsonify( { "status" : "running"})
