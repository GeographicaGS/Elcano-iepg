# coding=UTF8

"""

Explora country services.

"""
from frontend import app
from flask import jsonify,request,send_file,make_response
from common.helpers import baseMapData
import json
from model import iepgdatamodel
from common.errorhandling import ElcanoApiRestError
from common.const import variables, years
import common.datacache as dc
from collections import OrderedDict
import unicodedata

@app.route('/countryfilter/<string:lang>', methods=['GET'])
def countryFilter(lang):
    if "eu" in request.args:
        l = dc.countriesAndEu
    else:
        l = dc.countries

    isoTable = dc.isoToEnglish if lang=="en" else dc.isoToSpanish
    countries = sorted([{"id": x, "name": k}  for (x,k) in isoTable.iteritems() if x in l],
                       key=lambda t: unicodedata.normalize('NFD', t["name"].lower().decode('utf-8')).encode('ASCII', 'ignore'))
    return(jsonify({"results": countries}))
