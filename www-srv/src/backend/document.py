"""

Document backend

"""

from backend import app
from flask import jsonify,request,session
from model.documentmodel import DocumentModel
from utils import auth
import config
from werkzeug.utils import secure_filename
import werkzeug
import os
import hashlib
import time
import utils

@app.route('/document', methods=['POST'])
@auth
def newDocument():
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
    m = DocumentModel()

    r = m.getDocumentList(request.json, config.cfgBackend["DocumentListLength"])

    return(jsonify({"results": r}))


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

@app.route("/document/<int:id_document>", methods=["GET"])
@auth
def getDocument(id_document):
    m = DocumentModel()

    # Get data from Database
    d = m.getDocument(id_document)
    pdfs_es = m.getDocumentPDFs(id_document,"es")
    pdfs_en = m.getDocumentPDFs(id_document,"en")
    authors = m.getDocumentAuthors(id_document)
    labels_es = m.getDocumentLabels(id_document,"es")
    labels_en = m.getDocumentLabels(id_document,"en")

    json = {
        "id" : d["id_document"],
        "title_en" : utils.htmlspecialchars(d["title_en"]),
        "title_es" : utils.htmlspecialchars(d["title_es"]),
        "theme_en" : utils.htmlspecialchars(d["theme_en"]),
        "theme_es": utils.htmlspecialchars(d["theme_es"]),
        "description_en" : utils.htmlspecialchars(d["description_en"]),
        "description_es" : utils.htmlspecialchars(d["description_es"]),
        "link_es" : utils.htmlspecialchars(d["link_es"]),
        "link_en" : utils.htmlspecialchars(d["link_en"]),
        "published" : True if d["published"] == "t" else False,
        "last_edit_id_user" : d["last_edit_id_user"],
        "last_edit_time" : d["last_edit_time"],
        # Deprecated, now the id mapping for backbone is done by the client
        #"pdfs_es" : map(lambda p: utils.renameKeyDict(p,"id_pdf","id"), pdfs_es),
        #"pdfs_en" : map(lambda p: utils.renameKeyDict(p,"id_pdf","id"), pdfs_es),
        #"labels_es": map(lambda p: utils.renameKeyDict(p,"id_label","id"), labels_es),
        #"labels_en": map(lambda p: utils.renameKeyDict(p,"id_label","id"), labels_en),
        #"authors" : map(lambda p: utils.renameKeyDict(p,"id_author","id"), authors)
        "pdfs_es" : pdfs_es,
        "pdfs_en" : pdfs_en,
        "labels_es" : labels_es,
        "labels_en" : labels_en,
        "authors" : authors

    }

    return jsonify(json)
