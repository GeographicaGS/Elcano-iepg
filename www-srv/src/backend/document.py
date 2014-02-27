# coding=UTF8

"""

Document backend

"""

from backend import app
from flask import jsonify,request,session
from model.documentmodel import DocumentModel
from backend.utils import auth, prettyNumber, hsc
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
    """

    Creates a document. Needs a JSON in the form:

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
                  {"name": "pdf_en_3", "hash": "8383e83838283e838238"}]
    }

    """
    m = DocumentModel()
    out = m.createDocument(request.json)

    for f in request.json["pdfs_en"]:
        movePdfFile(f["hash"])

    for f in request.json["pdfs_es"]:
        movePdfFile(f["hash"])

    return(jsonify({"id": out}))

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
    print("Remove: ", file)
    # os.remove(file)


def movePdfFile(hash):
    """Moves a PDF file within the filesystem."""
    origin = config.cfgBackend["tmpFolder"]+"/"+hash+".pdf"
    destination = config.cfgBackend["mediaFolder"]+"/"+hash+".pdf"
    # os.rename(origin, destination)
    print("Move: ", origin, destination)


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

      offset: page to present
      search: search criteria
      orderbyfield: field to order by (currently dummy, set always to "title")
      orderbyorder: order to order by (currently dummy, set always to "asc")

    """
    m = DocumentModel()
    out = []

    totalSize = m.getDocumentListSize(request.args)

    for doc in m.getDocumentList(request.args, config.cfgBackend["DocumentListLength"]):
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

        #t = doc["time"]
        #thisDoc["time"] = prettyNumber(t.year)+"/"+prettyNumber(t.month)+ \
        #                  "/"+prettyNumber(t.day)+" - "+prettyNumber(t.hour)+ \
        #                  ":"+prettyNumber(t.minute)

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
    """

    Gets a document. Just state the id_document in the URL.

    """
    m = DocumentModel()

    # Get data from Database
    d = m.getDocument(id_document)
    pdfs_es = m.getDocumentPdf(id_document,"es")
    pdfs_en = m.getDocumentPdf(id_document,"en")
    authors = m.getDocumentAuthors(id_document)
    labels_es = m.getDocumentLabels(id_document,"es")
    labels_en = m.getDocumentLabels(id_document,"en")

    json = {
        "id" : d["id_document"],
        "title_en" : hsc(d["title_en"]),
        "title_es" : hsc(d["title_es"]),
        "theme_en" : hsc(d["theme_en"]),
        "theme_es": hsc(d["theme_es"]),
        "description_en" : hsc(d["description_en"]),
        "description_es" : hsc(d["description_es"]),
        "link_es" : hsc(d["link_es"]),
        "link_en" : hsc(d["link_en"]),
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
