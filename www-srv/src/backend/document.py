from backend import app
from flask import jsonify,request,session
from model.documentmodel import DocumentModel
# import utils
# import hashlib

@app.route('/document/test', methods=['GET'])
def testDocument():
    return jsonify({"ie": "jej"})

@app.route('/document/new', methods=['POST'])
def newDocument():
    return(jsonify({"User": request.json['user']['email']}))

