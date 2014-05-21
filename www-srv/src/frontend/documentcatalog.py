# coding=UTF8

"""

Frontend document catalog services.


"""
from frontend import app
from flask import jsonify,request
from model.documentmodel import DocumentModel
from model.labelmodel import LabelModel
from model.helpers import ElcanoError
from common import config as config
from common import const as cons
from operator import itemgetter


@app.route('/documentcatalog', methods=['GET'])
def getDocumentCatalog():
    """Gets a slice of a document list. request.args:
    page: mandatory, page to present
    lang: mandatory, language (en / es)
    search: optional, search criteria
    filterbylabel: optional, comma-separated list of labels ID to filter with
    """
    m = DocumentModel()
    lang = request.args["lang"]
    page = int(request.args["page"])
    fsearch = request.args["search"] if "search" in request.args else None
    flabels = request.args["filterbylabel"] if "filterbylabel" in request.args else None

    try:
        if fsearch:
            a = m.searchInLabels(lang, fsearch)["id_document"]
            searchLabels = set(a) if a else set([])

            a = m.searchInAuthors(fsearch)["id_document"]
            authors = set(a) if a else set([])
        else:
            searchLabels = set([])
            authors = set([])

        if flabels:
            a = m.filterByLabels(lang, flabels)["id_document"]
            filterLabels = set(a) if a else set([])

        a = m.searchInDocument(lang, fsearch)["id_document"]
        docs = set(a) if a else set([])
    except ElcanoError as e:
        return jsonify(e.dict())

    if flabels:
        docs = docs.union(searchLabels).union(authors).intersection(filterLabels)
    else:
        docs = docs.union(searchLabels).union(authors)

    out=[]
    for i in list(docs):
        try:
            docDetail = m.getDocumentDetails(lang, i)
            docAuthors = m.getDocumentAuthors(i)
            docLabels = m.getDocumentLabels(i, lang)
        except ElcanoError as e:
            return jsonify(e.dict())

        doc = dict()
        doc["id"] = docDetail["id_document"]
        doc["title"] = docDetail["title"]
        doc["theme"] = docDetail["theme"]
        doc["time"] = docDetail["last_edit_time"]
        doc["authors"] = []
        doc["labels"] = []

        for a in docAuthors:
            au = dict()
            au["id"] = a["id_author"]
            au["name"] = a["name"]
            au["twitter_user"] = a["twitter_user"]
            doc["authors"].append(au)

        for l in docLabels:
            la = dict()
            la["id"] = l["id_label"]
            la["label"] = l["label"]
            doc["labels"].append(la)

        out.append(doc)
        
    sortedOut = sorted(out, key=itemgetter("time"), reverse=True)

    return(jsonify({"results": sortedOut[page*cons.frontend["documentCatalogListSize"]: \
                                         (page*cons.frontend["documentCatalogListSize"])+ \
                                         cons.frontend["documentCatalogListSize"]], \
                    "listSize": len(sortedOut), "page": page}))
