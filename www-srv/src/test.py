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
import common.arrayops as arrayops
reload(arrayops)
import common.const
reload(common.const)
import common.config as config
reload(config)
from collections import OrderedDict

import common.datacache as dc
# reload(dc)

code=None
year=2013
cl = ["XBAP", "XBEU", "XBSA"]

print dc.variables

print h.getData(dc.variables["iepe_individual_contribution_energy"], code=code, 
                year=year, countryList=cl)
