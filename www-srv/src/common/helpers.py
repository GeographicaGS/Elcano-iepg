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
    """Returns a dictionary of block's data keyed by ISO codes."""
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


def getBlocksIso():
    """Returns a list of blocks ISO codes."""
    return([v for v in cacheWrapper(getBlocks).keys()])
    

def getCountryDataByVariableFamily(family):
    """Returns a dictionary with country data keyed by ISO codes of the given family."""
    m = arraySubstraction(cacheWrapper(engine.getVariableCodes, family, 'energy'), 
                          cacheWrapper(getBlocksIso))
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


def getCountriesIsoByVariableFamily(family):
    """Returns a list of country ISO codes in variable family."""
    return([c for c in cacheWrapper(getCountryDataByVariableFamily, family).keys()])


def getBlockMembers(isoBlock, year=None):
    """Returns a dictionary of block members data keyed by ISO."""
    out = dict()
    for m in cacheWrapper(maplex.getBlockMembers, maplex.getIdGeoentityByName(isoBlock, 4)[0]["id_geoentity"],
                          year=year):
        m["es"] = cacheWrapper(maplex.getGeoentityNames, m["id_geoentity_child"], 3)[0]["names"][0]
        m["en"] = cacheWrapper(maplex.getGeoentityNames, m["id_geoentity_child"], 2)[0]["names"][0]
        iso = cacheWrapper(maplex.getGeoentityNames, m["id_geoentity_child"], 1)[0]["names"][0]
        out[iso] = m
    return(out)


def getBlockMembersIso(isoBlock, year=None):
    """Returns a list of ISO codes for a block and a year."""
    return([c for c in cacheWrapper(getBlockMembers, isoBlock, year=year).keys()])


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
    """Returns a list for years present in IEPG/IEPE data.
    TODO: implement in engine the notion of DATASET, which points to a table with code, date_in, date_out.
    Column names are the variable's key, and variables must have metadata like they have now."""
    return(sorted(engine.getVariableYears(family, 'energy')))
    

def getGeoentityBlocks(isoGeoentity, year=None):
    """Return the ISO code of block from isoGeoentity."""
    id = maplex.getIdGeoentityByName(isoGeoentity, 1)
    blocks = maplex.getGeoentityBlocks(id[0]["id_geoentity"], year)
    return(maplex.getGeoentityNames(blocks[0]["id_geoentity_block"], 4)[0]["names"][0])


def getVariables(family=None):
    """Return variables for an optional family."""
    idFamily = engine.getIdFamilyByName(family) if family else None
    return(engine.getVariables(idFamily))


def isBlock(isoGeoentity):
    """Returns True if isoGeoentity is a block."""
    return(maplex.getIdGeoentityByName(isoGeoentity, 4)<>[])


def getVariableValue(family, variable, code, year):
    """Returns variable value."""
    return(engine.getVariableValue(family, variable, code, year))

