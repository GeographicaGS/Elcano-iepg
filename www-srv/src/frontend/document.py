# coding=UTF8

"""

Frontend document services.


"""
from frontend import app
from flask import jsonify,request,send_file,make_response
from model.documentmodel import DocumentModel
from model.labelmodel import LabelModel
import cons
import helpers
import config


@app.route('/download/pdf', methods=['GET'])
def downloadPdf():
    """Downloads a PDF. request.args:

    idPdf: mandatory, PDF ID.

    """
    m = DocumentModel()
    pdf = m.getPdfData(request.args["idPdf"])
    
    return(send_file(config.cfgFrontend["mediaFolder"]+"/"+pdf["hash"]+".pdf", \
                     mimetype="application/pdf", attachment_filename=pdf["pdf_name"]+".pdf", \
                     as_attachment=True))


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

      TODO: revisar los coalesce. Según lo último que hablamos, se
      íban a rellenar todos los campos o el documento era impublicable.

      TODO: cambiar los errores a make_response.
    """
    if lang not in cons.lang:
        return(jsonify(cons.errors["-1"]))

    out = dict()

    m = DocumentModel()
    authorsData = m.getDocumentAuthors(idDocument)
    authors = []

    for a in authorsData:
        authors.append(helpers.authorHelper(a, lang))

    out["authors"] = authors
    labels = m.getDocumentLabels(idDocument, lang)
    out["labels"]=labels
    pdf = m.getDocumentPdf(idDocument)
    out["pdf"]=pdf

    doc = m.getDocumentData(idDocument)
    if doc==None:
        return make_response(jsonify({"error": "Document not found"}), 404)

    out["id"] = doc["id_document"]
    out["time"] = doc["last_edit_time"]
    if lang=="en":
        out["description"] = helpers.coalesce([doc["description_en"], doc["description_es"]])
        out["theme"] = helpers.coalesce([doc["theme_en"], doc["theme_es"]])
        out["title"] = helpers.coalesce([doc["title_en"], doc["title_es"]])

        if doc["link_en"]!=None:
            out["link"] = doc["link_en"]
            out["link_lang"] = "en"
        elif doc["link_es"]!=None:
            out["link"] = doc["link_es"]
            out["link_lang"] = "es"

    else:
        out["description"] = helpers.coalesce([doc["description_es"], doc["description_en"]])
        out["theme"] = helpers.coalesce([doc["theme_es"], doc["theme_en"]])
        out["title"] = helpers.coalesce([doc["title_es"], doc["title_en"]])

        if doc["link_es"]!=None:
            out["link"] = doc["link_es"]
            out["link_lang"] = "es"
        elif doc["link_en"]!=None:
            out["link"] = doc["link_en"]
            out["link_lang"] = "en"

    return(jsonify(out))
