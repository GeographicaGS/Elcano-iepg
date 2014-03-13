# coding=UTF8

"""

Frontend document catalog services.


"""
from frontend import app
from flask import jsonify,request
from model.documentmodel import DocumentModel
import config


@app.route('/documentcatalog', methods=['GET'])
def getDocumentCatalog():
    """Gets a slice of a document list. Uses URL arguments:

      offset: mandatory, page to present
      lang: mandatory, language
      search: optional, search criteria

    """
    m = DocumentModel()
    search = request.args["search"] if "search" in request.args else None
    totalSize = m.getDocumentCatalogSize(search=search)
    docs = m.getDocumentCatalog(request.args["offset"], config.cfgFrontend["DocumentListLength"], \
                             request.args["lang"], search=search)

    return(jsonify({"results": docs}))


