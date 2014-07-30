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
from common.const import variables, years, blocks
import common.datacache as dc
from collections import OrderedDict

@app.route('/countryfilter/<string:lang>', methods=['GET'])
def countryFilter(lang):
    isoTable = dc.isoToEnglish if lang=="en" else dc.isoToSpanish
    countries = sorted([{"id": x, "name": k}  for (x,k) in isoTable.iteritems() if x in dc.countries],
                       key=lambda t: t["name"])
    return(jsonify({"results": countries}))
