# coding=UTF8

"""
News public backend
"""
from frontend import app
from flask import jsonify, request
from model.newmodel import NewModel
from model.helpers import ElcanoError
from operator import itemgetter
import locale
from common import const as cons


@app.route('/new', methods=['GET'])
def getNewCatalogFrontend():
    """Gets the news catalog. request.args:
    page: mandatory, page to show
    lang: mandatory, language
    search: optional, search criteria (searches in titles and texts)
    filterbylabel: optional, comma-separated list of labels ID to filter with

    TODO: habría que traerse el criterio de ordenación de la base de
    datos junto a los ID para ordenar antes de pedir todos los datos finalmente
    """
    m = NewModel()
    search = request.args["search"] if "search" in request.args else None
    lang = request.args["lang"]
    filterByLabel = request.args["filterbylabel"] if "filterbylabel" in request.args else None
    page = int(request.args["page"])
    notLang = "en" if lang=="es" else "es"

    try:
        if search:
            ids = m.searchNewsByFeatures(search, True).union(m.searchNewsByLabel(search, True))
        else:
            ids = m.searchNewsByFeatures("", True)
        if filterByLabel:
            ids = ids.intersection(m.filterByLabels(lang, filterByLabel))

        out=[]
        for i in list(ids):
            newsDetails = m.getNewDetails(i)
            labels = m.getLabelsForNew(i, lang)
            newsDetails["labels"] = labels
            newsDetails.pop("section_"+notLang)
            newsDetails.pop("text_"+notLang)
            newsDetails.pop("title_"+notLang)
            newsDetails.pop("url_"+notLang)
            newsDetails["title"]=newsDetails.pop("title_"+lang)
            newsDetails["text"]=newsDetails.pop("text_"+lang)
            newsDetails["url"]=newsDetails.pop("url_"+lang)
            newsDetails["section"] = newsDetails.pop("section_"+lang)
            out.append(newsDetails)

        sortedOut = sorted(out, key=itemgetter("title"), cmp=locale.strcoll)

        return(jsonify({"results": {"page": page, "listSize": len(out), \
                                    "data": sortedOut[cons.frontend["newsCatalogPageSize"]*page:\
                                                      cons.frontend["newsCatalogPageSize"]*(page+1)]}}))
    except ElcanoError as e:
        return(jsonify(e.dict()))
