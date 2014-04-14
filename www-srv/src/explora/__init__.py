from flask import Flask,jsonify
import config
app = Flask(__name__)
app.config.update(
    DEBUG=True
)

app.config["SECRET_KEY"] = config.cfgExplora["SECRET_KEY"]

import country

@app.route('/', methods = ['GET'])                                            
def alive():
    return jsonify( { "status" : "running"})
