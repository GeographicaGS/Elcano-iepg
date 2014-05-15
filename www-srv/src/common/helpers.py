# coding=UTF8

"""

Common helpers.

"""
import hashlib
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


def blocksGetData(code):
    """Retrieves block data."""
    return(blocks[code])


def blocksCalculateData(blockCode, year, family, variable):
    """Calculates block data for a variable."""
    m = model.iepgdatamodel.IepgDataModel()
    block = blocksGetData(blockCode)
    data = cacheWrapper(m.getCountriesData, block["members"][str(year)], year, family, variable)
    return(data)
