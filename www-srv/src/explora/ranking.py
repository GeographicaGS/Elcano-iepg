# coding=UTF8

"""

Explora ranking tool services.

"""
from helpers import processFilter
from explora import app
from model import iepgdatamodel
from flask import jsonify, request
from common.errorhandling import ElcanoApiRestError
import common.helpers as chelpers
import helpers
import common.datacache as datacache
import common.arrayops as arrayops


@app.route('/ranking/<string:lang>/<int:year>/<string:family>/<string:variable>/<int:blocks>', 
           methods=['GET'])
def ranking(lang, year, family, variable, blocks):
    """Retrieves ranking for a year and a variable. Examples:

    /ranking/es/1990/iepg/energy/0
    /ranking/en/2012/iepe/manufactures/1?filter=US,DE&entities=ES,NL,XBAP,XBSA
    """

    r = {"e": 1}

    f = processFilter(request.args, "filter")
    e = processFilter(request.args, "entities")
    countries = datacache.countries
    entitiesBlocks = [v for v in e if v in datacache.blocks]
    v = datacache.dataSets[family].variables[variable]

    if f:
        c = arrayops.arraySubstraction(countries, f)
    else:
        c = countries

    if blocks:
        for i in entitiesBlocks:
            c = arrayops.arraySubstraction(c, chelpers.getBlockMembers(i, year=year))
            c.append(i)

    ranking = chelpers.getRanking(c, year, v)
    out = []
    for k,v in ranking.iteritems():
        d = {
            "code": k,
            "ranking": v["rank"],
            "value": v["value"]
        }
        out.append(d)

    return(jsonify({"results": out}))
