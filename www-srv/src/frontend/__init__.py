from flask import Flask,jsonify
from common.config import SECRET_KEY

app = Flask(__name__)
app.config["SECRET_KEY"] = SECRET_KEY

import home
import documentcatalog
import document
import new
import country
#import locale
import downloads


@app.route('/', methods = ['GET'])                                            
def alive():
    return jsonify( { "status" : "running"})

#locale.setlocale(locale.LC_ALL, "es_ES.UTF-8")
