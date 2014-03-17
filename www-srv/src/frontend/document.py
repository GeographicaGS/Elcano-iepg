# coding=UTF8

"""

Frontend document services.


"""
from frontend import app
from flask import jsonify,request
from model.documentmodel import DocumentModel
from model.labelmodel import LabelModel


@app.route('/document/label/<string:lang>', methods=['GET'])
def getDocumentLabels(lang):
    """Gets the labels for filters in document catalog. 'lang' must be en/es."""
    m = LabelModel()
    return(jsonify({"labels": m.getLabels(lang)}))


@app.route('/document/<int:idDocument>/<string:lang>', methods=['GET'])
def getDocument(idDocument, lang):
    """Gets details of a document. Uses URL arguments:

      idDocument: mandatory, ID of the requested document
      lang: mandatory, language for document's metadata
    """
    m = DocumentModel()
    pdf = m.getDocumentPdf(idDocument)
    doc = m.getDocumentFrontend(idDocument, lang)

    return(jsonify({"details": doc, "pdf": pdf}))
