import common.blockfunctions
reload(common.blockfunctions)
import common.helpers as h
reload(h)
import varengine.varengine as e
reload(e)
import maplex.maplex as m
reload(m)
import maplex.maplexmodel
reload(maplex.maplexmodel)
import varengine.varenginemodel
reload(varengine.varenginemodel)
import common.const
reload(common.const)
import common.config as config
reload(config)
from collections import OrderedDict

import common.datacache as dc
# reload(dc)




# print OrderedDict(sorted(h.getRanking(dc.countries, 2013, dc.variables["iepg_energy"]).items(), 
#                          key=lambda t: t[1]))

print dc.variables["iepg_information"].getData(year=1990)

print sorted(h.getRanking(dc.blocksAndCountries, 1990, dc.variables["iepg_energy"]), key=lambda t: t["rank"])
# print OrderedDict(sorted(h.getRankingCode(dc.blocksAndCountries, 1990, dc.variables["iepg_energy"], "US")
