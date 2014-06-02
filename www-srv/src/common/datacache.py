# coding=UTF8

"""

Data cache.

"""

import varengine.varengine as varengine
import const
import common.cachewrapper as cachewrapper
import maplex.maplex as maplex
import copy
import arrayops

variables = dict()

for fam in const.variableDatasets:
    ds = varengine.Dataset(fam)
    ds.loadFromDatabase()
    for k,var in ds.variables.iteritems():
        var.cacheData(cacheWrapperFunc=cachewrapper.cacheWrapper)
        variables[var.tableName()] = var

blocks = [maplex.getGeoentityNames(i["id_geoentity_block"], 1)[0]["names"][0] for i in maplex.getBlocks()]
unprecalculatedBlocks = arraySubstraction(blocks, const.precalculatedBlocks)
countriesAndUe = variables["iepg_energy"].getVariableCodes()
countries = copy.deepcopy(countriesAndUe)
del countries[countries.index("XBEU")]
blocksAndCountries = copy.deepcopy(countries)
blocksAndCountries.extend(blocks)

isoToSpanish, spanishToIso = cachewrapper.cacheWrapper(maplex.getTranslationTable, 1, idNameFamilyB=3)
isoToSpanish = {key: value for key,value in isoToSpanish.iteritems() if key in blocksAndCountries}
spanishToIso = {key: value for key,value in spanishToIso.iteritems() if value in blocksAndCountries}

isoToEnglish, englishToIso = cachewrapper.cacheWrapper(maplex.getTranslationTable, 1, idNameFamilyB=2)
isoToEnglish = {key: value for key,value in isoToEnglish.iteritems() if key in blocksAndCountries}
englishToIso = {key: value for key,value in englishToIso.iteritems() if value in blocksAndCountries}

isoToGeoentity, geoentityToIso = cachewrapper.cacheWrapper(maplex.getTranslationTable, 1)
isoToGeoentity = {key: value for key,value in isoToGeoentity.iteritems() if key in blocksAndCountries}
geoentityToIso = {key: value for key,value in geoentityToIso.iteritems() if value in blocksAndCountries}
