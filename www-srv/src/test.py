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

import common.datacache as dc
reload(dc)

# print h.getData(dc.variables["iepg_energy"], year=2013)
# print h.getData(dc.variables["iepg_energy"], code="US")
# print h.getData(dc.variables["iepg_energy"], code="US", year=2013)

# print h.getData(dc.variables["iepg_energy"], code="XBEU")
# print h.getData(dc.variables["iepg_energy"], code="XBEU", year=2013)

print h.getData(dc.variables["iepg_energy"], code="XBAP")
print h.getData(dc.variables["iepg_energy"], code="XBAP", year=2013)

