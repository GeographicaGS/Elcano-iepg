# coding=UTF8

"""

Explora ranking tool services.

"""
from helpers import processFilter
from explora import app
from model import iepgdatamodel
from flask import jsonify, request
from common.errorhandling import ElcanoApiRestError
from common.helpers import cacheWrapper


@app.route('/ranking/<string:lang>/<int:year>/<string:family>/<string:variable>', methods=['GET'])
def ranking(lang, year, family, variable):
    """Retrieves ranking for a year and a variable. Examples:

    /ranking/es/1990/iepg/energy
    /ranking/en/2012/iepe/manufactures?filter=ES,NL,DE&toolfilter=ES,NL
    """
    m = iepgdatamodel.IepgDataModel()
    filter = processFilter(request.args, "filter")
    toolFilter = processFilter(request.args, "toolfilter")
    try:
        return(jsonify({"results": cacheWrapper(m.rankingComplete, lang, family, variable, 
                                                year, filter=filter, toolFilter=toolFilter)}))
    except ElcanoApiRestError as e:
        return(jsonify(e.toDict()))
