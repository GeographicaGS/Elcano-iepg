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


# # def getVariableData(family, key):
# #     """Retrieves variable data."""
# #     for k,i in const.variables.items():
# #         if i["family"]==family and i["key"]==key:
# #             return i
    
# #     return None


# # def blocksSumCalculateData(blockCode, year, family, variable):
# #     """Calculates block data for a variable."""
# #     m = model.iepgdatamodel.IepgDataModel()
# #     block = blocks[blockCode]
# #     if block["precalculated"]:
# #         pass
# #     else:
# #         data = cacheWrapper(m.getCountriesData, block["members"][str(year)], year, family, variable)
# #         sum = 0
# #         for a in data:
# #             sum += a["value"]
# #     return({"code": blockCode, "value": sum})


# # def getBlocksFromCountryList(countryList):
# #     """Returns two arrays: one with the countries present in the group,
# #     and another one with the blocks."""
# #     _countries = []
# #     _blocks = []
# #     for a in countryList:
# #         if a in getBlocks().keys():
# #             _blocks.append(a)
# #         else:
# #             _countries.append(a)
# #     return(_blocks, _countries)

# def getUnprecalculatedBlocksFromCountryList(countryList):
#     """Returns all uncalculated blocks in countryList."""
    

def getRanking(countryList, year, variable):
    """Calculates rankings, given a country list and a country filter, and
    given that the country list may contain blocks. Returns a dictionary with 
    ISO keys and the ranking. NaN are ignored."""
    values = [k for k in getData(variable, year=year, countryList=countryList) if not numpy.isnan(k["value"])]
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
    if numpy.isnan(value["value"]):
        return(None)

    # TODO: Check if if k["code"] in countryList is necessary
    dataValues = sorted(set([k["value"] for k in getData(variable, year=year, countryList=countryList)
                             if k["code"] in countryList
                             and not numpy.isnan(k["value"])]), reverse=True)
    i = 0
    while dataValues[i]>value["value"]:
        i+=1
    return(i+1)


# # def getVariableValuesSeries(countryList, year, family, variable):
# #     """Returns a dictionary keyed by ISO with the values of family/variable."""
# #     values = dict()
# #     for i in countryList:
# #         values[i] = getVariableValue(family, variable, i, year)
# #     return(values)


# # def getBlocksCountries(countryList, year, countryFilter=[]):
# #     """Returns a list of blocks and countries based on the country filter
# #     in place and expelling from countries those that are included in the 
# #     given blocks."""
# #     _blocks, _countries = getBlocksFromCountryList(countryList)
# #     for b in _blocks:
# #         _c = blocks[b]["members"][str(year)]
# #         _countries = arraySubstraction(_countries, _c)
# #     _countries = arraySubstraction(_countries, countryFilter)
# #     _blocks.extend(_countries)
# #     return(_blocks)




# # def getBlocks():
# #     """Returns a dictionary of block's data keyed by ISO codes."""
# #     names = cacheWrapper(maplex.getNames)
# #     isoCodes = {v["id_geoentity"]: v["name"] for v in names if v["id_name_family"]==4}
# #     spanishNames = {v["id_geoentity"]: v["name"] for v in names if v["id_name_family"]==3 and 
# #                     v["id_geoentity"] in isoCodes.keys()}
# #     englishNames = {v["id_geoentity"]: v["name"] for v in names if v["id_name_family"]==2 and 
# #                     v["id_geoentity"] in isoCodes.keys()}

# #     countries = dict()
# #     for k,v in isoCodes.iteritems():
# #         n = dict()
# #         n["es"] = spanishNames[k]
# #         n["en"] = englishNames[k]
# #         n["idGeoentity"] = k
# #         countries[v] = n
            
# #     return(countries)


# # def getBlocksIso():
# #     """Returns a list of blocks ISO codes."""
# #     return([v for v in cacheWrapper(getBlocks).keys()])
    

# # def getCountryDataByVariableFamily(family):
# #     """Returns a dictionary with country data keyed by ISO codes of the given family."""
# #     m = arraySubstraction(cacheWrapper(varengine.getVariableCodes, family, 'energy'), 
# #                           cacheWrapper(getBlocksIso))
# #     names = cacheWrapper(maplex.getNames)
# #     isoCodes = {v["id_geoentity"]: v["name"] for v in names if v["id_name_family"]==1 and v["name"] in m}
# #     spanishNames = {v["id_geoentity"]: v["name"] for v in names if v["id_name_family"]==3 and 
# #                     v["id_geoentity"] in isoCodes.keys()}
# #     englishNames = {v["id_geoentity"]: v["name"] for v in names if v["id_name_family"]==2 and 
# #                     v["id_geoentity"] in isoCodes.keys()}

# #     countries = dict()
# #     for k,v in isoCodes.iteritems():
# #         n = dict()
# #         n["es"] = spanishNames[k]
# #         n["en"] = englishNames[k]
# #         n["idGeoentity"] = k
# #         countries[v] = n
            
# #     return(countries)


# # def getCountriesIsoByVariableFamily(family):
# #     """Returns a list of country ISO codes in variable family."""
# #     return([c for c in cacheWrapper(getCountryDataByVariableFamily, family).keys()])

def getBlockMembers(isoBlock, year=None):
    """Returns a list of block members ISO."""
    return([datacache.geoentityToIso[i["id_geoentity_child"]] for i in 
            cacheWrapper(maplex.getBlockMembers, datacache.isoToGeoentity[isoBlock],
                         year=year)])

# def getBlockMembersIso(isoBlock, year=None):
#     """Returns a list of ISO codes for a block and a year."""
#     return([c for c in cacheWrapper(getBlockMembers, isoBlock, year=year).keys()])


# # def getListFromDictionary(dictionary, key):
# #     """Returns a list from the elements with a key in a dictionary."""
# #     out = []
# #     for i in dictionary:
# #         out.append(i[key])
# #     return(out)


# # def getOrderedDictionary(dict):
# #     """Returns an ordered dictionaty."""
# #     collator = PyICU.Collator.createInstance(PyICU.Locale("es_ES.UTF-8"))
# #     od = collections.OrderedDict()
# #     s = sorted(dict.keys(), cmp=collator.compare)
# #     for i in s:
# #         od[i] = dict[i]

# #     return od


# def getVariableYears(family):
#     """Returns a list for years present in IEPG/IEPE data."""
#     return(sorted(varengine.getVariableYears(family, 'energy')))
    

# # def getGeoentityBlocks(isoGeoentity, year=None):
# #     """Return the ISO code of block from isoGeoentity."""
# #     id = maplex.getIdGeoentityByName(isoGeoentity, 1)
# #     blocks = maplex.getGeoentityBlocks(id[0]["id_geoentity"], year)
# #     return(maplex.getGeoentityNames(blocks[0]["id_geoentity_block"], 4)[0]["names"][0])


# # def getVariables(family=None):
# #     """Return variables for an optional family."""
# #     idFamily = engine.getIdFamilyByName(family) if family else None
# #     return(engine.getVariables(idFamily))


# def isBlock(isoGeoentity):
#     """Returns True if isoGeoentity is a block."""
#     return(maplex.getIdGeoentityByName(isoGeoentity, 4)<>[])


def getData(variable, code=None, year=None, countryList=None):
    """Returns variable value. If countryList is present, only data for this countries 
    are returned. countryList can mix calculated and uncalculated codes. If code is not None,
    countryList is ignored."""
    if countryList:
        values = []
        for i in countryList:
            values.extend(getData(variable, code=i, year=year))
        return(values)

    # Try to get data if it exists in data
    v = variable.getData(code=code, year=year)
    if v[0]:
        out = v
    else:
        # It must be a block that has to be precalculated
        if code in datacache.blocks:
            if year:
                va = dict()
                members = getBlockMembers(code, year)
                values = [i for i in variable.getData(year=year) if i["code"] in members]
                va["code"]=code
                va["year"]=year
                va["value"] = const.blockFunctCalcFamilies[variable.dataset.idDataset](values)
                out = [va]
            else:
                v = []
                for y in variable.getVariableYears():
                    v.extend(getData(variable, code=code, year=y))
                out = v
        else:
            out = [None]

    return(out)
