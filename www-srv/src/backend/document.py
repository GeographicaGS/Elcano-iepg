# coding=UTF8

"""

Document backend

"""
from backend import app
from flask import jsonify,request,session,send_file
from model.documentmodel import DocumentModel
from backend.utils import auth, prettyNumber
import config
from werkzeug.utils import secure_filename
import werkzeug
import os
import hashlib
import time
import cons


@app.route('/download/pdf', methods=['GET'])
@auth
def downloadPdf():
    """Downloads a PDF. request.args:

    idPdf: mandatory, PDF ID.

    """
    m = DocumentModel()
    pdf = m.getPdfData(request.args["idPdf"])
    
    return(send_file(config.cfgBackend["mediaFolder"]+"/"+pdf["hash"]+".pdf", \
                     mimetype="application/pdf", attachment_filename=pdf["pdf_name"]+".pdf", \
                     as_attachment=True))


@app.route('/document', methods=['POST'])
@auth
def newDocument():
    """Creates a document. Needs a JSON in the form:

    {
      "title_es": "Test document ES",
      "title_en": "Test document EN",
      "labels_es": [{"id": "1", "label": "Label A"},
                    {"id": "2", "label": "Label B"},
                    {"id": "4", "label": "Label c"}],
      "labels_en": [{"id": "1", "label": "Label A"},
                    {"id": "3", "label": "Label B"},
                    {"id": "4", "label": "Label c"}],
      "theme_es": "Theme ES",
      "theme_en": "Theme EN",
      "description_es": "Description ES",
      "description_en": "Description EN",
      "authors": [{"twitter_user": "@iliana"}, {"twitter_user": "@jpperez"}, 
                  {"name": "Charles Powell", "position_en": "Director of the Elcano Royal Institute",
                   "position_es": "Director del Real Instituto Elcano"}],
      "link_es": "Link ES",
      "link_en": "Link EN",
      "pdfs_es": [{"name": "pdf_es_1", "hash": "8383e83838283e838238"}, 
                  {"name": "pdf_es_2", "hash": "8383e83838283e838238"}, 
                  {"name": "pdf_es_3", "hash": "8383e83838283e838238"}],
      "pdfs_en": [{"name": "pdf_en_1", "hash": "8383e83838283e838238"}, 
                  {"name": "pdf_en_2", "hash": "8383e83838283e838238"}, 
                  {"name": "pdf_en_3", "hash": "8383e83838283e838238"}]
    }"""
    m = DocumentModel()

    try: 
        for f in request.json["pdfs_en"]:
            movePdfFile(f["hash"])

        for f in request.json["pdfs_es"]:
            movePdfFile(f["hash"])

        out = m.createDocument(request.json)
        return(jsonify({"id": out}))
    except: 
        return(jsonify(cons.errors["-1"]))


@app.route('/document/<int:id_document>', methods=['PUT'])
@auth
def editDocument(id_document):
    """

    Edits a document. Gets the id_document in the URL, and upload this
    JSON:

    {
      "title_es": "Test document ES",
      "title_en": "Test document EN",
      "labels_es": [{"id": "1", "label": "Label A"},
                    {"id": "2", "label": "Label B"},
                    {"id": "4", "label": "Label c"}],
      "labels_en": [{"id": "1", "label": "Label A"},
                    {"id": "3", "label": "Label B"},
                    {"id": "4", "label": "Label c"}],
      "theme_es": "Theme ES",
      "theme_en": "Theme EN",
      "description_es": "Description ES",
      "description_en": "Description EN",
      "authors": ["@iliana", "@jpperez"],
      "link_es": "Link ES",
      "link_en": "Link EN",
      "pdfs_es": [{"name": "pdf_es_1", "hash": "8383e83838283e838238"}, 
                  {"name": "pdf_es_2", "hash": "8383e83838283e838238"}, 
                  {"name": "pdf_es_3", "hash": "8383e83838283e838238"}],
      "pdfs_en": [{"name": "pdf_en_1", "hash": "8383e83838283e838238"}, 
                  {"name": "pdf_en_2", "hash": "8383e83838283e838238"}, 
                  {"name": "pdf_en_3", "hash": "8383e83838283e838238"}],
      "published": "True"
    }

    """
    m = DocumentModel()
    oldDocPdfEn = map(lambda p: p["hash"], m.getDocumentPdf(id_document, "en"))
    oldDocPdfEs = map(lambda p: p["hash"], m.getDocumentPdf(id_document, "es"))
    newDocPdfEn = map(lambda p: p["hash"], request.json["pdfs_en"])
    newDocPdfEs = map(lambda p: p["hash"], request.json["pdfs_es"])
    newEn = [v for v in newDocPdfEn if v not in oldDocPdfEn]
    newEs = [v for v in newDocPdfEs if v not in oldDocPdfEs]
    delEn = [v for v in oldDocPdfEn if v not in newDocPdfEn]
    delEs = [v for v in oldDocPdfEs if v not in newDocPdfEs]

    for f in newEn:
        movePdfFile(f)

    for f in newEs:
        movePdfFile(f)

    for f in delEn:
        m.deletePdf(id_document, f)
        deletePdfFile(f)

    for f in delEs:
        m.deletePdf(id_document, f)
        deletePdfFile(f)

    out = m.editDocument(id_document, request.json, newEn, newEs)

    return(jsonify({"results": {"id": out}}))


def deletePdfFile(hash):
    """Deletes a PDF file from the filesystem."""
    file = config.cfgBackend["mediaFolder"]+"/"+hash+".pdf"
    os.remove(file)


def movePdfFile(hash):
    """Moves a PDF file within the filesystem."""
    origin = config.cfgBackend["tmpFolder"]+"/"+hash+".pdf"
    destination = config.cfgBackend["mediaFolder"]+"/"+hash+".pdf"
    app.logger.info(origin)
    app.logger.info(destination)
    os.rename(origin, destination)


@app.route('/document/<int:id_document>', methods=['DELETE'])
@auth
def deleteDocument(id_document):
    """Deletes a document. Just state the id_document in the URL."""
    m = DocumentModel()

    return(jsonify({"results": {"id": m.deleteDocument(id_document)}}))


@app.route('/document', methods=['GET'])
@auth
def getDocumentList():
    """

    Gets a slice of a document list. Uses URL arguments:

      offset: mandatory, page to present
      search: optional, search criteria
      orderbyfield: optional, set by default to title
      orderbyorder: optional, asc / desc, set by default to asc

    """
    m = DocumentModel()
    out = []

    search = request.args["search"] if "search" in request.args else None
    orderbyfield = request.args["orderbyfield"] if "orderbyfield" in request.args else "title"
    orderbyorder = request.args["orderbyorder"] if "orderbyorder" in request.args else "asc"

    if "orderbyorder" in request.args:
        if request.args["orderbyorder"] not in cons.orderBy:
            return(jsonify(cons.errors["-2"]))

    if "orderbyfield" in request.args:
        if request.args["orderbyfield"] not in cons.documentOrderFields:
            return(jsonify(cons.errors["-3"]))

    totalSize = m.getDocumentListSize(search=search)
    docs = m.getDocumentList(request.args["offset"], config.cfgBackend["DocumentListLength"], \
                             search=search, orderByField=orderbyfield, orderByOrder=orderbyorder)

    for doc in docs:
        thisDoc = dict()
        thisDoc["id"] = doc["id"]
        thisDoc["english"]=False
        thisDoc["spanish"]=False
        
        if doc["title_en"]!="" and doc["theme_en"]!="" and doc["description_en"]!="":
            thisDoc["english"]=True
            
        if doc["title_es"]!="" and doc["theme_es"]!="" and doc["description_es"]!="":
            thisDoc["spanish"]=True

        thisDoc["title"] = doc["title"]
        thisDoc["time"] = doc["time"]
        thisDoc["published"] = doc["published"]

        authors = []
        for author in m.getDocumentAuthors(doc["id"]):
            authors.append(author["twitter_user"])

        thisDoc["authors"] = authors
        thisDoc["attachments"] = False
        if len(m.getDocumentPdf(doc["id"]))>0:
            thisDoc["attachments"] = True

        thisDoc["links"] = False
        if doc["link_es"]!=None or doc["link_en"]!=None:
            thisDoc["links"] = True

        out.append(thisDoc)

    return(jsonify({"results": {"listSize": totalSize, "page": request.args["offset"], \
                                "documentList": out}}))


def allowedFilePDF(filename):
    """File extensions allowed to upload."""
    return '.' in filename and \
        filename.rsplit('.', 1)[1] in ["PDF","pdf"]
           

@app.route("/document/upload_pdf",methods=["POST"])
@auth
def uploadPDF():
    """Uploads a file."""
    try:
        file = request.files['file']
        if file and allowedFilePDF(file.filename):
            filename = secure_filename(file.filename)
            filename, fileExtension = os.path.splitext(filename)
            filename = hashlib.md5(str(time.time())+ session["email"]).hexdigest() 

            file.save(os.path.join(config.cfgBackend['tmpFolder'], filename + ".pdf"))
            return jsonify(  {"filename": filename} )  
        
        return jsonify(  {"error": -1} )    
    
    except werkzeug.exceptions.UnsupportedMediaType:
        return jsonify(  {"error": -2} )
    
    except werkzeug.exceptions.RequestEntityTooLarge:
        return jsonify(  {"error": -3} )


@app.route("/document/<int:id_document>", methods=["GET"])
@auth
def getDocument(id_document):
    """

    Gets a document. Just state the id_document in the URL.

    """
    m = DocumentModel()

    # Get data from Database
    d = m.getDocumentBackend(id_document)
    pdfs_es = m.getDocumentPdf(id_document,"es")
    pdfs_en = m.getDocumentPdf(id_document,"en")
    authors = m.getDocumentAuthors(id_document)
    labels_es = m.getDocumentLabels(id_document,"es")
    labels_en = m.getDocumentLabels(id_document,"en")

    json = {
        "id" : d["id_document"],
        "title_en" : d["title_en"],
        "title_es" : d["title_es"],
        "theme_en" : d["theme_en"],
        "theme_es": d["theme_es"],
        "description_en" : d["description_en"],
        "description_es" : d["description_es"],
        "link_es" : d["link_es"],
        "link_en" : d["link_en"],
        "published" : True if d["published"] == "t" else False,
        "last_edit_id_user" : d["last_edit_id_user"],
        "last_edit_time" : d["last_edit_time"],
        "pdfs_es" : pdfs_es,
        "pdfs_en" : pdfs_en,
        "labels_es" : labels_es,
        "labels_en" : labels_en,
        "authors" : authors
    }

    return jsonify(json)


@app.route("/document/<int:id_document>/toggle_publish", methods=["GET"])
@auth
def togglePublish(id_document):
    """Toggles the published status of a document."""
    m = DocumentModel()
    status = m.togglePublish(id_document)

    if status==None:
        return jsonify(cons.errors["-4"])
    else:
        return jsonify({"result" : status})
