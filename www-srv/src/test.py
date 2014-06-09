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

dataInterface = e.DataInterfacePostgreSql()
dataInterface.readAll("iepg_data_redux.iepg_data", "code", "date_in", "date_out")
dataStore = e.DataStorePostgreSql("store", "store")
dataStore.remove()
dataStore.setup()
dataStore.createDataSet("iepg")
dataStore.createVariable("iepg", "energy", True, "float")
dataStore.createVariable("iepg", "information", True, "float")



# iepg = e.DataSet("iepg")
# energy = e.Variable("energy", True, "float", iepg)
# information = e.Variable("information", True, "float", iepg)

# dataStore = e.DataStorePostgreSql("store", "store")
# # dataStore.remove()
# # dataStore.setup()

# dataInterface = e.DataInterfacePostgreSql()
# dataInterface.readAll("iepg_data_redux.iepg_data", "code", "date_in", "date_out")
# energy.loadFromDataInterface(dataInterface, "energy")
# information.loadFromDataInterface(dataInterface, "information")
# dataInterface.clearData()

# energy.addValue("XBAP", 1990, "blockfunc::common.blockfunctions.blockFunctionLumpSum", None)
# energy.addValue("XBAP", 1995, "blockfunc::common.blockfunctions.blockFunctionLumpSum", None)
# energy.addValue("XBAP", 2000, "blockfunc::common.blockfunctions.blockFunctionLumpSum", None)
# energy.addValue("XBAP", 2005, "blockfunc::common.blockfunctions.blockFunctionLumpSum", None)

# energyCache = e.DataCacheNumpy("energyCache")
# energyCache.cacheData(energy)
# informationCache = e.DataCacheNumpy("informationCache")
# informationCache.cacheData(information)

# dataStore.registerDataSet(iepg)



# dataSet = e.DataSet("dataset")
# variable = e.Variable("variable", True, "float", dataSet=dataSet)
# variable.loadFromDataInterface(dataInterface, "energy")
# dataStore.registerDataSet(dataSet)

# dataCache.cacheData(variable)



# # This creates a DataStore in PostgreSQL
# datastore = e.DataStorePostgreSql("ds", connection=PostgreSQL.connection)
# # This creates a dataset
# dataset = e.Dataset("dataset")




# code=None
# year=2013
# cl = ["XBAP", "XBEU", "XBSA"]


# for k,v in dc.variables.iteritems():
#     print k
#     print v.tableName()

# # print h.getData(dc.variables["iepe_individual_contribution_energy"], code=code, 
# #                 year=year, countryList=cl)
