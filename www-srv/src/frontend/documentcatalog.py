# coding=UTF8

"""

Frontend document catalog services.


"""
from frontend import app
from flask import jsonify,request
from model.documentmodel import DocumentModel
from model.labelmodel import LabelModel
import config
import cons


@app.route('/documentcatalog', methods=['GET'])
def getDocumentCatalog():
    """Gets a slice of a document list. Uses URL arguments:

      offset: mandatory, page to present
      lang: mandatory, language (en / es)
      search: optional, search criteria
      filterbylabel: optional, comma-separated list of labels ID to filter with

    """
    if request.args["lang"] not in cons.lang:
        return(jsonify(cons.errors["-1"]))
    
    if not request.args["offset"].isdigit():
        return(jsonify(cons.errors["-3"]))

    if "filterbylabel" in request.args:
        labels = request.args["filterbylabel"].split(",")
        print(labels)
        for i in labels:
            if not i.isdigit():
                return(jsonify(cons.errors["-5"]))

    m = DocumentModel()
    l = LabelModel()
    langLabels = l.getLabels(request.args["lang"])

    

    fsearch = request.args["search"] if "search" in request.args else None

    totalSize = m.getDocumentCatalogSize(search=fsearch)
    docs = m.getDocumentCatalog(request.args["offset"], config.cfgFrontend["DocumentListLength"], \
                             request.args["lang"], search=fsearch)

    return(jsonify({"results": docs, "listSize": totalSize}))



