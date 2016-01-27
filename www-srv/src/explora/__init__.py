from flask import Flask,jsonify
from common.config import SECRET_KEY

app = Flask(__name__)
app.debug = True
app.config["SECRET_KEY"] = SECRET_KEY

import country
import ranking
import quotes

@app.route('/', methods = ['GET'])
def alive():
    return jsonify( { "status" : "running"})
