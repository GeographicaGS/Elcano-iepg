# coding=UTF8

"""

Explora country services.

"""
from explora import app
from flask import jsonify,request,send_file,make_response
from common.helpers import cacheWrapper, baseMapData
import cons
import json
from model import iepgdatamodel, basemap
from common.errorhandling import ElcanoApiRestError
from common.const import variables, years
from helpers import processFilter


@app.route('/countryfilter/<string:lang>', methods=['GET'])
def countryFilter(lang):
    m = iepgdatamodel.IepgDataModel()
    try:
        return(jsonify({"results": cacheWrapper(m.countryFilter, lang)}))
    except ElcanoApiRestError as e:
        return(jsonify(e.toDict()))


@app.route('/countrysheet/<string:lang>/<string:countryCode>', methods=['GET'])
def countrySheet(lang, countryCode):
    """Retrieves all the data, for all years, and for a single country, to render the country sheet.
    Only retrieves context and IEPG variable families.
    Service call:

    /countrysheet/es/US?filter=US,DK,ES
    /countrysheet/en/NL?filter=US,NL,ES&toolfilter=NL,ES
    """
    m = iepgdatamodel.IepgDataModel()
    filter = processFilter(request.args, "filter")
    toolFilter = processFilter(request.args, "toolfilter")
    try:
        data = dict()
        for year in years:
            y = dict()
            iepg_var = dict()
            context_var = dict()
            for var,item in variables.items():
                if item["family"]=="iepg":
                    rankData = cacheWrapper(m.ranking, lang, countryCode, 
                                            "iepg", item["key"], year, filter=filter, toolFilter=toolFilter)
                    iepg_var[item["key"]] = rankData[0]
                if item["family"]=="context":
                    rankData = cacheWrapper(m.ranking, lang, countryCode, 
                                            "context", item["key"], year, filter=filter, toolFilter=toolFilter)
                    context_var[item["key"]] = rankData[0]

            y["iepg_variables"] = iepg_var
            y["context_var"] = context_var
            y["comment"] = cacheWrapper(m.getIepgComment, lang, countryCode, year)[0]
            data[year]=y
        return(jsonify({"results": data}))
    except ElcanoApiRestError as e:
        return(jsonify(e.toDict()))


@app.route('/mapdata/<string:family>/<string:variable>/<int:year>', methods=['GET'])
def mapData(family, variable, year):
    """Retrieves map data. Service call:
    
    /mapdata/es/iepg/economic_presence/2013?filter=US,DK,ES&toolfilter=US,DK
    """
    filter = processFilter(request.args, "filter")
    toolFilter = processFilter(request.args, "toolfilter")
    m = iepgdatamodel.IepgDataModel()

    try:
        varData = cacheWrapper(m.variableData, family, variable, year, filter=filter, toolFilter=toolFilter)
    except ElcanoApiRestError as e:
        return(jsonify(e.toDict()))    

    return(jsonify({"results": varData}))


@app.route('/mapgeojson', methods=['GET'])
def mapGeoJson():
    """Returns the map GeoJSON."""
    m = basemap.GeometryData()
    data = cacheWrapper(m.geometryData)
    out = dict()
    out["type"] = "FeatureCollection"
    
    features = []
    for d in data:
        print(d)
        f = dict()
        f["type"] = "Feature"
        f["geometry"] = json.loads(d["geojson"])
        fp = dict()
        fp["code"] = d["iso_3166_1_2_code"]
        fp["name_en"] = d["name_en"]
        fp["name_es"] = d["name_es"]
        f["properties"] = fp
        features.append(f)

    out["features"] = features

    return(jsonify(out))
