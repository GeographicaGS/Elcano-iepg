# coding=UTF8

"""

Explora country services.

"""
import common.datacache as datacache
import common.arrayops as arrayops
from explora import app
from flask import jsonify,request,send_file,make_response
from common.helpers import baseMapData
import common.arrayops
import json
from model import iepgdatamodel, basemap
from common.errorhandling import ElcanoApiRestError
import common.helpers
import common.const as const
from helpers import processFilter
import varengine.varengine as varengine
import numpy as numpy
from collections import OrderedDict
import locale
import copy
import maplex as maplex


@app.route('/countryfilter/<string:lang>', methods=['GET'])
def countryFilter(lang):
    if lang=="es":
        iso = datacache.isoToSpanish
    else:
        iso = datacache.isoToEnglish
    data = sorted([{"id": k, "name": v, "short_name_"+lang+"_order": v} for (k,v) in iso.iteritems() 
            if k in datacache.countries], key=lambda t: t["short_name_"+lang+"_order"])
    return(jsonify({"results": data}))


@app.route('/blocks', methods=["GET"])
def blocksData():
    """Retrieves blocks data."""
    isoSpanish = {k: v for (k,v) in datacache.isoToSpanish.iteritems() if k in datacache.blocks}
    isoEnglish = {k: v for (k,v) in datacache.isoToEnglish.iteritems() if k in datacache.blocks}
    out = dict()
    for b in datacache.blocks:
        year = dict()
        for y in datacache.dataSets["iepg"].variables["energy"].getVariableYears:
            m = common.helpers.getBlockMembers(b, year=y)
            year[y] = m
        year["name_es"] = isoSpanish[b]
        year["name_en"] = isoEnglish[b]
        out[b] = year

    locale.setlocale(locale.LC_ALL, "es_ES.UTF-8")
    out["es"] = [k[0] for k in sorted(isoSpanish.items(), key=lambda t: t[1], cmp=locale.strcoll)]
    out["en"] = [k[0] for k in sorted(isoEnglish.items(), key=lambda t: t[1], cmp=locale.strcoll)]

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

    # Check the type of country code (country, EU, or block)
    if countryCode in datacache.countries:
        rankType = 0
        population = copy.deepcopy(datacache.countries)
    if countryCode in datacache.blocks:
        rankType = 2
        population = copy.deepcopy(datacache.blocksNoEu)
    if countryCode=="XBEU":
        rankType = 1
        population = copy.deepcopy(datacache.countriesAndEu)

    # Filter substraction
    if f:
        filteredPopulation = arrayops.arraySubstraction(population, f)
    else:
        filteredPopulation = population

    try:
        out = dict()
        # Iterate through the years involved in the variable
        for year in const.years:
            yearData = dict()
            famData = datacache.dataSets[family].getData(code=countryCode, year=year)
            famPercentage = datacache.dataSets[family+"_relative_contribution"].\
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
                    c = arrayops.arraySubstraction(filteredPopulation, 
                                                   common.helpers.getBlockMembers(countryCode, year))
                else:
                    c = filteredPopulation

                d["globalranking"] = common.helpers.getRankingCode(population, 
                                                                   year, 
                                                                   datacache.dataSets[family].variables[k], 
                                                                   countryCode)

                if f:
                    d["relativeranking"] = common.helpers.getRankingCode(c, year, 
                                                                         datacache.dataSets[family].variables[k],
                                                                         countryCode)
                else:
                    d["relativeranking"] = d["globalranking"]

                famDict[k] = d

            conDict = dict()

            for k,v in conData.iteritems():
                if family=="iepe" and year>=2005:
                    population = common.helpers.getBlockMembers("XBEU", year)
                    if f:
                        filteredPopulation = arrayops.arraySubstraction(population, f)
                    else:
                        filteredPopulation = population

                a = v.values()[0]
                d = {
                    "code": a["code"],
                    "variable": k,
                    "year": year,
                    "percentage": None
                }

                if lang=="en":
                    if k=="gdp":
                        d["value"] = round(a["value"]/1000000000, 2) if a["value"] else None
                    if k=="population":
                        d["value"] = round(a["value"]/1000000, 2) if a["value"] else None
                if lang=="es":
                    if k=="gdp":
                        d["value"] = round(a["value"]/1000000000000, 2) if a["value"] else None
                    if k=="population":
                        d["value"] = round(a["value"]/1000000, 2) if a["value"] else None

                # Check if countryCode is a block. If it is, substract its members from countries
                if countryCode in datacache.blocks:
                    c = arrayops.arraySubstraction(filteredPopulation, 
                                                   common.helpers.getBlockMembers(countryCode, year))
                else:
                    c = filteredPopulation

                d["globalranking"] = common.helpers.getRankingCode(population, 
                                                                   year, 
                                                                   datacache.dataSets["context"].variables[k], 
                                                                   countryCode)
                d["relativeranking"] = common.helpers.getRankingCode(c, year,
                                                                     datacache.dataSets["context"].variables[k],
                                                                      countryCode)

                conDict[k] = d
                yearData["family"] = famDict
                yearData["context"] = conDict
                comment = m.getIepgComment(lang, countryCode, 2013)
                yearData["comment"] = comment[0] if comment else None
                out[year] = yearData

        return(jsonify({"results": out}))
    except ElcanoApiRestError as e:
        return(jsonify(e.toDict()))


@app.route('/mapdata/<string:family>/<string:variable>/<int:year>/<int:mode>', methods=['GET'])
def mapData(family, variable, year, mode):
    """Retrieves map data. Service call:
    
    /mapdata/es/iepg/economic_presence/2013/0?filter=US,DK,ES&toolfilter=US,DK

    Modes are:
    0: countries
    1: countries+EU
    2: blocks
    """
    if mode==0:
        population = copy.deepcopy(datacache.countries)
    if mode==1:
        population = arrayops.arraySubstraction(
            copy.deepcopy(datacache.countriesAndEu),
            common.helpers.getBlockMembers("XBEU", year=year))
    if mode==2:
        population = copy.deepcopy(datacache.blocksNoEu)

    filter = processFilter(request.args, "filter")
    toolFilter = processFilter(request.args, "toolfilter")
    if filter:
        c = arrayops.arraySubstraction(population, filter)
    else:
        c = population
    
    varData = [v for (k,v) in 
               common.helpers.getData(datacache.dataSets[family].variables[variable], 
                                      year=year, countryList=c).iteritems()]
    return(jsonify({"results": varData}))


@app.route('/mapgeojson', methods=['GET'])
def mapGeoJson():
    """Returns the map GeoJSON."""
    m = basemap.GeometryData()
    data = m.geometryData
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
