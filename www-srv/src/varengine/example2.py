import common.blockfunctions
reload(common.blockfunctions)
# import common.helpers as h
# reload(h)
import varengine.varengine as e
reload(e)
import maplex.maplex as m
reload(m)
import maplex.maplexmodel
reload(maplex.maplexmodel)
# import varengine.varenginemodel
# reload(varengine.varenginemodel)
import common.arrayops as arrayops
reload(arrayops)
import common.const
reload(common.const)
import common.config as config
reload(config)
from collections import OrderedDict

# import common.datacache as dc
# # reload(dc)

"""
Classes:

DataStore: storage of data in symbolic form (drivers: PostgreSQL)
DataCache: storage of postprocessed data (drivers: Numpy)
DataSet: set of variables
Variable: variable
DataInterface: interface to origin data sources (drivers: PostgreSQL)
"""

iepg = e.DataSet("iepg")
energy = e.Variable("energy", True, "float", dataSet=iepg)
information = e.Variable("information", True, "float", dataSet=iepg)

dataInterface = e.DataInterfacePostgreSql()
dataInterface.readAll("iepg_data_redux.iepg_data", "code", "date_in", "date_out")
iepg.loadVariableDataFromDataInterface(dataInterface)

energy.addValue("XBAP", 1990, "blockfunc::common.blockfunctions.blockFunctionLumpSum", None)
energy.addValue("XBAP", 1995, "blockfunc::common.blockfunctions.blockFunctionLumpSum", None)
energy.addValue("XBAP", 2000, "blockfunc::common.blockfunctions.blockFunctionLumpSum", None)
energy.addValue("XBAP", 2005, "blockfunc::common.blockfunctions.blockFunctionLumpSum", None)
energy.addValue("XBAP", 2010, "blockfunc::common.blockfunctions.blockFunctionLumpSum", None)
energy.addValue("XBAP", 2011, "blockfunc::common.blockfunctions.blockFunctionLumpSum", None)
energy.addValue("XBAP", 2012, "blockfunc::common.blockfunctions.blockFunctionLumpSum", None)
energy.addValue("XBAP", 2013, "blockfunc::common.blockfunctions.blockFunctionLumpSum", None)

dataStore = e.DataStorePostgreSql("store","store")
dataStore.remove()
dataStore.setup()

dataStore.registerDataSet(iepg)

energy.setupCache(e.DataCacheNumpy)
energy.cacheData()



