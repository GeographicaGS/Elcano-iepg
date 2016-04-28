from flask import Flask,jsonify
from common.config import SECRET_KEY

app = Flask(__name__)
app.debug = True
app.config["MAX_CONTENT_LENGTH"] = 32*1024*1024
app.config["SECRET_KEY"] = SECRET_KEY

import user
import document
import label
import highlight
import new
#import locale
# import maplex
import engine
import calculus

@app.route('/', methods = ['GET'])                                            
def alive():
    return jsonify( { "status" : "running"})

#locale.setlocale(locale.LC_ALL, "es_ES.UTF-8")
