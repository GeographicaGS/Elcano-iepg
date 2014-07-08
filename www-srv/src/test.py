# coding=UTF8

import common.blockfunctions
reload(common.blockfunctions)
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
reload(common.const)
import common.config as config
#reload(config)
from collections import OrderedDict

import common.datacache as dc
reload(dc)


# var = dc.dataSets["iepg_relative_contribution"].variables["soft_global"]
# var.delValue(code="XBSA")
# var.delValue(code="DE")
# var.addValue("XBSA", 2013, "blockfunc::common.blockfunctions.blockFunctionRelativeContributions", None)
# var.addValue("DE", 1990, "blockfunc::common.blockfunctions.blockFunctionRelativeContributions", None)
# print "XBSA", var.getData(code="XBSA", year=2013)
# print "DE", var.getData(code="DE", year=1990)

print dc.dataSets["iepg_relative_contribution"].variables["primary_goods"].getData(code="XBAP")

