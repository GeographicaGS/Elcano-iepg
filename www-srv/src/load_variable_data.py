# coding=UTF8

"""

Variable data loader.

"""

import common.const as const
reload(const)
import varengine.varengine as varengine
reload(varengine)

dataStore = varengine.DataStorePostgreSql("store", "store")
dataStore.remove()
dataStore.setup()

for fam in const.variableNames.keys():
    d = varengine.DataSet(fam)
    mapping = dict()
    for k,var in const.variableNames[fam].iteritems():
        v = varengine.Variable(k, True, "float", dataSet=d)
        mapping[k]=var["column"]

    dataStore.registerDataSet(d)


