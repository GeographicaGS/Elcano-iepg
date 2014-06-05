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


@app.route('/ranking/<string:lang>/<int:year>/<string:family>/<string:variable>', methods=['GET'])
def ranking(lang, year, family, variable):
    """Retrieves ranking for a year and a variable. Examples:

    /ranking/es/1990/iepg/energy
    /ranking/en/2012/iepe/manufactures?filter=ES,NL,DE&entities=ES,NL&blocks=t
    """
    filter = helpers.processFilter(request.args, "filter")
    entities = helpers.processFilter(request.args, "entities")
    blocks = True if helpers.processArgs(request.args, "blocks") else False

    if blocks and entities:
        c = arrayops.arraySubstraction(datacache.countries, filter)
        if family=="iepe":
            c = arrayops.arraySubstraction(c, datacache.blocks)
        else:
            blocksInEntities = [b for b in entities if b in datacache.blocks]
            for bl in blocksInEntities:
                if chelpers.getData(datacache.variables[family+"_"+variable], code=bl, year=year):
                    c = arrayops.arraySubstraction(c, chelpers.getBlockMembers(bl, year=year))
            c.extend(entities)
        c = list(set(c))
    else:
        c = arrayops.arraySubstraction(datacache.countries, filter)

    r = chelpers.getRanking(c, year, datacache.variables[family+"_"+variable])
    return(jsonify({"results": r}))
