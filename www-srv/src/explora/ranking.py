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


@app.route('/ranking/<string:lang>/<int:currentYear>/<int:referenceYear>/<string:family>/<string:variable>/<int:mode>', methods=['GET'])
def ranking(lang, currentYear, referenceYear, family, variable, mode):
    """Retrieves ranking for a year and a variable. Examples:

    /ranking/es/1995/1990/iepg/energy/0
    /ranking/en/2012/1995/iepe/manufactures/1?filter=US,DE&entities=ES,NL,XBAP,XBSA

    Modes are:

    0: country ranking
    1: countries+UE ranking
    2: block ranking
    """
    f = processFilter(request.args, "filter")
    e = processFilter(request.args, "entities")

    if mode==1 and currentYear<2005:
        return(jsonify({"results": []}))

    if family=="iepg":
        if mode==0:
            population=copy.deepcopy(datacache.countries)
        if mode==1:
            population=copy.deepcopy(datacache.countriesAndEu)
        if mode==2:
            population=copy.deepcopy(datacache.blocksNoEu)

    if family=="iepe":
        population = chelpers.getBlockMembers("XBEU", year=currentYear)

    v = datacache.dataSets[family].variables[variable]

    if f:
        currentC = arrayops.arraySubstraction(population, f)
    else:
        currentC = population

    referenceC = currentC

    if mode==1:
        currentC = arrayops.arraySubstraction(currentC, chelpers.getBlockMembers("XBEU", year=currentYear))
        referenceC = arrayops.arraySubstraction(referenceC, chelpers.getBlockMembers("XBEU", year=referenceYear))

    currentRanking = OrderedDict(sorted(chelpers.getRanking(currentC, currentYear, v).items(), 
                                        key=lambda t: t[1]["rank"]))
    referenceRanking = chelpers.getRanking(referenceC, referenceYear, v)

    out = []
    allNull = True
    for k,v in currentRanking.iteritems():
        d = {
            "code": k,
            "currentRanking": v["rank"],
            "currentValue": v["value"]
        }
        if v["rank"] is not None:
            allNull = False
        if k in referenceRanking:
            d["referenceRanking"]=referenceRanking[k]["rank"]
            d["referenceValue"]=referenceRanking[k]["value"]
        else:
            d["referenceRanking"]=None
            d["referenceValue"]=None

        out.append(d)

    if allNull:
        return(jsonify({"results": []}))
    else:
        return(jsonify({"results": out}))
