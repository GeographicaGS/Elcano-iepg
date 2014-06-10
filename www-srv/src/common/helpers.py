# coding=UTF8

"""

Common helpers.

"""
import common.datacache as datacache
from common.cachewrapper import cacheWrapper
import hashlib
import tweepy
from config import MemcachedConfig
from flask import jsonify
import varengine.varengine as varengine
import maplex.maplex as maplex
if MemcachedConfig["enabled"] == True:
    import memcache
import collections
import numpy
import const
import model.iepgdatamodel


def baseMapData():
    m = basemap.GeometryData()
    geomData = cacheWrapper(m.geometryData)
    out = dict()
    for r in geomData:
        data = dict()
        data["name_en"] = r["name_en"]
        data["name_es"] = r["name_es"]
        data["geojson"] = r["geojson"]
        out[r["iso_3166_1_2_code"]] = data
    return(jsonify(out))
    

def getRanking(countryList, year, variable):
    """Calculates rankings, given a country list and a country filter, and
    given that the country list may contain blocks. Returns a dictionary with 
    ISO keys and the ranking. NaN are ignored."""
    values = [k for k in getData(variable, year=year, countryList=countryList) if k and 
              not numpy.isnan(k["value"])]
    valSorted = sorted(set([k["value"] for k in values]), reverse=True)
    out = []
    for i in values:
        d = {}
        j = 0
        while valSorted[j]>i["value"]:
            j+=1
        d["code"] = i["code"]
        d["value"] = i["value"]
        d["rank"] = j+1
        out.append(d)
    return(out)


def getRankingCode(countryList, year, variable, countryCode):
    """Calculates rankings, given a country list and a country filter, and
    given that the country list may contain blocks. Returns a dictionary with 
    ISO keys and the ranking. NaN are ignored."""
    if countryCode not in countryList:
        return(None)
    value = getData(variable, year=year, code=countryCode)[0]
    if not value or numpy.isnan(value["value"]):
        return(None)

    # TODO: Check if if k["code"] in countryList is necessary
    dataValues = sorted(set([k["value"] for k in getData(variable, year=year, countryList=countryList)
                             if k and k["code"] in countryList
                             and not numpy.isnan(k["value"])]), reverse=True)
    i = 0
    while dataValues[i]>value["value"]:
        i+=1
    return(i+1)


def getBlockMembers(isoBlock, year=None):
    """Returns a list of block members ISO."""
    return([datacache.geoentityToIso[i["id_geoentity_child"]] for i in 
            cacheWrapper(maplex.getBlockMembers, datacache.isoToGeoentity[isoBlock],
                         year=year)])


def getData(variable, code=None, year=None, countryList=None):
    """Returns variable value. If countryList is present, only data for this countries 
    are returned. countryList can mix calculated and uncalculated codes. If code is not None,
    countryList is ignored."""
    if countryList:
        return({u.keys()[0]: u.values()[0] for u 
                in [getData(variable, code=i, year=year) 
                    for i in countryList]})
    return(variable.getData(code=code, year=year))
