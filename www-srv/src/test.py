# coding=UTF8

import common.blockfunctions
#reload(common.blockfunctions)
import common.helpers as h
reload(h)
import varengine.varengine as e
reload(e)
import maplex.maplex as m
#reload(m)
import maplex.maplexmodel
#reload(maplex.maplexmodel)
# import varengine.varenginemodel
# reload(varengine.varenginemodel)
import common.arrayops as arrayops
#reload(arrayops)
import common.const
#reload(common.const)
import common.config as config
#reload(config)
from collections import OrderedDict

#import common.datacache as dc
#reload(dc)

import common.cachewrapper
import datacache_memcache


# print h.getRanking(dc.blocksAndCountries, 1990, dc.dataSets["iepg"].variables["information"])

print h.getData(dc.dataSets["iepg"].variables["manufactures"], year=2013, 
                countryList=["XBSA", "XBEU", "XBNA", "XBE2", "XBLA", "XBMM", "XBAP"])

# print h.getData(dc.dataSets["iepg"].variables["manufactures"])

# print h.getRanking(["NZ", "MX", "ES", "XBAP", "XBEU"], 2000, dc.dataSets["iepg"].variables["energy"])


# di = e.DataInterfacePostgreSql()
# di.readAll("iepg_data_redux.iepg_data", "code", "date_in", "date_out")
# vinfo = e.Variable("information", True, "float")
# vinfo.loadFromDataInterface(di, "information")
# vinfo.setupCache(e.DataCacheNumpy)
# vinfo.cacheData()
