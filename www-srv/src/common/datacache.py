# coding=UTF8

"""

Data cache.

"""
import varengine.varengine as varengine
import const
import common.helpers as helpers

variables = dict()

for fam in const.variableDatasets:
    ds = varengine.Dataset(fam)
    ds.loadFromDatabase()
    for k,var in ds.variables.iteritems():
        var.cacheData(cacheWrapperFunc=helpers.cacheWrapper)
        variables[var.tableName()] = var

