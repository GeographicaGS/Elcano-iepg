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



dataStore = e.DataStorePostgreSql("store", "store")
dataCache = e.DataCacheNumpy("cache")
dataStore.remove()
dataStore.setup()

dataInterface = e.DataInterfacePostgreSql()
dataInterface.read("iepg_data_redux.iepg_data", "code", "date_in", "date_out", "energy")

dataSet = e.DataSet("dataset")
variable = e.Variable("variable", True, "float", dataSet=dataSet)
variable.loadFromDataInterface(dataInterface, "energy")
dataStore.registerDataSet(dataSet)
variable.addValue("XBAP", "1990", "blockfunc::blockfunctions.blockFunctionLumpSum", None)
variable.addValue("XBAP", "1995", "blockfunc::blockfunctions.blockFunctionLumpSum", None)
variable.addValue("XBAP", "2000", "blockfunc::blockfunctions.blockFunctionLumpSum", None)
variable.addValue("XBAP", "2005", "blockfunc::blockfunctions.blockFunctionLumpSum", None)



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
