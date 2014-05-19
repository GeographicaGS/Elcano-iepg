# coding=UTF8

"""

Common helpers.

"""
import hashlib
import tweepy
import model.iepgdatamodel
from config import MemcachedConfig
from flask import jsonify
from const import families, variables, blocks
if MemcachedConfig["enabled"] == True:
    import memcache


def cacheWrapper(funcName, *args, **kwargs):
    """Cache wrapping helper."""
    if MemcachedConfig["enabled"]:
        h = hashlib.sha256(funcName.__name__+str(args)+str(kwargs)).hexdigest()
        mc = memcache.Client([MemcachedConfig["host"]+":"+MemcachedConfig["port"]], debug=0)
        v = mc.get(h)
        if v:
            return(v)
        else:
            out = funcName(*args, **kwargs)
            mc.set(h, out, MemcachedConfig["expiration"])
            return(out)
    else:
        return(funcName(*args, **kwargs))


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


def getVariableData(family, key):
    """Retrieves variable data."""
    for k,i in variables.items():
        if i["family"]==family and i["key"]==key:
            return i
    
    return None


def blocksSumCalculateData(blockCode, year, family, variable):
    """Calculates block data for a variable."""
    m = model.iepgdatamodel.IepgDataModel()
    block = blocks[blockCode]
    if block["precalculated"]:
        
    else:

        data = cacheWrapper(m.getCountriesData, block["members"][str(year)], year, family, variable)
        sum = 0
        for a in data:
            sum += a["value"]
    return({"code": blockCode, "value": sum})


def getBlocksFromCountryList(countryList):
    """Returns two arrays: one with the countries present in the group,
    and another one with the blocks."""
    _countries = []
    _blocks = []
    for a in countryList:
        if a in blocks:
            _blocks.append(a)
        else:
            _countries.append(a)
    return(_blocks, _countries)


def getRanking(countryList, countryFilter, year, family, variable):
    """Calculates rankings, given a country list and a country filter, and
    given that the country list may contain blocks."""
    blocks, countries = getBlocksFromCountryList(countryList)

    print(blocks, countries)

    for block in blocks:
        pass

    return(1)


def getBlocksCountries(countryList, year, countryFilter=[]):
    """Returns a list of blocks and countries based on the country filter
    in place and expelling from countries those that are included in the 
    given blocks."""
    _blocks, _countries = getBlocksFromCountryList(countryList)
    for b in _blocks:
        _c = blocks[b]["members"][str(year)]
        _countries = arraySubstraction(_countries, _c)
    _countries = arraySubstraction(_countries, countryFilter)
    _blocks.extend(_countries)
    return(_blocks)


def arrayIntersection(array1, array2):
    """Returns the intersection of two arrays."""
    return([v for v in array1 if v in array2])


def arraySubstraction(array1, array2):
    """Returns array1 without members of array2."""
    return([v for v in array1 if v not in array2])


def getIepgCountries():
    """Returns all ISO codes of countries in IEPG."""
    m = model.iepgdatamodel.IepgDataModel()

    return(cacheWrapper(m.getIepgCountriesIso))
