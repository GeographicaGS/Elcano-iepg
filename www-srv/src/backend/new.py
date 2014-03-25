# coding=UTF8

"""

News administration backend

"""
from backend import app
from flask import jsonify, request
from model.newmodel import NewModel
from backend.utils import auth
from operator import itemgetter
import locale
import cons


@app.route('/new', methods=['POST'])
@auth
def createNew():
    """
    Creates a new new. Requires a JSON:

    {
    "title_en": "title_en",
    "title_es": "title_es",
    "text_en": "text_en",
    "text_es": "text_es",
    "url_en": "url_en",
    "url_es": "url_es",
    "news_section": 1,
    "labels_en": [1,2,3,4],
    "labels_es": [2,3,4,5]
    }

    where news_section are:
    1: Blog,
    2: Media,
    3: Events
    """
    m = NewModel()
    j = request.json
    return(jsonify({"id_new": m.createNew(j["title_en"], j["title_es"], \
                                          j["text_en"], j["text_es"], \
                                          j["url_en"], j["url_es"], \
                                          j["news_section"], j["labels_en"], j["labels_es"])}))


@app.route('/new/<int:id>', methods=['PUT'])
@auth
def updateNew(id):
    """
    Updates a new. Requires a JSON:

    {
    "title_en": "title_en",
    "title_es": "title_es",
    "text_en": "text_en",
    "text_es": "text_es",
    "url_en": "url_en",
    "url_es": "url_es",
    "news_section": 1,
    "labels_en": [1,2,3,4],
    "labels_es": [2,3,4,5]
    }

    where news_section are:
    1: Blog,
    2: Media,
    3: Events
    """
    m = NewModel()
    j = request.json
    return(jsonify({"id_new": m.editNew(id, j["title_en"], j["title_es"], \
                                        j["text_en"], j["text_es"], \
                                        j["url_en"], j["url_es"], \
                                        j["news_section"], j["labels_en"], j["labels_es"])}))


@app.route('/new/<int:id>', methods=['DELETE'])
@auth
def deleteNew(id):
    """Deletes the new with ID id."""
    m = NewModel()
    return(jsonify({"id_new": m.deleteNew(id)}))


@app.route('/new/toggle_published/<int:id>', methods=['PUT'])
@auth
def newTogglePublish(id):
    """Toggles published status of the new with ID id."""
    m = NewModel()
    return(jsonify({"id_new": m.togglePublish(id)}))
    

@app.route('/new', methods=['GET'])
@auth
def getNewCatalog():
    """Gets the news catalog. request.args:
    page: mandatory, page to show
    search: optional, search criteria (searches in titles, texts, and labels)
    """
    m = NewModel()
    search = request.args["search"] if "search" in request.args else None
    page = int(request.args["page"])

    if search:
        ids = m.searchNewsByFeatures(search).union(m.searchNewsByLabel(search))
    else:
        ids = m.searchNewsByFeatures("")

    news = []
    for new in ids:
        out = dict()
        d = m.getNewDetails(new)
        if d["title_en"] and d["text_en"] and d["url_en"] and d["description_en"]:
            out["english"]=True
        else:
            out["english"]=False
        if d["title_es"] and d["text_es"] and d["url_es"] and d["description_es"]:
            out["spanish"]=True
        else:
            out["spanish"]=False
        out["title"] = d["title_es"] if d["title_es"]!=None else \
                       d["title_en"] if d["title_en"]!=None else "Sin título"
        out["time"] = d["new_time"]
        out["published"] = d["published"]
        out["id"] = d["id_new"]
        news.append(out)

    return(jsonify({"results": sorted(news, key=itemgetter("title"), cmp=locale.strcoll)\
                    [cons.newsCatalogPageSize*page:cons.newsCatalogPageSize*(page+1)]}))
