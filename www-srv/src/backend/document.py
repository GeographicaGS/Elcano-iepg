from backend import app
from flask import jsonify,request,session
from model.documentmodel import DocumentModel
from utils import auth

@app.route('/document', methods=['POST'])
@auth
def newDocument():
    app.logger.info(request.json)
    m = DocumentModel()

    return(jsonify({"id": m.createDocument(request.json)}))

@app.route('/document', methods=['PUT'])
@auth
def editDocument():
    app.logger.info(request.json)
    m = DocumentModel()

    return(jsonify({"id": m.editDocument(request.json)}))

@app.route('/document', methods=['DELETE'])
@auth
def deleteDocument():
    app.logger.info(request.json)
    m = DocumentModel()

    return(jsonify({"id": m.deleteDocument(request.json)}))





@app.route('/uploadpdf', methods=['POST'])
@auth
def uploadPdf():
    pass
