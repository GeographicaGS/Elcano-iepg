# coding=UTF8

"""

Common helpers.

"""
import common.datacache as datacache
import tweepy
#from common.config import MemcachedConfig
from flask import jsonify
import varengine.varengine as varengine
import maplex.maplex as maplex

import collections
import numpy
import const
import model.iepgdatamodel


def baseMapData():
    m = basemap.GeometryData()
    geomData = m.geometryData()
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

    data = sorted([v for (k,v) in getData(variable, year=year, countryList=countryList).iteritems()
                   if v["code"] in countryList], key=lambda x: x["value"], reverse=True)
    values = sorted(set([k["value"] for k in data if k["value"] is not None]), reverse=True)
    out = {}
    i = 0
    j = 0
    while j<len(data):
        if data[j]["value"] is None:
            d = {
                "value": data[j]["value"],
                "rank": None
            }
            out[data[j]["code"]] = d
            j += 1
        else:
            if values[i]==data[j]["value"]:
                d = {
                    "value": data[j]["value"],
                    "rank": i+1
                }
                out[data[j]["code"]] = d
                j += 1
            else:
                if i<len(values):
                    i += 1
    return(out)


def getRankingCode(countryList, year, variable, countryCode):
    """Calculates rankings, given a country list and a country filter, and
    given that the country list may contain blocks. Returns a dictionary with 
    ISO keys and the ranking. NaN are ignored."""

    if countryCode not in countryList:
        return(None)
    value = getData(variable, year=year, code=countryCode).values()[0]["value"]
    if not value:
        return(None)
    dataValues = sorted(set([v["value"] for (k,v) in 
                            getData(variable, year=year, countryList=countryList).iteritems()
                            if v["value"]]), reverse=True)
    i = 0
    while dataValues[i]>value:
        i+=1
    return(i+1)


def getBlockMembers(isoBlock, year=None):
    """Returns a list of block members ISO."""
    return([datacache.geoentityToIso[i["id_geoentity_child"]] for i in 
            maplex.getBlockMembers(datacache.isoToGeoentity[isoBlock],
                                   year=year)])


# TODO: code can be an array of codes, years the same
def getData(variable, code=None, year=None, countryList=None):
    """Returns variable value. If countryList is present, only data for this countries 
    are returned. countryList can mix calculated and uncalculated codes. If code is not None,
    countryList is ignored."""
    if countryList:
        out = {}
        for i in countryList:
            for k,v in getData(variable, code=i, year=year).iteritems():
                out[k] = v
        return(out)
    return(variable.getData(code=code, year=year))
