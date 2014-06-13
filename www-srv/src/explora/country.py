# coding=UTF8

"""

Explora country services.

"""
import common.datacache as datacache
import common.arrayops as arrayops
from explora import app
from flask import jsonify,request,send_file,make_response
from common.helpers import cacheWrapper, baseMapData
import common.arrayops
import json
from model import iepgdatamodel, basemap
from common.errorhandling import ElcanoApiRestError
from common.const import variables, years, blocks
import common.helpers
import common.const as const
from helpers import processFilter
import varengine.varengine as varengine
import numpy as numpy


@app.route('/countryfilter/<string:lang>', methods=['GET'])
def countryFilter(lang):
    if lang=="es":
        iso = datacache.isoToSpanish
    else:
        iso = datacache.isoToEnglish
    data = [{"id": k, "name": v, "short_name_"+lang+"_order": v} for (k,v) in iso.iteritems() 
            if k in datacache.countries]
    return(jsonify({"results": data}))


@app.route('/blocks/<string:lang>', methods=["GET"])
def blocksData(lang):
    """Retrieves currently available blocks data (based on filtered countries)."""
    if lang=="es":
        iso = datacache.isoToSpanish
    else:
        iso = datacache.isoToEnglish
    out = dict()
    for b in datacache.blocks:
        year = dict()
        for y in cacheWrapper(datacache.dataSets["iepg"].variables["energy"].getVariableYears):
            m = cacheWrapper(common.helpers.getBlockMembers, b, year=y)
            year[y] = m
        year["name"] = iso[b]
        out[b] = year

    return(jsonify(out))


@app.route('/countrysheet/<string:lang>/<string:family>/<string:countryCode>', methods=['GET'])
def countrySheet(lang, family, countryCode):
    """Retrieves all the data, for all years, and for a single country, to render the country sheet.
    Only retrieves context and IEPG variable families.
    Service call:

    /countrysheet/es/iepe/US?filter=US,DK,ES&entities=NL,XBEU,NZ

    entities is mandatory, although it has no effect in this tool.
    """
    m = iepgdatamodel.IepgDataModel()
    f = processFilter(request.args, "filter")
    # Participating countries
    countries = datacache.countries
    # Filter substraction
    if f:
        countries = arrayops.arraySubstraction(countries, f)

    try:
        out = dict()
        # Iterate through the years involved in the variable
        for year in const.years:
            yearData = dict()
            famData = datacache.dataSets[family].getData(code=countryCode, year=year)
            famPercentage = datacache.dataSets[family+"_individual_contribution"].\
                            getData(code=countryCode, year=year)
            conData = datacache.dataSets["context"].getData(code=countryCode, year=year)
            famDict = dict()

            for k,v in famData.iteritems():
                a = v.values()[0]
                d = {
                    "code": a["code"],
                    "value": a["value"],
                    "variable": k,
                    "year": year,
                    "percentage": famPercentage[k].values()[0]["value"] if k not in ["global"] else None
                }

                # Check if countryCode is a block. If it is, substract its members from countries
                # This is expensive. Cache block members.
                if countryCode in datacache.blocks:
                    c = arrayops.arraySubstraction(countries, 
                                                   cacheWrapper(common.helpers.getBlockMembers,
                                                                countryCode, year))
                    c.append(countryCode)
                else:
                    c = countries

                d["globalranking"] = cacheWrapper(common.helpers.getRankingCode, datacache.countries, 
                                                  year, datacache.dataSets[family].variables[k], 
                                                  countryCode)
                d["relativeranking"] = cacheWrapper(common.helpers.getRankingCode, c, year,
                                                    datacache.dataSets[family].variables[k], countryCode)
                famDict[k] = d
            conDict = dict()

            for k,v in conData.iteritems():
                a = v.values()[0]
                d = {
                    "code": a["code"],
                    "value": a["value"],
                    "variable": k,
                    "year": year,
                    "percentage": None
                }

                # Check if countryCode is a block. If it is, substract its members from countries
                if countryCode in datacache.blocks:
                    c = arrayops.arraySubstraction(countries, 
                                                   cacheWrapper(common.helpers.getBlockMembers,
                                                                countryCode, year))
                    c.append(countryCode)
                else:
                    c = countries

                d["globalranking"] = cacheWrapper(common.helpers.getRankingCode, datacache.countries, 
                                                  year, datacache.dataSets["context"].variables[k], 
                                                  countryCode)
                d["relativeranking"] = cacheWrapper(common.helpers.getRankingCode, c, year,
                                                    datacache.dataSets["context"].variables[k], countryCode)
                
                conDict[k] = d
                yearData[family] = famDict
                yearData["context"] = conDict
                comment = cacheWrapper(m.getIepgComment, lang, countryCode, 2013)
                yearData["comment"] = comment[0] if comment else None
                out[year] = yearData
        return(jsonify({"results": out}))
    except ElcanoApiRestError as e:
        return(jsonify(e.toDict()))


@app.route('/mapdata/<string:family>/<string:variable>/<int:year>', methods=['GET'])
def mapData(family, variable, year):
    """Retrieves map data. Service call:
    
    /mapdata/es/iepg/economic_presence/2013?filter=US,DK,ES&toolfilter=US,DK
    """
    filter = processFilter(request.args, "filter")
    toolFilter = processFilter(request.args, "toolfilter")
    if filter:
        c = arrayops.arraySubstraction(datacache.countries, filter)
    else:
        c = datacache.countries
    try:
        varData = cacheWrapper(common.helpers.getData, datacache.dataSets[family].variables[variable], 
                               year=year, countryList=c)
        varData = [v for (k,v) in varData.iteritems() if v["value"] is not None]
        return(jsonify({"results": varData}))
    except ElcanoApiRestError as e:
        return(jsonify(e.toDict()))    


@app.route('/mapgeojson', methods=['GET'])
def mapGeoJson():
    """Returns the map GeoJSON."""
    m = basemap.GeometryData()
    data = cacheWrapper(m.geometryData)
    out = dict()
    out["type"] = "FeatureCollection"
    
    features = []
    for d in data:
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


@app.route('/globalindex/<string:family>/<string:variable>/<string:countries>/<string:lang>', methods=['GET'])
def globalindex(family,variable,countries,lang):
    countriesArray = countries.split(",")
    varData = common.helpers.getData(datacache.dataSets[family].variables[variable],
                                     countryList=countriesArray)
    out = []
    codes = set([j["code"] for (i,j) in varData.iteritems()])
    for k in codes:
        years = {j["year"]: {"value": j["value"]} for (i,j) in varData.iteritems() if j["code"]==k}
        d = {
            "country": k,
            "years": years
        }
        out.append(d)
    return jsonify({"results": out})
