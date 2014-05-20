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
import locale
import maplex
import engine

@app.route('/', methods = ['GET'])                                            
def alive():
    return jsonify( { "status" : "running"})

locale.setlocale(locale.LC_ALL, "es_ES.UTF-8")
