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
from collections import OrderedDict
import copy


@app.route('/ranking/<string:lang>/<int:currentYear>/<int:referenceYear>/<string:family>/<string:variable>/<int:blocks>', 
           methods=['GET'])
def ranking(lang, currentYear, referenceYear, family, variable, blocks):
    """Retrieves ranking for a year and a variable. Examples:

    /ranking/es/1995/1990/iepg/energy/0
    /ranking/en/2012/1995/iepe/manufactures/1?filter=US,DE&entities=ES,NL,XBAP,XBSA
    """
    f = processFilter(request.args, "filter")
    e = processFilter(request.args, "entities")
    countries = copy.deepcopy(datacache.countries)
    entitiesBlocks = [v for v in e if v in datacache.blocks]
    v = datacache.dataSets[family].variables[variable]

    if f:
        currentC = arrayops.arraySubstraction(countries, f)
        referenceC = currentC
    else:
        currentC = countries
        referenceC = currentC

    if blocks:
        for i in entitiesBlocks:
            currentC = arrayops.arraySubstraction(currentC, chelpers.getBlockMembers(i, year=currentYear))
            currentC.append(i)
            referenceC = arrayops.arraySubstraction(referenceC, chelpers.getBlockMembers(i, year=referenceYear))
            referenceC.append(i)

    currentRanking = OrderedDict(sorted(chelpers.getRanking(currentC, currentYear, v).items(), 
                                        key=lambda t: t[1]["rank"]))
    referenceRanking = chelpers.getRanking(referenceC, referenceYear, v)

    out = []
    for k,v in currentRanking.iteritems():
        d = {
            "code": k,
            "currentRanking": v["rank"],
            "currentValue": v["value"],
            "referenceRanking": referenceRanking[k]["rank"],
            "referenceValue": referenceRanking[k]["value"]
        }
        out.append(d)

    return(jsonify({"results": out}))
