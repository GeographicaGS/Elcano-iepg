"""

Document backend

"""

from backend import app
from flask import jsonify,request,session
from model.documentmodel import DocumentModel
from backend.utils import auth, prettyNumber
import config
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

@app.route('/document', methods=['GET'])
@auth
def getDocumentList():
    """Gets a slice of a document list."""
    m = DocumentModel()
    out = []

    totalSize = m.getDocumentListSize(request.json)

    print(request.json["offset"])

    for doc in m.getDocumentList(request.json, config.cfgBackend["DocumentListLength"]):
        thisDoc = dict()
        thisDoc["english"]=False
        thisDoc["spanish"]=False
        
        if doc["title_en"]!="" and doc["theme_en"]!="" and doc["description_en"]!="":
            thisDoc["english"]=True
            
        if doc["title_es"]!="" and doc["theme_es"]!="" and doc["description_es"]!="":
            thisDoc["spanish"]=True

        thisDoc["title"] = doc["title"]
        t = doc["time"]
        thisDoc["time"] = prettyNumber(t.year)+"/"+prettyNumber(t.month)+ \
                          "/"+prettyNumber(t.day)+" - "+prettyNumber(t.hour)+ \
                          ":"+prettyNumber(t.minute)

        thisDoc["published"] = False        

        if doc["published"] is not None:
            thisDoc["published"] = True

        authors = []
        for author in m.getDocumentAuthors(doc["id"]):
            authors.append(author["twitter_user"])

        thisDoc["authors"] = authors

        thisDoc["attachments"] = False
        if doc["link_es"]!="" or doc["link_en"]!="" or \
           len(m.getDocumentPdf(doc["id"]))>0:
            thisDoc["attachments"] = True

        out.append(thisDoc)

    return(jsonify({"results": {"listSize": totalSize, "page": request.json["offset"], \
                                "documentList": out}}))


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
