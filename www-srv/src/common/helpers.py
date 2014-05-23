# coding=UTF8

"""

Common helpers.

"""
import hashlib
import tweepy
import model.iepgdatamodel
from config import MemcachedConfig
from flask import jsonify
import engine.engine as engine
import maplex.maplex as maplex
if MemcachedConfig["enabled"] == True:
    import memcache
import const
import collections


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
    for k,i in const.variables.items():
        if i["family"]==family and i["key"]==key:
            return i
    
    return None


def blocksSumCalculateData(blockCode, year, family, variable):
    """Calculates block data for a variable."""
    m = model.iepgdatamodel.IepgDataModel()
    block = blocks[blockCode]
    if block["precalculated"]:
        pass
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
        if a in getBlocks().keys():
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


def getBlocks():
    """Returns all ISO codes of blocks."""
    names = cacheWrapper(maplex.getNames)
    isoCodes = {v["id_geoentity"]: v["name"] for v in names if v["id_name_family"]==4}
    spanishNames = {v["id_geoentity"]: v["name"] for v in names if v["id_name_family"]==3 and 
                    v["id_geoentity"] in isoCodes.keys()}
    englishNames = {v["id_geoentity"]: v["name"] for v in names if v["id_name_family"]==2 and 
                    v["id_geoentity"] in isoCodes.keys()}

    countries = dict()
    for k,v in isoCodes.iteritems():
        n = dict()
        n["es"] = spanishNames[k]
        n["en"] = englishNames[k]
        n["idGeoentity"] = k
        countries[v] = n
            
    return(countries)
    

def getIepgCountries():
    """Returns all ISO codes of countries in IEPG."""
    m = getListFromDictionary(arraySubstraction(cacheWrapper(engine.getVariableCodes, 1), const.iepgBlocks), 
                              "code")
    names = cacheWrapper(maplex.getNames)
    isoCodes = {v["id_geoentity"]: v["name"] for v in names if v["id_name_family"]==1 and v["name"] in m}
    spanishNames = {v["id_geoentity"]: v["name"] for v in names if v["id_name_family"]==3 and 
                    v["id_geoentity"] in isoCodes.keys()}
    englishNames = {v["id_geoentity"]: v["name"] for v in names if v["id_name_family"]==2 and 
                    v["id_geoentity"] in isoCodes.keys()}

    countries = dict()
    for k,v in isoCodes.iteritems():
        n = dict()
        n["es"] = spanishNames[k]
        n["en"] = englishNames[k]
        n["idGeoentity"] = k
        countries[v] = n
            
    return(countries)


def getIepeCountries():
    """Returns all ISO codes of countries in IEPE."""
    m = getListFromDictionary(arraySubstraction(cacheWrapper(engine.getVariableCodes, 2), iepgBlocks), 
                              "code")
    names = cacheWrapper(maplex.getNames)
    isoCodes = {v["id_geoentity"]: v["name"] for v in names if v["id_name_family"]==1 and v["name"] in m}
    spanishNames = {v["id_geoentity"]: v["name"] for v in names if v["id_name_family"]==3 and 
                    v["id_geoentity"] in isoCodes.keys()}
    englishNames = {v["id_geoentity"]: v["name"] for v in names if v["id_name_family"]==2 and 
                    v["id_geoentity"] in isoCodes.keys()}

    countries = dict()
    for k,v in isoCodes.iteritems():
        n = dict()
        n["es"] = spanishNames[k]
        n["en"] = englishNames[k]
        n["idGeoentity"] = k
        countries[v] = n
            
    return(countries)


def getBlockMembers(idGeoentityBlock, year=None):
    out = []
    for m in cacheWrapper(maplex.getBlockMembers, idGeoentityBlock, year=year):
        m["es"] = cacheWrapper(maplex.getGeoentityNames, m["id_geoentity_child"], 3)[0]["names"][0]
        m["en"] = cacheWrapper(maplex.getGeoentityNames, m["id_geoentity_child"], 2)[0]["names"][0]
        m["iso"] = cacheWrapper(maplex.getGeoentityNames, m["id_geoentity_child"], 1)[0]["names"][0]
        out.append(m)
    return(out)


def getListFromDictionary(dictionary, key):
    """Returns a list from the elements with a key in a dictionary."""
    out = []
    for i in dictionary:
        out.append(i[key])
    return(out)


def getOrderedDictionary(dict):
    """Returns an ordered dictionaty."""
    collator = PyICU.Collator.createInstance(PyICU.Locale("es_ES.UTF-8"))
    od = collections.OrderedDict()
    s = sorted(dict.keys(), cmp=collator.compare)
    for i in s:
        od[i] = dict[i]

    return od


def getVariableYears(family):
    """Returns a list for years present in IEPG/IEPE data."""
    if family=="iepg":
        return(sorted([int(i["year"]) for i in engine.getVariableYears(1)]))
    if family=="iepe":
        return(sorted([int(i["year"]) for i in engine.getVariableYears(2)]))


def getGeoentityBlocks(isoGeoentity, year=None):
    """Return the ISO code of block from isoGeoentity."""
    pass
    ###HERE
    #blocks = maplex.getGeoentityBlocks(
