from backend import app
from flask import jsonify,request,session
from model.documentmodel import DocumentModel
from utils import auth
from werkzeug.utils import secure_filename
import werkzeug
import os
import hashlib
import time

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


def allowedFilePDF(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1] in ["PDF","pdf"]
           

@app.route("/document/upload_pdf",methods=["POST"])
@auth
def uploadPDF():
    try:
        file = request.files['file']
        if file and allowedFilePDF(file.filename):
            filename = secure_filename(file.filename)
            filename, fileExtension = os.path.splitext(filename)
            filename = hashlib.md5(str(time.time())+ session["email"]).hexdigest() + fileExtension
            
            file.save(os.path.join(app.config['tmpFolder'], filename))
            
            return jsonify(  {"filename": filename} )  
        
        return jsonify(  {"error": -1} )    
    
    except werkzeug.exceptions.UnsupportedMediaType:
        return jsonify(  {"error": -2} )
    
    except werkzeug.exceptions.RequestEntityTooLarge:
        return jsonify(  {"error": -3} )
    


