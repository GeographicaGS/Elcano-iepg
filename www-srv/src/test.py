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

import common.datacache as dc
# reload(dc)


print dc.dataSets["context"].variables["gdp"].getData(code="US", year=1990)
print dc.dataSets["context"].variables["gdp"].getData(code="XBEU", year=1990)

# print h.getRanking(dc.blocksAndCountries, 2013, dc.dataSets["iepg"].variables["information"])

# print h.getRanking(["NZ", "MX", "ES", "XBAP", "XBEU"], 2000, dc.dataSets["iepg"].variables["energy"])


# di = e.DataInterfacePostgreSql()
# di.readAll("iepg_data_redux.iepg_data", "code", "date_in", "date_out")
# vinfo = e.Variable("information", True, "float")
# vinfo.loadFromDataInterface(di, "information")
# vinfo.setupCache(e.DataCacheNumpy)
# vinfo.cacheData()
