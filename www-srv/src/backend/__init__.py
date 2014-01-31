from flask import Flask,jsonify
app = Flask(__name__)
app.config.update(
    DEBUG=True,
    SECRET_KEY='IuwqOl6;a#RF1a',    
)

import user

@app.route('/', methods = ['GET'])                                            
def alive():
    return jsonify( { "status" : "running"})
