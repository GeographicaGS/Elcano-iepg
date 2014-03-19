# coding=UTF8

"""

Frontend document services.


"""
from frontend import app
from flask import jsonify,request
from model.documentmodel import DocumentModel
from model.labelmodel import LabelModel

import twitter_helper


@app.route('/document/label/<string:lang>', methods=['GET'])
def getDocumentLabels(lang):
    """Gets the labels for filters in document catalog. 'lang' must be en/es."""
    m = LabelModel()
    return(jsonify({"results": m.getLabels(lang)}))


@app.route('/document/<int:idDocument>/<string:lang>', methods=['GET'])
def getDocument(idDocument, lang):
    """Gets details of a document. Uses URL arguments:

      idDocument: mandatory, ID of the requested document
      lang: mandatory, language for document's metadata
    """
    m = DocumentModel()
    pdf = m.getDocumentPdf(idDocument)
    doc = m.getDocumentFrontend(idDocument, lang)

    target_authors = []
    for a in doc["authors"]:
        twitter = twitter_helper.getUserInfo(a)
        if twitter:
            target_authors.append({
                "name" : twitter.name,
                "description" : twitter.description,
                "image" : twitter.profile_image_url_https.replace("_normal","_bigger")
            })
    
    doc["authors"] = target_authors
    

    return(jsonify({"details": doc, "pdf": pdf}))
