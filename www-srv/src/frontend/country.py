# coding=UTF8

"""

Explora country services.

"""
from frontend import app
from flask import jsonify,request,send_file,make_response
from common.helpers import cacheWrapper, baseMapData, arrayIntersection
import json
from model import iepgdatamodel
from common.errorhandling import ElcanoApiRestError
from common.const import variables, years, blocks

@app.route('/countryfilter/<string:lang>', methods=['GET'])
def countryFilter(lang):
    m = iepgdatamodel.IepgDataModel()
    try:
        return(jsonify({"results": cacheWrapper(m.countryFilter, lang)}))
    except ElcanoApiRestError as e:
        return(jsonify(e.toDict()))