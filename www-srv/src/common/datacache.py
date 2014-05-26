# coding=UTF8

"""

Data cache.

"""
import varengine.varengine as varengine
import const
import common.helpers as helpers

caches = dict()

for fam in const.variableDatasets:
    ds = varengine.Dataset(fam)
    ds.loadFromDatabase()
    for k,var in ds.variables.iteritems():
        d = helpers.cacheWrapper(varengine.DataCache, var)
        caches[fam+"__"+k] = d
