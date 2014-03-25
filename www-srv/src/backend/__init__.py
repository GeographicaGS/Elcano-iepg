from flask import Flask,jsonify

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 32*1024*1024
app.config.update(
    DEBUG=True,
    SECRET_KEY='IuwqOl6;a#RF1a',    
)

import user
import document
import label
import highlight
import new

@app.route('/', methods = ['GET'])                                            
def alive():
    return jsonify( { "status" : "running"})
